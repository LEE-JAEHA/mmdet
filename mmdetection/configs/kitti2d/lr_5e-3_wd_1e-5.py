_base_ = [
    '../_base_/models/retinanet_r50_fpn.py',
    '../_base_/datasets/kitti2d_detection.py',
    '../_base_/default_runtime.py'
]

model = dict(bbox_head=dict(num_classes=1))
data = dict(samples_per_gpus=12, workers_per_gpu=4)
# optimizer
optimizer = dict(type='SGD', momentum=0.9, lr=0.005, weight_decay=0.00001)
optimizer_config = dict(grad_clip=dict(max_norm=35, norm_type=2))
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[120, 170, 200])
total_epochs = 210

evaluation = dict(interval=5, metric='bbox')
checkpoint_config = dict(interval=5)
