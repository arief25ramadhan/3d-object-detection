# import sys
# import cv2
# sys.path.append('mmdetecion3d/')

# from mmdet3d.apis import MonoDet3DInferencer
# from mmdet3d.apis import init_model, inference_detector, inference_mono_3d_detector

# config_file = 'mmdetection3d/configs/pgd/pgd_r101-caffe_fpn_head-gn_4xb3-4x_kitti-mono3d.py'
# checkpoint_file = 'mmdetection3d/pgd_r101_caffe_fpn_gn-head_3x4_4x_kitti-mono3d_20211022_102608-8a97533b.pth'
# # model = init_model(config_file, checkpoint_file)
# # result = inference_mono_3d_detector(model, 'mmdetection3d/demo/data/kitti/000008.png', 'mmdetection3d/demo/data/kitti/000008.pkl', cam_type='CAM2', show=True)
# # print(result)

# inferencer = MonoDet3DInferencer(config_file, checkpoint_file)
# inputs = dict(img='mmdetection3d/demo/data/kitti/000008.png', infos='mmdetection3d/demo/data/kitti/000008.pkl')

# # results = inferencer(inputs, show=False, out_dir='./remote_outputs')

# results = inferencer(inputs, return_vis=True)
# print(results['visualization'][0])

# cv2.imwrite('aa.jpg', results['visualization'][0])
# # print(results['predictions'])

# # for key in results:
# #     print(key)


import mmcv
import numpy as np
from mmengine import load
import sys
import cv2
sys.path.append('mmdetecion3d/')

from mmdet3d.visualization import Det3DLocalVisualizer
from mmdet3d.structures import CameraInstance3DBoxes

info_file = load('mmdetection3d/demo/data/kitti/000008.pkl')
cam2img = np.array(info_file['data_list'][0]['images']['CAM2']['cam2img'], dtype=np.float32)
bboxes_3d = []
for instance in info_file['data_list'][0]['instances']:
    bboxes_3d.append(instance['bbox_3d'])
gt_bboxes_3d = np.array(bboxes_3d, dtype=np.float32)
gt_bboxes_3d = CameraInstance3DBoxes(gt_bboxes_3d)
input_meta = {'cam2img': cam2img}

visualizer = Det3DLocalVisualizer()

img = mmcv.imread('mmdetection3d/demo/data/kitti/000008.png')
img = mmcv.imconvert(img, 'bgr', 'rgb')
visualizer.set_image(img)
# project 3D bboxes to image
visualizer.draw_proj_bboxes_3d(gt_bboxes_3d, input_meta)

cv2.imwrite('test.jpg', img)

# print(img_out)

# visualizer.show()