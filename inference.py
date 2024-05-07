import sys
import cv2
sys.path.append('mmdetecion3d/')

from mmdet3d.apis import MonoDet3DInferencer
from mmdet3d.apis import init_model, inference_detector, inference_mono_3d_detector

config_file = 'mmdetection3d/configs/pgd/pgd_r101-caffe_fpn_head-gn_4xb3-4x_kitti-mono3d.py'
checkpoint_file = 'mmdetection3d/pgd_r101_caffe_fpn_gn-head_3x4_4x_kitti-mono3d_20211022_102608-8a97533b.pth'
# model = init_model(config_file, checkpoint_file)
# result = inference_mono_3d_detector(model, 'mmdetection3d/demo/data/kitti/000008.png', 'mmdetection3d/demo/data/kitti/000008.pkl', cam_type='CAM2', show=True)
# print(result)

inferencer = MonoDet3DInferencer(config_file, checkpoint_file)
inputs = dict(img='mmdetection3d/demo/data/kitti/000008.png', infos='mmdetection3d/demo/data/kitti/000008.pkl')

results = inferencer(inputs, show=False, out_dir='./remote_outputs')

print(results['visualization'][0])

for key in results:
    print(key)
