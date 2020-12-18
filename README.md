# DIMCool_data_tool
For consolidating DIMCool/iFEED ascii outputs into netCDF, using ARC job scheduler


Setup:
* Log onto arc3
* clone this repo with `git clone https://github.com/cemac-ccs/DIMCool_data_tool`
* go into repo directory with `cd DIMCool_data_tool`
* make a note of the directory path returned from typing `pwd`
* If you haven't installed a personal version of conda, do so. I recommend installing in `/nobackup/${USER}`. Miniconda, a smaller version of Anaconda, can be downloaded and installed by the following:
```
cd /nobackup/${USER}
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
* Set up conda environment with `conda env create -f environment.yml`
* Edit paths to output directories, conda installation, and location of this repository in `Controller.sh`

Usage:
* Log onto arc3 and navigate to the repository directory
* Edit 'CROPS', 'REGIONS', 'MODELS' and 'RCPS' parameters in Controller.sh as needed
* Run Controller.sh script
