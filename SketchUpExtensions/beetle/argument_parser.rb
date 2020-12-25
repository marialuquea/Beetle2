module EdinburghNapier::Beetle
  class ArgumentParser

    def parse(*args)
      if args.size == 1 && args[0].is_a?(Hash)
        get_options_hash(args.first)
      end
    end

    private

    def get_options_hash(options)
      options = {
        title: options[:title],
        calculate_button: options[:calculate_button],
        cancel_button: options[:cancel_button],
        material: options[:material].map(&:as_json),
        uniform: options[:uniform].map(&:as_json),
        gaussian: options[:gaussian].map(&:as_json),
        triangular: options[:triangular].map(&:as_json),
        distribution: options[:distribution].map(&:as_json),
        geometry: options[:geometry].map(&:as_json),
        loads: options[:loads].map(&:as_json)
      }
    end

    def ensure_array(arguments, index)
      unless arguments[index].is_a?(Array)
        raise ArgumentError, "argument #{index} must be an array"
      end
      arguments[index]
    end

  end # class
end # module
