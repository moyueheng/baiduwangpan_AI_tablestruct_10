# 代码示例
# python predict.py [src_image_dir] [results]

import os
import sys
import glob
import json
import cv2
import paddle
import numpy as np


def process(src_image_dir, save_dir):
    model = paddle.jit.load("./mymodel/ext_myPPYoloeVoc_l_100e/model")
    model.eval()

    label_list = ["table", "row", "column", "spanning_cell"]

    image_paths = glob.glob(os.path.join(src_image_dir, "*.jpg"))
    result = {}
    for image_path in image_paths:
        filename = os.path.split(image_path)[1]
        # do something
        img = cv2.imread(image_path)

        input_size = (640, 640)
        scale_factor = [input_size[0] / img.shape[0], input_size[1] / img.shape[1]]
        factor = np.array(scale_factor, dtype=np.float32)
        factor = paddle.to_tensor(factor).reshape((1, 2)).astype("float32")

        img = cv2.resize(img, input_size)
        img = img / 255
        img = (img - np.array([0.0, 0.0, 0.0])) / np.array([1.0, 1.0, 1.0])
        img = img.transpose([2, 0, 1])
        img = paddle.to_tensor(img).astype("float32")
        img = paddle.reshape(img, [1] + img.shape)

        pre = model(img, factor)

        if filename not in result:
            result[filename] = []

        for item in pre[0].numpy():
            label_index, value, xmin, ymin, xmax, ymax = item
            label_index, xmin, ymin, xmax, ymax = [
                int(x) for x in [label_index, xmin, ymin, xmax, ymax]
            ]
            label = label_list[label_index]
            if value > 0.53:
                result[filename].append(
                    {"box": [xmin, ymin, xmax, ymax], "label": label}
                )

    with open(os.path.join(save_dir, "result.txt"), "w", encoding="utf-8") as f:
        f.write(json.dumps(result))


if __name__ == "__main__":
    assert len(sys.argv) == 3

    src_image_dir = sys.argv[1]
    save_dir = sys.argv[2]

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    process(src_image_dir, save_dir)
