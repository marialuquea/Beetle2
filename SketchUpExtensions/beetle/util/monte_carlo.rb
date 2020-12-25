require 'beetle/util/distributions'
require 'bigdecimal'

module EdinburghNapier::Beetle
    module Simulation
        class MonteCarlo
            def initialize(variable_lower, variable_upper, type, boundaries)
                @outputs = Array.new(5000, 0)
                if (type == "Uniform")
                    ecc = Distributions::Uniform.new(boundaries[0], boundaries[1])
                    runMonteCarlo(variable_lower, variable_upper, ecc)
                elsif(type == "Triangular")
                    ecc = Distributions::Triangle.new(boundaries[0], boundaries[1], boundaries[2])
                    runMonteCarlo(variable_lower, variable_upper, ecc)
                elsif(type == "Gaussian")
                    ecc = Distributions::Normal.new(boundaries[0], boundaries[1])
                    runMonteCarlo(variable_lower, variable_upper, ecc)
                end
            end

            def getOutputs
                return @outputs
            end

            private

            def runMonteCarlo(variable_lower, variable_upper, ecc)
                if (variable_upper < variable_lower)
                    variable_upper = variable_lower
                end

                material = Distributions::Uniform.new(variable_lower, variable_upper)
                for i in 0..4999
                    @outputs[i] = material.rand * ecc.rand
                end
            end
        end
    end
end
