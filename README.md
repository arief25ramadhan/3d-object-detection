# 3d-object-detection

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)

## 1. Introduction

## 2. Installation

To use this repository, we need to set up our environment with its required libraries. The steps are:

1. Create new python virtual environment
    ```
    # Create a new virtual env named 3d_env
    python -m 
    
    # Go inside the virtual environment
    source 3d_env/bin/activate
    ```

2. Install required packages

   ```
   # Change pip version
   python -m pip install pip==24.*
   
   # Install pytorch and torchvision
   pip install torch==2.0.1 torchvision==0.15.2 

   ## Install mmengine, mmcv, and mmdet
   pip install -U openmim
   mim install mmengine
   mim install 'mmcv>=2.0.0rc4'
   mim install 'mmdet>=3.0.0'
   ```

3. Install the mmdetection3d library

   ```
   git clone https://github.com/open-mmlab/mmdetection3d.git -b dev-1.x
   # "-b dev-1.x" means checkout to the `dev-1.x` branch.
   cd mmdetection3d
   pip install -v -e .
   # "-v" means verbose, or more output
   # "-e" means installing a project in edtiable mode,
   # thus any local modifications made to the code will take effect without reinstallation.
   ```
## 3. Usage

## References