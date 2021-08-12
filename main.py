# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Sandship
@file:main.py
@time:2021/08/11
@IDE:PyCharm
@blog:https://sandship.fun
"""
import os
import jieba as jb
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud


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
            if "#" not in item_string:  # 去除标签所在行，不过到底要不要去除应该待定
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
    corpus = build_corpus()
    with open("stopwords.txt", "r", encoding="utf-8") as stopwords_file:
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
    print('Segmenting corpus ...')
    return cloud


def makedir(path):
    """
    生成输出文件夹
    :param path: 文件夹名称
    """
    folder = os.path.exists(path)
    if folder:
        pass
    else:
        os.makedirs(path)


def generate_wordcloud_img(font):
    """
    生成词云图片
    :param font: 需要显示的字体名称
    """
    string = segment_corpus()
    print("Generating wordcloud ...")
    wordcloud = WordCloud(
        background_color='white',  # 背景颜色，根据图片背景设置，默认为黑色
        font_path="fonts/" + font + ".ttf",  # 若有中文需要设置才会显示中文
        width=1000,
        height=900,
        margin=2,
        max_words=300,
        min_word_length=2).generate(string)  # generate 可以对全部文本进行自动分词
    # 参数 width，height，margin分别对应宽度像素，长度像素，边缘空白处
    plt.imshow(wordcloud)
    plt.axis('off')
    makedir("output")
    print("Saving images ...")
    wordcloud.to_file("output/my_flomo_wordcloud.png")  # 保存PNG格式
    svg_string = wordcloud.to_svg()  # 保存SVG格式
    with open("output/my_flomo_wordcloud.svg", "w", encoding="utf-8") as svg_file:
        svg_file.write(svg_string)
        svg_file.close()
    print("Finished!")


if __name__ == '__main__':
    jb.initialize()
    generate_wordcloud_img(font='毛笔体')
