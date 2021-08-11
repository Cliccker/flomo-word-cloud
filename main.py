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
        para_list.append(item.string)
    return para_list


def build_corpus():
    """
    遍历file文件夹以建立corpus
    """
    corpus = []
    for root, dirs, names in os.walk("file"):
        for filename in names:
            corpus += read_html(os.path.join(root, filename))
    return corpus


def segment_corpus(corpus):
    """
    对语料库进行分词
    """
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
    return cloud


def generate_img(string):
    """
    生成词云图片
    :param string: 需要处理的文本
    """
    wordcloud = WordCloud(
        background_color='white',  # 背景颜色，根据图片背景设置，默认为黑色
        font_path='C:\Windows\Fonts\STZHONGS.TTF',  # 若有中文需要设置才会显示中文
        width=1000,
        height=900,
        margin=2).generate(string)  # generate 可以对全部文本进行自动分词
    # 参数 width，height，margin分别对应宽度像素，长度像素，边缘空白处

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

    # 保存图片：默认为此代码保存的路径
    wordcloud.to_file('my_flomo_wordcloud.png')


if __name__ == '__main__':
    corpus = build_corpus()
    cloud = segment_corpus(corpus)
    generate_img(cloud)
