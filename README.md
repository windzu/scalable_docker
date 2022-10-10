# Scalabel使用说明

- [官方文档](https://doc.scalabel.ai/setup.html)

## Installation
> 本说明仅提供docker安装方法

1. 拉取镜像

```bash
docker pull scalabel/www
```

2. 创建容器 & 启动服务
```bash
docker-compose up -d
```

访问[http://localhost:8686/](http://localhost:8686/create)


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

此外Scalabel还提供了很高的标注自由度和快捷标注方式，启用这些功能需要进行正确的配置，下面详细介绍如何进行配置，**这也是官方文档中漏掉的部分**

### 数据源配置

scalabel支持多种数据源，包含
- redis
- s3
- local file

使用不同的数据源需要使用不同的配置文件，配置文件可以参考[官方config](https://github.com/scalabel/scalabel/tree/master/app/config)

> 在本目录下提供了一个默认的 local_config.yml 文件，其内容与官方config中的default.yml一致，属于本地读取方式

如果需要替换此种方式，在 docker-compose.yml 文件中修改 config file的配置即可

### Item & Category & Attribute 配置

> 以下所有配置文件的示例均可在[官方示例](https://github.com/scalabel/scalabel/tree/master/examples)中找到

与LabelImg等标注工具不同，Scalabel提供了很高的自由度来辅助高效的标注数据，这些功能需要通过配置文件来启用，需要配置的内容主要包括
- 待标注数据的文件列表
- label的类别信息
- label的属性信息

这些配置文件的提供，官方支持两种方式，一种是配置文件单独提供，一种是将所有配置写在一起，下面介绍**配置文件单独提供方式**(这样更灵活)

**Item 配置**

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


**Category 配置**

该配置用于设置待标注数据的类别，在进行标注时只能从设置的类别中进行选择，需为yaml格式，格式可参考本工程下 category 目录中的系列文件
- categories.yml : 预设的bbox类别信息，与bdd100k相同
- drivable_area_categories.yml : 预设的可通行区域(Polygon)的类别信息，与bdd100k相同
- lane_categories.yml : 预设的车道线(Polyline)类别信息，与bdd100k相同
- two_level_categories.yml : 全景分割相关，略
- three_level_categories.yml : 全景分割相关，略
- tree_structured_categories.yml : 全景分割相关，略

下面以lane_categories.yml文件中内容为例做详细说明
```yaml
- name: road curb # 道路边界线
- name: white # 白线
- name: yellow # 黄线
- name: other # other
- name: crosswalk # 人行道
```

**Attribute 配置**

该配置用于设置待标注数据的属性，例如在标注bbox时常见的Occluded属性，通过配置文件可以将其配置为 switch 或 list 按钮显示在标注面板上，格式可参考本工程下 attribute 目录中的系列文件
- bbox_attributes.yml : bbox属性
- lane_attributes.yml ： 车道线相关属性
- segmentation_attributes.yml ： 分割相关属性

下面以bbox_attributes.yml文件中内容为例做详细说明
```yaml
-
  name: Occluded # 属性名为 Occluded
  type: switch # 在dashboard中的显示方式为 switch , 所以属性类型为 bool
  tag: o # 在标注时，label中附加显示的内容 (与标注结果无关，仅用于标注时显示)
-
  name: Truncated # 属性名为 Occluded
  type: switch # 在dashboard中的显示方式为 switch  , 所以属性类型为 bool
  tag: t
-
  name: Traffic Light Color # 属性名为 Traffic Light Color
  type: list # 在dashboard中的显示方式为 list 
  values: # 以下是可选择的值
    - NA # none
    - G # green
    - Y # yellow
    - R # red
  tagPrefix: "" # 分别对应的前缀，在标注时，label中附加显示的内容
  tagSuffixes: # 分别对应的后缀，在标注时，label中附加显示的内容
    - ""
    - g
    - y
    - r
  tag: t
```
