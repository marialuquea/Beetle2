require 'beetle/input/input'


module EdinburghNapier::Beetle
  module HtmlUI

    class Dropdown < Input

      def initialize(label, default = nil, options = [])
        super(label: label, default: default, options: options)
      end

    end # class

  end # module
end # module
