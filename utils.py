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
                print(item_string)
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


