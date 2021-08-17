# flomo-word-cloud

从flomo导出的笔记中生成词云

## 如何使用？

+ 将本项目克隆到你的电脑上，使用如下的命令，安装所需python库

  ```python
  pip install -r requirements.txt
  ```

+ 在项目里新建一个`file`文件夹，把所有从flomo导出的html文件放入其中

+ 运行`main.py`

+ 打开`output`文件夹，欣赏你的flomo词云吧🤗

## 对结果不满意？

+ 如果你对某些词不满意：

  在`words/stopword.txt`里添加它们，或者在`words/dictionary.txt`里添加你认为没有分出来的词

  你也可以修改`main()`的参数，如`main(min_word_length=3)`来限制词语的最小长度

  

+ 如果你对字体不满意：

  修改`mian()`的参数，如`main(font="毛笔体")`

  目前我添加了三个字体，**华文中宋**（通用），**阿里普惠体**（免费），**毛笔体**（好看）

  在`fonts`文件夹下添加你喜欢的字体

  **注意：** svg图片显示需要字体支持，如果你使用了自定义字体，请先安装它！

  

+ 如果你对词云形状不满意：

  修改`mian()`的参数，如`main(img="pika.jpg")`

  在`back_ground`文件夹下添加你喜欢的背景图片
  
  **注意：** 使用背景为白色的图片效果会更好
  
  

