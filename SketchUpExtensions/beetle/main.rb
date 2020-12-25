# Copyright 2016 Trimble Inc
# Licensed under the MIT license

require 'sketchup.rb'
require 'beetle/html_ui'
require 'beetle/input/textbox'
require 'beetle/input/dropdown'

module EdinburghNapier::Beetle

    unless file_loaded?(__FILE__)
      menu = UI.menu('Plugins').add_submenu('HTML InputBox')
      menu.add_item('Beetle options'){
        self.prompt_beetle_options
      }
      file_loaded(__FILE__)
    end

    # Inputs
    def self.prompt_beetle_options
      puts "Promp Beetle Inputs"
      options = {
        title: 'Beetle Inputs',
        cancel_button: 'Cancel',
        calculate_button: 'Calculate',
        material: [
          HtmlUI::Dropdown.new('Material', 'Steel', ['Steel', 'Reinforced Concrete', 'Glulam'])
        ],
        uniform: [
          HtmlUI::Textbox.new('LOWER BOUND', 1.0), # 1-5
          HtmlUI::Textbox.new('UPPER BOUND', 1.0)  # 1-5    
        ],
        gaussian: [
          HtmlUI::Textbox.new('MEAN', 1.0), # 1-5
          HtmlUI::Textbox.new('STANDARD DEVIATION', 1.0) # 1-5
        ],
        triangular: [
          HtmlUI::Textbox.new('LOWER BOUND', 1.0), # 1-5
          HtmlUI::Textbox.new('UPPER BOUND', 1.0), # 1-5
          HtmlUI::Textbox.new('MODE', 1.0) # 1-5
        ],
        distribution: [
          HtmlUI::Dropdown.new('EMBODIED CARBON COEFFICIENT [kgCO<sub>2</sub>e/kg<sub>MAT</sub>]', 'Uniform', ['Uniform', 'Gaussian', 'Triangular'])
        ],
        geometry: [
          HtmlUI::Textbox.new('PRIMARY SPAN [m]', 1.0), # 5-9
          HtmlUI::Textbox.new('SECONDARY SPAN [m]', 1.0), # 5-12
          HtmlUI::Textbox.new('INTER-STOREY HEIGHT [m]', 1.0), # 3.5-4
          HtmlUI::Textbox.new('NO. OF PRIMARY SPANS', 1), # 2-21
          HtmlUI::Textbox.new('NO. OF SECONDARY SPANS', 1), # 1-13
          HtmlUI::Textbox.new('NO. OF STOREYS', 1) # 1-10
        ],
        loads:[
          HtmlUI::Textbox.new('VARIABLE FLOOR LOAD', 1.0), # 1-5
          HtmlUI::Textbox.new('FINISHES, CEILING, SERVICES AND PARTITIONS LOAD', 1.0), # 0-1.75
          HtmlUI::Textbox.new('ENVELOPE WALLS LOAD', 1.0) # 1-5
        ]
      }
      dialog = HtmlUI::InputBox.new(options) 
      results = dialog.prompt
    end

  end
