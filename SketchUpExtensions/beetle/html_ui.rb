require 'json'
require 'beetle/argument_parser'
require 'beetle/generate_building'
require 'beetle/predictions/apply_model'


module EdinburghNapier::Beetle
  module HtmlUI
    # Class that uses UI::HtmlDialog to create a dialog box that operates
    # similar to UI.inputbox.
    class InputBox

      def initialize(*args)
        puts "Initialising..."
        defaults = {
          title: Sketchup.app_name,
          cancel_button: 'Cancel',
          calculate_button: 'Calculate',
          material: [],
          distribution: [],
          uniform: [],
          gaussian: [],
          triangular: [],
          geometry: []
        } 
        options = ArgumentParser.new.parse(*args)
        @options = defaults.merge(options)
      end

      def prompt
        results = []
        window_options = {
          :dialog_title => @options[:title],
          :preferences_key => 'com.example.html-input',
          :resizable => true,
          :scrollable => true,
          :width  => 500,
          :height => 450,
          :style => UI::HtmlDialog::STYLE_DIALOG
        }
        window = UI::HtmlDialog.new(window_options)
        inputbox_file = File.join(__dir__, 'html', 'inputbox.html')
        window.set_file(inputbox_file)

        window.add_action_callback('ready') { |action_context|
          json_options = JSON.pretty_generate(@options)
          window.execute_script("app.options = #{json_options}")
        }
        window.add_action_callback('calculate') { |action_context, material, geometry, loads, distribution, uniform, gaussian, triangular|

          #puts "-------TESTING--------","MATERIAL", material
          #puts "GEOMETRY", geometry
          #puts "LOADS",loads
          #puts "DISTRIBUTION", distribution
          #puts "UNIFORM", uniform
          #puts "GAUSSIAN", gaussian
          #puts "TRIANGLE", triangle

          puts "CHECKING SLIDERS"
          js_command = "checkSliders()"
          window.execute_script(js_command)

          # Convert inputs to their type and into a single array list (results)
          results_dist = []
          if distribution[0] == 'Uniform'
            results_dist = convert_values(@options, distribution[0], uniform)
          elsif distribution[0] == 'Triangular'
            results_dist = convert_values(@options, distribution[0], triangular)
          elsif distribution[0] == 'Gaussian'
            results_dist = convert_values(@options, distribution[0], gaussian)
          end 
          results_geometry = convert_values(@options, 'geometry', geometry)
          results_loads = convert_values(@options, 'loads', loads)
          results_distribution_name = convert_values(@options, 'distribution', distribution)
          results = results_geometry.push(*results_loads).push(*results_distribution_name).push(*results_dist)
          #puts results


          begin
            preds = Predictions::ApplyModel.new(results_geometry, results_loads, distribution[0], results_dist, material)
            #puts "preds", preds
            histogram_data = preds.returnHistogramData() # method in apply_model.rb
            puts "PLOTTING HISTOGRAM"
            js_command = "plot_histogram(" + histogram_data.to_s + ")"
            window.execute_script(js_command)
          rescue NoMethodError => e
            puts e
            puts "PLOTTING HISTOGRAM in rescue mode"
            js_command = "plot_histogram('')"
            window.execute_script(js_command)
          end

          # Generate Building in Sketchup
          Visualisation::BuildingGenerator.new(results_geometry.push(*results_loads))
        }
        window.add_action_callback('cancel') { |action_context|
          window.close
        }
        window.center
        window.show
      end

      private 

      def convert_values(options, name, values)
        values.each_with_index.map { |value, index|
          default = options[(name.downcase).to_sym][index][:default]
          case default
          when Length 
            value.to_l
          when Float 
            value.to_f
          when Integer 
            value.to_i
          else 
            value.to_s
          end
        }
      end


    end


  end # module HtmlUi
end # module EdinburghNapier::Beetle