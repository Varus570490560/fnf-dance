import math
import os

from PIL import Image
import config

config = config.Config()


def generate_picture(sub_picture_x: int, sub_picture_y: int, column: int):
    picture_path_lst = list()

    for root, dirs, files in os.walk(config.input_dir):
        for picture in files:
            picture_path_lst.append(config.input_dir + '/' + picture)
    line: int = math.ceil(len(picture_path_lst) / column)
    res_width: int = sub_picture_x * column
    res_height: int = sub_picture_y * line
    res = Image.new(size=(res_width, res_height), mode='RGBA')
    count: int = 0
    for i in range(0, line):
        for j in range(0, column):
            if count >= len(picture_path_lst):
                break
            x: int = j * sub_picture_x
            y: int = i * sub_picture_y
            img = Image.open(picture_path_lst[count])
            count = count + 1
            res.paste(img, (x, y))
    res.save(config.output_dir+'/'+"a.png")


def generate_xml():
    pass
