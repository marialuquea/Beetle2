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

          js_command = "checkSliders()"
          window.execute_script(js_command)

          # Convert inputs to their type and into a single array list (results)
          results_dist = []
          correct_dists = true
          if distribution[0] == 'Uniform'
            results_dist = convert_values(@options, distribution[0], uniform)
            if (results_dist[0] >= results_dist[1])
              correct_dists = false
            end
          elsif distribution[0] == 'Triangular'
            results_dist = convert_values(@options, distribution[0], triangular)
            if (results_dist[0] >= results_dist[1] && results_dist[2] >= results_dist[0] && results_dist[2] <= results_dist[1])
              correct_dists = false
            end
          elsif distribution[0] == 'Gaussian'
            results_dist = convert_values(@options, distribution[0], gaussian)
            if ((results_dist[0] - (3 * results_dist[1]) < 0))
              correct_dists = false
            end
          end 
          results_geometry = convert_values(@options, 'geometry', geometry)
          results_loads = convert_values(@options, 'loads', loads)
          results_distribution_name = convert_values(@options, 'distribution', distribution)
          results = results_geometry.push(*results_loads).push(*results_distribution_name).push(*results_dist)


          if !results.any?{ |e| e.nil? } && correct_dists
            begin
              preds = Predictions::ApplyModel.new(results_geometry, results_loads, distribution[0], results_dist, material)
              #puts "preds", preds
              histogram_data = preds.returnHistogramData() # method in apply_model.rb
              js_command = "plot_histogram(" + histogram_data.to_s + ")"
              window.execute_script(js_command)
            rescue NoMethodError => e
              puts "Error in html_ui.rb: ", e, "PLOTTING EMPTY HISTOGRAM in rescue mode"
              window.execute_script("plot_histogram('')")
            end
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