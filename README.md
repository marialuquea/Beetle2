# Beetle2
An artificially-intelligent tool to estimate the whole life carbon emissions of building structures

There are 3 main projects in this repository:
- The python notebook used to experiment with the datasets and Machine Learning models
- The python app that can be used as a tool to predict carbon emission of building structures
- The sketchup ruby app

## To open the Python notebook

### 1. If you don't have it - install conda
1. **Check you don't already have conda installed!**
    1. `which conda`
    1. **if you already have it installed, skip ahead to Create an Environment**
    1. It doesn't matter if you have miniconda3, or anaconda3 installed (it does not even matter if it is version 2).
1. If you don't have conda, download the latest version of miniconda3
    1. `cd ~/Downloads`
    1. Download the installer (miniconda carries less baggage), depending on your system (you can check links [here](https://conda.io/miniconda.html)):
        * Linux: `wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh`
        * Mac: `wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh` or ```curl -LOk https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh```
        * Or just simply download from [the site](https://conda.io/miniconda.html)
1. Install miniconda3 *with default settings*
    1. `bash Miniconda3-latest-Linux-x86_64.sh`
    1. Follow the prompt - **type `yes` and hit `enter` to accept all default
    settings when asked**
1. Close Terminal and reopen
1. Try executing `conda -h`. If it works, you can delete the installer ```rm ~/Downloads/Miniconda3-latest-Linux-x86_64.sh```

#### Windows users
* Please follow conda installation instructions on their
website [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)


### 2. Create an environment for the project - optional
1. Update conda: `conda update conda`
1. Create the environment for the project. Call it beetle and install python 3 (*hence the name*):
```conda create -n beetle python=3.8 ```

 `source activate beetle` will activate the new environment and `conda deactivate` will exit it.

 Windows users should instead use `conda activate beetle`

### 3. Open the Python Notebook
First you need to activate the software environment and then
start a Jupyter Notebook session from within the folder where the project is
stored.

1. Activate the conda environment: `source activate beetle`
2. Enter the directory where you downloaded the project material:
`cd betle2`
3. Start a jupyter notebook
    * `jupyter notebook`
4. This should automatically open your browser
    * Click on `Beetle2.ipynb ` to open it

If step 3 fails, try
- `pip install jupyter` and then `jupyter notebook`
- searching for the app 'Anaconda navigator' and manually launch Jupyter Notebook


# TODO
- [x] Change dataset URL to github link in python notebook
- [ ] Change readme: add instructions to open Sketchup plugin and python standalone
