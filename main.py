# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Sandship
@file:main.py
@time:2021/08/12
@IDE:PyCharm
@blog:https://sandship.fun
"""

from utils import segment_corpus, makedir
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def generate_wordcloud_img(font="华文中宋", min_word_length=3):
    """
    生成词云图片
    :param min_word_length: 词语的最短长度，默认为3
    :param font: 字体名称，默认为华文中宋
    """
    string = segment_corpus()
    print("Generating wordcloud ...")
    cloud = WordCloud(
        background_color='white',  # 背景颜色，根据图片背景设置，默认为黑色
        font_path="fonts/" + font + ".ttf",  # 若有中文需要设置才会显示中文
        width=1000,
        height=900,
        margin=2,
        max_words=300,
        min_word_length=min_word_length).generate(string)  # generate 可以对全部文本进行自动分词
    # 参数 width，height，margin分别对应宽度像素，长度像素，边缘空白处
    plt.imshow(cloud)
    plt.axis('off')
    makedir("output")
    print("Saving images ...")
    # 保存PNG格式
    cloud.to_file("output/my_flomo_wordcloud_" + str(min_word_length) + ".png")
    # 保存SVG格式
    svg_string = cloud.to_svg()
    with open("output/my_flomo_wordcloud_" + str(min_word_length) + ".svg", "w", encoding="utf-8") as svg_file:
        svg_file.write(svg_string)
        svg_file.close()
    print("Finished!")


if __name__ == '__main__':
    generate_wordcloud_img(font='毛笔体')
