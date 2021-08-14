# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Sandship
@file:utils.py
@time:2021/08/11
@IDE:PyCharm
@blog:https://sandship.fun
"""
import os

import jieba as jb

from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

def read_html(html_path):
    """
    解析HTML文件
    :param html_path: html文件的路径
    """
    soup = BeautifulSoup(open(html_path, encoding="utf-8"), features='html.parser')
    para = soup.find_all("p")  # 获取所有的段落
    para_list = []
    for item in para:
        item_string = item.string
        try:
            if "#" not in item_string and "https" not in item_string:  # 去除标签和网址所在行
                para_list.append(item_string)
        except TypeError:
            continue
    return para_list


def build_corpus():
    """
    遍历file文件夹以建立corpus
    """
    corpus = []
    for root, dirs, names in os.walk("file"):
        for filename in names:
            print("Parsing {} ...".format(filename))
            corpus += read_html(os.path.join(root, filename))
    print("Building corpus ...")
    return corpus


def segment_corpus():
    """
    对语料库进行分词
    """
    jb.load_userdict("words/dictionary.txt")  # 加载jieba的自定义词库
    corpus = build_corpus()
    with open("words/stopwords.txt", "r", encoding="utf-8") as stopwords_file:
        stopwords = stopwords_file.read().splitlines()
    cloud = ""
    for item in corpus:
        try:
            words = jb.lcut(item)
            for word in words:
                if word not in stopwords:
                    cloud += " " + word
        except AttributeError:
            pass
    # # 保存语料库为txt文件
    # with open("words/corpus.txt", "w", encoding="utf-8") as corpus_txt:
    #     corpus_txt.write(cloud)
    #     corpus_txt.close()
    print('Segmenting corpus ...')
    return cloud


def make_dir(path):
    """
    生成输出文件夹
    :param path: 文件夹名称
    """
    folder = os.path.exists(path)
    if folder:
        pass
    else:
        os.makedirs(path)


def pick_background(img):
    """
    选择背景图片，没有选则返回无
    :param img: 背景图片
    """
    if img is None:
        return None
    else:
        image = plt.imread("back_ground/"+img)
        image = image.astype(np.uint8)
        return image


def make_wordcloud(font, min_word_length, string, img):
    """
    生成词云
    :param img: 背景图片
    :param string: 语料
    :param font: 字体
    :param min_word_length: 最小长度
    :return:
    """
    print("Generating wordcloud ...")
    background = pick_background(img)
    cloud = WordCloud(
        background_color='white',  # 背景颜色，根据图片背景设置，默认为黑色
        font_path="fonts/" + font + ".ttf",  # 若有中文需要设置才会显示中文
        width=1000,
        mask=background,
        height=900,
        margin=2,
        max_words=300,
        min_word_length=min_word_length).generate(string)  # generate 可以对全部文本进行自动分词
    # 参数 width，height，margin分别对应宽度像素，长度像素，边缘空白处
    return cloud


def save_img(cloud, min_word_length):
    """
    保存图片
    :param cloud: 词云
    :param min_word_length: 最短词的长度，用来做区分
    """
    plt.imshow(cloud)
    plt.axis('off')
    make_dir("output")
    print("Saving images ...")
    # 保存PNG格式
    cloud.to_file("output/my_flomo_wordcloud_" + str(min_word_length) + ".png")
    # 保存SVG格式
    svg_string = cloud.to_svg()
    with open("output/my_flomo_wordcloud_" + str(min_word_length) + ".svg", "w", encoding="utf-8") as svg_file:
        svg_file.write(svg_string)
        svg_file.close()
    print("Finished!")
