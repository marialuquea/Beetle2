require 'beetle/predictions/steel_optimised'
require 'beetle/predictions/steel_rationalised'
require 'beetle/predictions/concrete_optimised'
require 'beetle/predictions/concrete_rationalised'
require 'beetle/predictions/glulam_rationalised'
require 'bigdecimal'
require 'beetle/util/distributions'
require 'beetle/util/monte_carlo'

module EdinburghNapier::Beetle
    module Predictions
        class ApplyModel
            BigDecimal.limit(30)

            attr_accessor :histogram_data

            def initialize(geometry, loads, distribution_type, distribution_value, material)
                # Calculate the total area
                area = geometry[0] * geometry[1] * geometry[3] * geometry[4]
                # Calculate the aspect ratio
                aspect_ratio = (geometry[0] * geometry[3]) / (geometry[1] * geometry[4])

                # GEOMETRY ORDER: area, aspect ratio, primary span, secondary span, 
                # primery span units, secondary span units, no of storeys, interstory height, max spacing (constant 2.6)

                # LOADS ORDER: floor slabs self, finishes ceiling, variable floor load, weight of envelope

                inputs = [area, aspect_ratio, geometry[0], geometry[1], geometry[3], geometry[4], geometry[5], geometry[2],
                        loads[1], loads[0], loads[2]]

                # Check which material we are trying to predict
                #puts "MATERIAL-",material

                if (material[0].eql?("Steel"))
                    steel_optimised = SteelOptimised.new
                    weights_optimised = steel_optimised.getWeights()
                    biases_optimised = steel_optimised.getBiases()
                    answer_optimised = createAndCalculate(inputs, weights_optimised, biases_optimised)[0].round()

                    steel_rationalised = SteelRationalised.new
                    weights_rationalised = steel_rationalised.getWeights()
                    biases_rationalised = steel_rationalised.getBiases()
                    answer_rationalised = createAndCalculate(inputs, weights_rationalised, biases_rationalised)[0].round()

                    mc = Simulation::MonteCarlo.new(answer_optimised, answer_rationalised, distribution_type, distribution_value)
                    histogram_output = mc.getOutputs
                    @histogram_data = histogram_output
                elsif (material[0] == "Reinforced Concrete")
                    concrete_optimised = ConcreteOptimised.new
                    weights_optimised = concrete_optimised.getWeights()
                    biases_optimised = concrete_optimised.getBiases()
                    answer_optimised = createAndCalculate(inputs, weights_optimised, biases_optimised)[0].round()

                    concrete_rationalised = ConcreteRationalised.new
                    weights_rationalised = concrete_rationalised.getWeights()
                    biases_rationalised = concrete_rationalised.getBiases()
                    answer_rationalised = createAndCalculate(inputs, weights_rationalised, biases_rationalised)[0].round()

                    mc = Simulation::MonteCarlo.new(answer_optimised, answer_rationalised, distribution_type, distribution_value)
                    histogram_output = mc.getOutputs
                    @histogram_data = histogram_output
                elsif (material[0] == "Glulam")
                    glulam_rationalised = GlulamRationalised.new
                    weights_rationalised = glulam_rationalised.getWeights()
                    biases_rationalised = glulam_rationalised.getBiases()
                    answer_rationalised = createAndCalculate(inputs, weights_rationalised, biases_rationalised)[0].round()
                    mc = Simulation::MonteCarlo.new(answer_rationalised, answer_rationalised, distribution_type, distribution_value)
                    histogram_output = mc.getOutputs
                    @histogram_data = histogram_output
                end
            end

            def returnHistogramData()
                return @histogram_data
            end

            private

            def createAndCalculate(inputs, weights, biases)
                if inputs.length != weights[0].length
                    puts "!!!Differing number of inputs!!!"
                    return
                end

                for layer in 0..(weights.length - 1)
                    outputs = Array.new(weights[layer][0].length, BigDecimal("0.0"))
                    for input in 0..(inputs.length - 1)
                        for weight in 0..(weights[layer][input].length - 1)
                            outputs[weight] += inputs[input] * weights[layer][input][weight]
                        end
                    end
                    for i in 0..(outputs.length - 1)
                        outputs[i] += biases[layer][i]
                        outputs[i] = relu(outputs[i])
                    end

                    inputs = outputs
                end
                inputs
            end


            def relu(x)
                if x < 0
                    0
                else
                    x
                end
            end

        end
    end
end