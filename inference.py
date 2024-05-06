from mmdetecion3d.mmdet3d.apis import MonoDet3DInferencer
from mmdet3d.apis import init_model, inference_detector


# python demo/mono_det_demo.py demo/data/kitti/000008.png demo/data/kitti/000008.pkl  
# configs/pgd/pgd_r101-caffe_fpn_head-gn_4xb3-4x_kitti-mono3d.py pgd_r101_caffe_fpn_gn-head_3x4_4x_kitti-mono3d_20211022_102608-8a97533b.pth --show --cam-type CAM2 --pred-score-thr 0.9

config_file = 'mmdetection3d/configs/pgd/pgd_r101-caffe_fpn_head-gn_4xb3-4x_kitti-mono3d.py' # 'pointpillars_hv_secfpn_8xb6-160e_kitti-3d-car.py'
checkpoint_file = 'pgd_r101_caffe_fpn_gn-head_3x4_4x_kitti-mono3d_20211022_102608-8a97533b.pth'
model = init_model(config_file, checkpoint_file)
inference_detector(model, 'demo/data/kitti/000008.png')