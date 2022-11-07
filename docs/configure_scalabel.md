# Configure Scalabel

经过简单的使用，我发现scalabel是一个可以为标注对象添加属性的工具，其需要正确的配置即可使用，下面是个人的一些配置和理解。

## Config 

Scalabel支持标注多种数据类型(标注类型)以及多种标注方式

数据类型包括(标注类型)
- Image : 对图像进行标注
- Video Tracking : 对图像进行标注tracking标注
- Point Cloud : 对点云进行标注
- Point Cloud Tracking : 对点云进行标注tracking标注

Label类型包括
- Tagging
- Bounding Box
- Polygon
- Polyline
- 3D Bounding Box

与LabelImg等标注工具不同，Scalabel提供了很高的自由度来辅助高效的标注数据，这些功能需要通过配置文件来启用，需要配置的内容主要包括
- 待标注数据的文件列表
- label的类别信息
- label的属性信息


> **Note** 
>
> 以下所有配置文件的示例修改自[官方示例](https://github.com/scalabel/scalabel/tree/master/examples)，已与bdd100k保持一致

### Item 配置

与一般标注软件不同，scalable不是通过选择文件夹的方式来载入数据，而是通过导入一个配置文件，其内容是所有待标注文件的url路径列表,支持json或yaml格式，格式可参考本工程下item目录中的文件
- image_list.json : 图片文件url列表的json格式
- image_list.yml : 图片文件url列表的yaml格式
- point_cloud_list.yml : 点云文件url列表的yaml格式

下面以image_list.yml文件中部分内容为例做详细说明
```yaml
- {url: 'https://s3-us-west-2.amazonaws.com/scalabel-public/demo/frames/intersection-0000099.jpg', videoName: 'a'}
- {url: 'https://s3-us-west-2.amazonaws.com/scalabel-public/demo/frames/intersection-0000101.jpg'}
```
- 每一个文件在yaml文件中以列表形式表示，其中必须包含 url key
- 可在url字段外添加其他的描述属性，如上述例子中的 videoName


### Category 配置

该配置用于设置待标注数据的类别，在进行标注时只能从设置的类别中进行选择，需为yaml格式，格式可参考本工程下 category 目录中的系列文件
- categories.yml : 预设的bbox类别信息，与bdd100k相同
- drivable_area_categories.yml : 预设的可通行区域(Polygon)的类别信息，与bdd100k相同
- lane_categories.yml : 预设的车道线(Polyline)类别信息，与bdd100k相同
- two_level_categories.yml : 全景分割相关，略
- three_level_categories.yml : 全景分割相关，略
- tree_structured_categories.yml : 全景分割相关，略

下面以lane_categories.yml文件中内容为例做详细说明
```yaml
- name: crosswalk  # 人行道
- name: double other # 双其他
- name: double white # 双白线
- name: double yellow # 双黄线
- name: road curb # 路缘 
- name: single other # 单其他 
- name: single white # 单白线
- name: single yellow # 单黄线
- name: background # 背景
```

### Attribute 配置

该配置用于设置待标注数据的属性，例如在标注bbox时常见的`Occluded`属性，通过配置文件可以将其配置为 `switch` 或 `list` 按钮显示在标注面板上，格式可参考本工程下 attribute 目录中的系列文件
- object_detection_categories.yml : bbox属性
- lane_attributes.yml ： 车道线相关属性
- segmentation_attributes.yml ： 分割相关属性

下面以 object_detection_categories.yml文件中内容为例做详细说明
```yaml
-
  name: occluded # 属性名为 occluded
  type: switch # 在dashboard中的显示方式为 switch , 所以属性类型为 bool
  tag: o # 属性名缩写 在标注时，label中附加显示的内容 (与标注结果无关，仅用于标注时显示)
-
  name: truncated # 属性名为 truncated
  type: switch # 在dashboard中的显示方式为 switch , 所以属性类型为 bool
  tag: t # 属性名缩写 在标注时，label中附加显示的内容 (与标注结果无关，仅用于标注时显示)
-
  name: trafficLightColor # 属性名为 trafficLightColor
  type: list # 在dashboard中的显示方式为 list , 所以属性类型为 string
  values: # 属性值列表
    - red
    - green
    - yellow
    - none
  tagPrefix: "" # 分别对应的前缀，在标注时，label中附加显示的内容
  tagSuffixes: # 分别对应的后缀，在标注时，label中附加显示的内容
    - r
    - g
    - y
    - n
  tag: t
```
