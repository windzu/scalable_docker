# Tutorial1 : BDD100K

## Introduction

这个教程将会带你了解如何使用scalabel按照BDD100K的格式标注数据，然后将数据转换为COCO格式，以及结合ADMLops完成yolopv2的训练。具体包含的内容如下：
- [x] 使用scalabel标注数据
- [x] 通过admlops完成自动化标注
- [x] 将数据转换为COCO格式
- [x] 使用yolopv2进行训练

## Annotation
使用scalabel标注数据

### 1. 准备数据 & 导入数据
> 为了方便描述，约定一些变量：
- 准备好的图像数据路径为`$HOME/example/imgs_00`
- scalabel工程的路径为`SCALABEL_PATH`

**生成img url list文件**
```bash
cd $SCALABEL_PATH/scripts && \
python3 url_generator.py --path $HOME/example/imgs_00 --suffix jpg 
```
此时生成的文件在本工程的local文件夹中，文件名为`imgs_00.json`


**修改docker-compose文件 & 启动scalabel**
将准备好的图像数据挂载至scalabel容器的`/opt/scalabel/local-data/items`目录下
```yml
volumes:
    - $HOME/example/imgs_00:/opt/scalabel/local-data/items/imgs_00
```

```bash
docker-compose up -d
```

此时可以通过`http://localhost:8686`访问scalabel

**自动标注**
> 通过admlops完成自动化标注

```bash
conda activate mmdet && \
cd $ADMLOPS_PATH && \
git checkout main && \
cd mmdetection_extension/tools/auto_annotation && \
python main.py \
--input $SCALABEL_PATH/local/imgs_00.json \
--type scalabel \
--config $ADMLOPS_PATH/mmdetection/configs/yolox/yolox_l_8x8_300e_coco.py \
--checkpoint $ADMLOPS_PATH/checkpoints/mmdet/yolox/yolox_l_8x8_300e_coco_20211126_140236-d3bd2b23.pth
```
此时在`$SCALABEL_PATH/local`目录下会生成`imgs_00_auto_annotation.json`文件，其中包含了自动标注的结果

### 2. 标注数据
因为已经获取了自动标注的结果，所以可以直接通过`http://localhost:8686`访问scalabel，然后导入`imgs_00_auto_annotation.json`文件，即可看到自动标注的结果

然后在这个基础上进行人工调整、标注，该标准的标注流程可以参考[scalabel标注流程](./labeling_guide.md)

最后导出标注结果，将导出的文件重命名为`imgs_00_bbox_export.json`. 将其移动至`$SCALABEL_PATH/local`目录下

### 3. 转换数据格式
> 通过scalabel的转换工具将数据转换为COCO格式

```bash
docker exec -it scalabel /bin/bash && \
cd /opt/scalabel && \
python3 -m scalabel.label.to_coco --input ./local-data/local/imgs_00_bbox_export.json \
--output ./local-data/local/imgs_00_bbox_export_coco.json && \
--mode det
```
