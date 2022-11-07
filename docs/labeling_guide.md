# Labeling Guide

> **Warning** 
> 
> 本文内容是针对bdd100k数据集的标注指导

## Common Labeling Guide

- 请尽量避免标注过于模糊的目标，例如：由于人或者物已经出现了明显的模糊，或者由于目标的大小过小，导致目标的边界线模糊不清，这些都是不合理的标注，可以不用标注，或者添加`difficult`标签。
- 对于影响驾驶安全特别小的小目标，例如路边很远处的人、障碍物等，可以不用标注，或者添加`difficult`标签。

## Bounding Box

类别应该包含十类
```yaml
- name: pedestrian
- name: rider
- name: car
- name: truck
- name: bus
- name: train
- name: motorcycle
- name: bicycle
- name: traffic light
- name: traffic sign
```

注意事项：
- `pedestrian`：仅需要标注行人，而不是所有人。例如骑车的人不需要标注
- `rider`：需要标注车和人的最大外接矩形
- `truck`：如果不确定是否是卡车，可以标注为`car`
- `bus`：如果不确定是否是公交车，可以标注为`car`
- `traffic light`：标注红绿灯的最大外接矩形，而不是单个灯泡. **与bdd100k不同的是，不需要标注灯的颜色**


## Polygon

> **Note**
>
> scalabel所支持的`polygon`得到的结果是`rle`格式的mask，而不是polygon格式的mask. 可用于`instance segmentation`、`panoptic segmentation`等任务。

> **Warning**
>
> 但是请注意，虽然可通行区域的标注也是`polygon`，但是生成的结果类别与`instance segmentation`不兼容，需要单独处理。

## Polyline


## 3D Bounding Box

## Tagging