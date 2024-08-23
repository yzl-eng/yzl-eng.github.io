## 简介

QT是众多GUI框架里面非常著名的一款，它本身由C++开发，天然支持基于C++的GUI编程，编出来的图形化软件在当今众多GUI框架中运行效率几乎是天花板级别的，拥有完善的第三方库，极其适合数字图像处理、文档排版、多媒体、3D建模等专业软件开发。与此同时，QT还有一个强大的功能：支持跨平台，简单来理解，就是我们只需要编写一套代码就可以同时在windows、mac、linux上运行。

值得一提的是，QT对Python也有完善API支持，意味着我们可以规避C++编程的苦恼，使用更简洁的Python来代替C++开发QT应用，同样具备跨平台等优势。需要说明的是，目前有两种QT对应的Python工具：PySide和PyQt。这里首先介绍下两者的区别。

PySide是Qt公司的产品，PyQt是第三方公司的产品，二者用法基本相同，不过在使用协议上却有很大差别。PySide可以在LGPL协议下使用，PyQt则在GPL协议下使用。这两个协议的区别就是如果使用PyQt，那么你开发的软件必须开源，否则就存在被告的风险。而PySide就没有这种约束，不管是开发商业闭源软件还是开源软件，你都可以不开源代码，开不开源是你的自由。从这一点上来看，对于商业公司或者说有商业考虑的软件来说，我更倾向于推荐PySide，更何况PySide还是QT的亲儿子。虽然PySide和PyQt在协议上有不同，但是两者提供的接口几乎是完全一致的。目前市面上PyQt的教程**完全适合**PySide，因此，对于学习者来说学习任何一个都是可以的。

PySide目前常见的有两个版本：PySide2和PySide6。PySide2由C++版的Qt5开发而来.，而PySide6对应的则是C++版的Qt6。从PySide6开始，PySide的命名也会与Qt的大版本号保持一致，不会再出现类似PySide2对应Qt5这种容易混淆的情况。

在使用层面上，PySide2和PySide6无过多的差异，只有一点需要注意，使用PySide6开发的程序在默认情况下不兼容Windows7系统，这也是Qt6所决定的（即使是C++的QT6也不支持Windows7）。


## 安装

```shell
pip install pyside6
```



基于PySide6开发GUI程序包含下面三个基本步骤：

- 设计GUI，图形化拖拽或手撸；
- 响应UI的操作（如点击按钮、输入数据、服务器更新），使用信号与Slot连接界面和业务；
- 打包发布；



使用QtWidget开发程序时，也有两种基本的使用方法，一种是通过designer开发界面，另一种是用代码手动开发界面。本文的目的是极简快速入门，所以使用designer这种方便的方式进行开发。

我们可以在CMD终端中使用下面的命令启动designer：

```shell
pyside6-designer
```

本体位置在`Lib\site-packages\PySide6`文件夹下，也可以手动点击designer.exe文件运行



## 配置

### Pycharm配置PySide6

打开Pycharm点击`File` -> `Settings` -> `Tools` -> `External Tools`，点击`＋`。需要添加 `Pyside6-Designer` 、 `Pyside6-UIC` 和 `Pyside6-rcc`三个选项。

#### 配置PySide6-Designer

- **designer.exe**是 PySide6 框架中的图形界面设计器工具，它允许您可视化地创建和编辑用户界面。开发者能够通过拖放、调整大小和设置属性等操作来创建复杂的 GUI 布局，而**无需手动编写代码**。

- `designer.exe`在**虚拟环境**所安装的文件夹下的`Lib\site-packages\PySide6`文件夹下,`D:\Anaconda\envs\Flaskenv\Lib\site-packages\PySide6\designer.exe`

<img src="https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202408072356264.png" alt="image-20240807235642215" style="zoom:67%;" />

#### 配置PySide6-uic

- `pyside6-uic.exe` 是 PySide6 框架中的一个命令行工具，用于将 Qt Designer 创建的 `.ui` 文件（用户界面文件）转换为 Python 代码。
- `pyside6-uic.exe`在虚拟环境所安装的文件夹下的`Scripts`文件夹下,`D:\Anaconda\envs\Flaskenv\Scripts\pyside6-uic.exe`

<img src="https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202408080035178.png" alt="image-20240808000235378" style="zoom:67%;" />

#### 配置PySide6-rcc

- `pyside6-rcc.exe `是 PySide6 框架中的一个命令行工具，用于将 Qt 资源文件（`.qrc` 文件）编译成 Python 代码文件。资源文件通常用于存储应用程序所需的非代码资源，如图像、样式表、音频文件等。通过将资源文件编译成 Python 代码，可以在 PySide6 应用程序中更方便地访问这些资源。
- `pyside6-rcc.exe`也在虚拟环境所安装的文件夹下的`Scripts`文件夹下,`D:\Anaconda\envs\Flaskenv\Scripts\pyside6-rcc.exe`

<img src="https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202408080035514.png" alt="image-20240808002259095" style="zoom:67%;" />

[参考资料](https://blog.csdn.net/qq_45062768/article/details/132357617)



### VSCode配置PySide6环境

在应用商店中搜索插件`PYQT Integration`，点击安装即可。

打开插件设置

按上面Pycharm用到的地址填入插件设置的相应位置

#### 配置PySide6-Designer

<img src="https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202408081846794.png" alt="image-20240808184613752" style="zoom:50%;" />

#### 配置PySide6-rcc

<img src="https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202408081845483.png" alt="image-20240808184516358" style="zoom: 50%;" />

#### 配置PySide6-uic

<img src="https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202408081845982.png" alt="image-20240808184538933" style="zoom:50%;" />



## 使用

注意，PySide6是不能直接使用`.ui`文件的，我们还需要将其转为`.py`文件。首先cd到hello文件夹中，然后使用命令：

```bash
pyside6-uic hello.ui > ui.py
```



### 基础代码示例

```python
# hello.py
from PySide6.QtWidgets import QMainWindow,QApplication

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__=='__main__':
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()
```



官方示例

```python
# app.py
from PySide6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.
```


运行，QT会自动创建一个带有普通窗口装饰的窗口，你可以将其拖动并像任何窗口一样大小。

```shell
python app.py
```



应用程序处理程序和`QWidget`，一个基础的空白GUI小部件，都来自`QtWidgets`模块
> from PySide6.QtWidgets import QApplication, QWidget





### 打包部署

我们最终希望交给用户是一个纯粹的exe可执行文件（可以包含一些dll之类的动态库或配置文件），用户不需要安装Python依赖，直接双击就可以运行展示。下面我们来实现最后的这个环节。

下面主要以windows为例。

首选安装打包工具：

```shell
pip install pyinstaller 
pip install auto-py-to-exe
```



输入`auto-py-to-exe`运行

<img src="https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202408072344665.png" alt="image-20240807234401558" style="zoom: 50%;" />

[参考资料](https://blog.csdn.net/qianbin3200896/article/details/126947934)

## 

通过PySide6和QT designer设计一个计算器

在QT designer中设计好UI

<img src="D:/Typora_img/image-20240823110119583.png" alt="image-20240823110119583" style="zoom: 67%;" />

生成对应UI文件，将对应`.ui`文件通过**PySide_UIC**转成`.py`文件

在主程序中导入该文件

**程序示例**

```python
# main.py

import sys

from PySide6.QtWidgets import QApplication, QWidget,  QPushButton

#导入UI文件
from calculator import Ui_Form


class Calculator(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 循环绑定数字和基本操作按钮
        for btn in self.findChildren(QPushButton):
            btn: QPushButton
            if btn.objectName().startswith('num') or btn.objectName().startswith('opr'):
                btn.clicked.connect(self.on_num_click)

        # 清空按钮获取与绑定
        self.clear_btn.clicked.connect(self.on_clear_click)
        # 输出按钮获取与绑定
        self.equal_btn.clicked.connect(self.on_equal_click)
    
    # 点击将按钮内容放入Qlabel并显示
    def on_num_click(self):
        number = self.sender().text()
        self.eval_box.setText(self.eval_box.text() + number)

    # 点击清空
    def on_clear_click(self):
        self.result_label.clear()
        self.eval_box.clear()

    # 点击输出结果
    def on_equal_click(self):
        try:
            result = eval(self.eval_box.text())
            self.eval_box.clear()
            self.result_label.setText(str(result))
        except:
            self.eval_box.setText('')
            self.result_label.setText("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    # 显示窗体
    window.show()
    app.exec()
```



















