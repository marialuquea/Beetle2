# Copyright 2016 Trimble Inc
# Licensed under the MIT license

require 'sketchup.rb'
require 'extensions.rb'

module EdinburghNapier
  module Beetle

    unless file_loaded?(__FILE__)
      ex = SketchupExtension.new('Beetle', 'beetle/main')
      ex.description = 'SketchUp Ruby API implementation of BEETLE.'
      ex.version     = '1.0.0'
      ex.copyright = 'Edinburgh Napier © 2020'
      ex.creator     = 'Michal Lange & Maria Luque Anguita'
      Sketchup.register_extension(ex, true)
      file_loaded(__FILE__)
    end

  end # module Beetle
end # module Edinburgh Napier
