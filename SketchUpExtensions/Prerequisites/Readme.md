0. Install Visual Studio Code
1. Download Ruby and install it on your computer (https://rubyinstaller.org/)
2. Start cmd with Ruby and do $gem install rubocop-sketchup
3. Follow the tutorial on this website to set up the Sketchup Extension for VSCode (https://github.com/SketchUp/sketchup-extension-vscode-project)
4. Follow the steps on bundler.io (https://bundler.io/)
5. Follow the rest of the steps on https://github.com/SketchUp/sketchup-extension-vscode-project
6. The previous steps mentioned I struggled with actually to get working. In essence
to get the scripts running. You are supposed to have the .rb within the plugins folder and
run them from within SketchUp otherwise you'll get a "Sketchup.rb not found" error, this due to the fact
that THERE IS A SEPERATE RUBY INSTALL WITHIN SKETCHUP :( .
So the best way to run scripts outside of the plugins folder (otherwise source control will be a nightmare)
is to have a script within the plugins folder and have it linked to your actual folder.
7. Go to the SketchUp plugins folder (In my case it was "C:\Users\Maria\AppData\Roaming\SketchUp\SketchUp 2020\SketchUp\Plugins")
8. Copy into that folder the external.rb script MAKE SURE TO CHANGE THE DIRECTORIES TO SUIT THE ONES ON YOUR COMPUTER
9. Run the reload.rb script within SketchUp to reload the changes
10. Follow the steps on this page for debugging options https://github.com/SketchUp/sketchup-ruby-api-tutorials/wiki/VSCode-Debugger-Setup
	In order to run with SketchUp with debugging run the following command from cmd "SketchUp.exe -rdebug "ide port=7000"


Authors Note: The way this is explained on the official site is extremely frustrating and unintuitive and
I've wasted an entire day trial and erroring these issues.
