# Auto Annotation

在scalabel的文档中，提到了自动化标注技术，但很可惜的是，官方并没有提供相关的模型支持

但是也有相关的支持. 在导入的item文件时，默认会将item文件中的`url`字段作为图片的路径，除此之外，还可以包含其他与标注内容相关的字段，例如`label`字段

```yaml
"labels": [
    {
        "id": 0,
        "category": "car",
        "attributes": {},
        "manualShape": true,
        "box2d": {
            "x1": 1623,
            "y1": 532,
            "x2": 1798,
            "y2": 615
        },
        "poly2d": null,
        "box3d": null
    },
    ...
]
```
这样scalabel在载入图像的时候，会同时读取标注的信息并展示，如果有不合适的标注，可以直接修改，如果没有标注，可以直接在图像上标注

基于此支持，可以通过一些高精度模型预先对数据进行检测，将检测结果转换为scalabel支持的格式，这样就可以直接在scalabel上进行标注的修改，而不需要重新标注

## ADMLOps拓展

ADMLOps是一个基于open-mmlab制作的针对自动驾驶的MLOps开源平台，其中集成了大量的模型，我在其中添加了一个小拓展，使其可以读取 scalabel 格式的item文件，并将检测结果转换为scalabel支持的标注格式，然后便完成了自动化标注的功能

具体的使用和实现方法请参考[ADMLOps Auto Annotation](待补充)