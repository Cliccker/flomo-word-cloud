# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Sandship
@file:main.py
@time:2021/08/12
@IDE:PyCharm
@blog:https://sandship.fun
"""

from utils import *


def main(font="华文中宋", min_word_length=3, img=None):
    """
    生成词云图片
    :param img: 背景图片，默认为无背景图片
    :param min_word_length: 词语的最短长度，默认为3
    :param font: 字体名称，默认为华文中宋
    """
    string = segment_corpus()
    cloud = make_wordcloud(font, min_word_length, string, img)
    save_img(cloud, min_word_length)


if __name__ == '__main__':
    main(font='毛笔体', img="pika.jpg")
