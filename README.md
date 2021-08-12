# flomo-word-cloud

从flomo导出的笔记中生成词云

## 如何使用？

+ 将本项目克隆到你的电脑上，使用如下的命令，安装所需python库；

  ```python
  pip install -r requirements.txt
  ```

+ 在项目里新建一个`file`文件夹，把所有从flomo导出的html文件放入其中；

+ 运行`main.py`

+ 打开`output`文件夹，欣赏你的flomo词云吧🤗

## 对结果不满意？

+ 如果你对某些词不满意：

  在`stopword.txt`里添加它们，再运行`main.py`就可以啦。

  

+ 如果你对字体不满意：

  在`main.py`中修改`generate_wordcloud_img()`的参数，如`generate_wordcloud_img(font="毛笔体")`

  目前我添加了三个字体，**华文中宋**（通用），**阿里普惠体**（免费），**毛笔体**（好看）

  当然你也可以添加自己喜欢的字体，只需要将它拷贝到`fonts`文件夹下就可以了~

  **注意：**svg图片的显示需要字体支持，如果你使用了第三方字体，请先安装它！

  

+ 如果你对词云形状不满意：

  或许可以试着自己学习python库wordcloud的用法，自定义形状。

  当然，我还是会更新这个feature的，就是不知道啥时候更😋

