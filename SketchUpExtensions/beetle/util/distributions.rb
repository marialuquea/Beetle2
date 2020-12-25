module EdinburghNapier::Beetle
    module Distributions
        class Uniform
            def initialize(lower, upper, rand_helper = lambda { Kernel.rand })
                @upper = upper.to_f
                @lower = lower.to_f
                @rand_helper = lambda { Kernel.rand(@lower..@upper) }
            end

            def rand
                return @rand_helper.call
            end
        end
        
        class Normal
            def initialize(mean, stddev, rand_helper = lambda { Kernel.rand })
              @rand_helper = rand_helper
              @mean = mean.to_f
              @stddev = stddev.to_f
              @valid = false
              @next = 0
            end
          
            def rand
              if @valid then
                @valid = false
                return @next
              else
                @valid = true
                x, y = self.class.normal(@mean, @stddev, @rand_helper)
                @next = y
                return x
              end
            end
          
            private
            def self.normal(mean, stddev, rand)
              theta = 2 * Math::PI * rand.call
              rho = Math.sqrt(-2 * Math.log(1 - rand.call))
              scale = stddev * rho
              x = mean + scale * Math.cos(theta)
              y = mean + scale * Math.sin(theta)
              return x, y
            end
          end

        class Triangle
            def initialize(lower, upper, mode)
                @lower = lower.to_f
                @upper = upper.to_f
                @mode = mode.to_f
            end

            def rand
                proposal = 0.0
                while true
                    acceptance_prob = 0.0
                    proposal = Kernel.rand(@lower..@upper)
                    if (proposal < @mode)
                        acceptance_prob = (proposal - @lower).to_f / (@mode - @lower).to_f
                    else
                        acceptance_prob = (@upper - proposal).to_f / (@upper - @mode).to_f
                    end
                    break if Kernel.rand() < acceptance_prob
                end
                return proposal
            end
        end
    end
  end

