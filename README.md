# flomo-word-cloud
从flomo导出的笔记中生成词云

由于最近flomo出了一个导出功能，想在导出的数据上创造一些有趣的玩法。故写了这个生成词云的脚本

## 如何使用？

+ 将本项目克隆到你的电脑上，使用如下的命令，安装所需python库；

  ```python
  pip install -r requirements.txt
  ```

+ 在项目里新建一个`file`文件夹，把所有从flomo导出的html放入`file`；

+ 运行`main.py`，`my_flomo_wordcloud.png`就是你想要的图片

## 对结果不满意？

如果你对结果里的某些词不太满意，在`stopword.txt`里添加它们，再运行`main.py`就可以啦

## 想要更有趣的形状？

或许你可以参考一下wordcloud的教程，创造出更多好看有趣的词云。

