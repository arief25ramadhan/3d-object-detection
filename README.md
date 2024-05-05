# 3d-object-detection

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)

## 1. Introduction

## 2. Installation

To use this repository, we need to set up our environment with its required libraries. The steps are:

1. Installation

   ```
   pip install torch==2.0.1 torchvision==0.15.2 
   python -m pip install pip==24.*
   pip install -U openmim
   mim install mmengine
   mim install 'mmcv>=2.0.0rc4'
   mim install 'mmdet>=3.0.0'
   ```

2. Go to the repository, and install dependencies:

   ```
   cd vehicle-tracking-counting
   pip install -r requirements.txt
   ```

3. Inside this current repo, clone the ByteTrack Libraries:

    ```
   git clone https://github.com/ifzhang/ByteTrack.git
   ```
    
4. Install ByteTrack dependencies:
   ```
   cd ByteTrack
   
   # workaround related to https://github.com/roboflow/notebooks/issues/80
   sed -i 's/onnx==1.8.1/onnx==1.9.0/g' requirements.txt

   pip install -r requirements.txt

   python3 setup.py develop
   pip install cython_bbox onemetric loguru lap thop
   ```


## 3. Usage


## References