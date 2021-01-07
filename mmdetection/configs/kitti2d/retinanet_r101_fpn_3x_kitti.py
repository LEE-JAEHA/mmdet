_base_ = [
    '../_base_/models/retinanet_r101_fpn.py',
    '../_base_/datasets/kitti2d_detection.py',
    '../_base_/schedules/schedule_3x.py', '../_base_/default_runtime.py'
]
# optimizer
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
model = dict(bbox_head=dict(num_classes=1))
total_epochs = 1