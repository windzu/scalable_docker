import os
import time
import cv2
import json


def frame_list_generator(path, suffix):
    """_summary_: frame_list
    格式为: ref:https://doc.scalabel.ai/format.html
    [
        {
            "name": "http://localhost:8686/items/imgs_00/0000.jpg",
            "url": "http://localhost:8686/items/imgs_00/0000.jpg",
            "videoName": "",
            "timestamp": 0,
            "intrinsics":{
                focal: [0, 0],
                center: [0, 0],
            },
            "extrinsics":{
                location: [0, 0, 0],
                rotation: [0, 0, 0],
            },
            "attributes":{},
            "size":{
                "width": 1920,
                "height": 1080
            }
            "labels":[] # 等待自动标注进行填充
            "sensor": -1,
        },
        ...
    ]

    Args:
        root_path (str): 图片根目录
        suffix (str): 图片后缀名
    """
    frame_list = []
    file_list = []
    basename = os.path.basename(path)
    suffix = suffix.split(" ")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.split(".")[-1] in suffix:
                frame = {}
                frame["url"] = "http://localhost:8686/items/" + os.path.join(basename, file)
                frame["name"] = "http://localhost:8686/items/" + os.path.join(basename, file)
                frame["videoName"] = ""
                frame["timestamp"] = 0
                frame["intrinsics"] = None
                frame["extrinsics"] = None
                frame["attributes"] = {}
                # get size
                img = cv2.imread(os.path.join(root, file))
                frame["size"] = {"width": img.shape[1], "height": img.shape[0]}
                frame["labels"] = []
                frame["sensor"] = -1
                frame_list.append(frame)

    return frame_list


def save_url_list(url_list, path):
    """_summary_: 保存url列表为json文件
    保存的json格式为:
    [
        {
        "url": "http://localhost:8686/items/example/0000.jpg",
        },
        ...
    ]

    Args:
        url_list (list): url列表
        path (str): 保存路径

    """
    import json

    # sort
    url_list.sort()
    url_list = [{"url": url} for url in url_list]
    with open(path, "w") as f:
        json.dump(url_list, f, indent=4)


def parse_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, default="./items/example", help="图片根目录")
    parser.add_argument("--suffix", "-s", type=str, default="jpg png", help="图片后缀名")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    frame_list = frame_list_generator(args.path, args.suffix)
    frame_list.sort(key=lambda x: x["name"])
    basename = os.path.basename(args.path)
    save_path = os.path.join("../local", basename + ".json")
    # save to json
    with open(save_path, "w") as f:
        json.dump(frame_list, f, indent=4)
    print("save to {}".format(save_path))
