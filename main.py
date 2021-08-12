# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Sandship
@file:main.py
@time:2021/08/12
@IDE:PyCharm
@blog:https://sandship.fun
"""


from utils import generate_wordcloud_img
""" 生成词云图片
font : string (default="华文中宋")
    参数为空则默认选择华文中宋
"""
generate_wordcloud_img(font="毛笔体")

