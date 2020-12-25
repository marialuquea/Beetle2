require 'sketchup.rb'

module EdinburghNapier::Beetle
  module Visualisation
    class BuildingGenerator
      def initialize(results)
        # Undo the previous building
        Sketchup.undo
        # Make the current scene active for modelling
        model = Sketchup.active_model
        # Start operation so the user can easily undo
        model.start_operation('Create Buidling', true)
        # Initiate wireframe mode
        opts = Sketchup.active_model.rendering_options
        @old_mode = opts["RenderMode"]
        opts["RenderMode"] = 0

        group = model.active_entities.add_group
        entities = group.entities
        for z in 1..results[6] do
          for i in 1..results[4] do
            for j in 1..results[5] do
              points = create_cube(results[0], results[1], results[0] * i * 1.01, results[1] * j * 1.01, results[3] * z * 1.01)
              face = entities.add_face(points)
              adjustedresults = results[3]
              face.pushpull(-adjustedresults.m)
            end
          end
        end
        model.commit_operation
      end

      private

      def create_cube(x, y, xOffset, yOffset, zOffset)
        points = [
          Geom::Point3d.new(xOffset.m,   yOffset.m,   zOffset.m),
          Geom::Point3d.new(x.m + xOffset.m, yOffset.m,   zOffset.m),
          Geom::Point3d.new(x.m + xOffset.m, y.m + yOffset.m, zOffset.m),
          Geom::Point3d.new(xOffset.m,   y.m + yOffset.m, zOffset.m)
        ]
        points
      end
    end
  end
end
