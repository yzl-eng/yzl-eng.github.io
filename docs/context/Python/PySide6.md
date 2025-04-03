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







## 信号与槽（Signals & Slots）

信号与槽是Qt中的一种事件处理机制；

**信号（Signals）**是当某些事情发生时由**小部件（widgets**）发出的通知。这些"某些事情"可以是任何事情，比如按下一个按钮、输入框中的文本变化，或者窗口中的文本变化，窗口大小被调整时也能产生一个信号。

信号还可以**发送数据**来提供有关发生事件的额外背景信息。简单来说，信号不仅仅是用来告知某件事情已经发生，它们还可以携带额外的信息来帮助接收者更好地理解这个事件的细节或原因。

**槽（Slots）**是用来**接收信号**的组件。在Python中，应用程序中的任何**函数**或**方法**都可以用作**槽**——只需将信号连接到它即可。如果信号发送数据，那么接收函数也会接收到这些数据。许多Qt控件也有自己内置的槽，这意味着你可以直接将Qt控件相互连接起来。

可以将**PySide6** 的 **信号和槽** 机制简单地理解为一种 订阅机制。

- 信号充当了 **发布者**（**publisher**）的角色，负责发布消息；
- 槽扮演了 **订阅者**（**subscriber**）的角色，用于接收消息并作出响应。
- 槽可以订阅一个或多个信号，当信号发生时，槽会自动被调用执行。



### 信号

**信号**是一种特殊函数，可以在特定的情况下被`QObject` 对象发射（`emit`）

在**PySide6**中，可以使用 `Signal()` 来定义信号

下面代码定义了一个名为 `my_signal` 的信号，它接受一个整形参数（可以为空，也可以更换为其它类型)

```python
from PySide6.QtCore import (QThread, Signal)

class MyThread(QThread):
    my_signal = Signal(int)
```



### 槽 Slot

在**PySide6**中，可以使用` @Slot()`装饰器 来定义**槽**

**槽**是普通的函数，它可以被信号调用。当一个信号被发射时，与之相连接的槽将被调用，并将信号的参数传递给槽。

下面定义了一个名为 `my_slot` 的槽，它接受一个字符串参数，并打印接收到的数据

```python
from PySide6.QtCore import (QThread, Slot)


class MyThread(QThread):
    @Slot(int)
	def my_slot(self, data):
    	print("Received data: ", data)
```


**值得注意是：**

这里的` @Slot(int)` 可以不写，但是写了可以提高代码**可读性**和**执行效率**。



**所以还是推荐使用`@Slot()`装饰器**

- `@Slot `装饰器可以更好地管理对象的生命周期，特别是在使用` deleteLater `时
- 使用 `@Slot` 装饰器可以明确地标识哪些函数是槽函数，提高代码的可读性和可维护性
- 使用 `@Slot `装饰器可以提供更详细的调试信息，帮助开发者更好地调试和理解信号和槽的连接情况



`@Slot `装饰器非常灵活，可以根据需要指定多种参数类型，确保信号和槽之间的连接是类型安全的

一个槽函数可以支持一个参数的多种类型，通过使用多个` @Slot `装饰器：

```python
@Slot(str)
@Slot(int)
def on_multiple_signal_types(self, value=None):
    if isinstance(value, str):
        self.label.setText(f"Received string: {value}")
    elif isinstance(value, int):
        self.label.setText(f"Received integer: {value}")
    else:
        self.label.setText("No value received")
```

`@Slot `装饰器还可以指定多个参数的类型，并且可以使用默认参数：

```python
@Slot(int, str, bool)
def on_multiple_parameters(self, number, message, flag):
    self.label.setText(f"Number: {number}, Message: {message}, Flag: {flag}")

@Slot(int, str, bool)
def on_multiple_parameters_with_defaults(self, number=0, message="Default", flag=False):
    self.label.setText(f"Number: {number}, Message: {message}, Flag: {flag}")
```



**信号**和**槽**只能在 `QObject`的子类里使用


然而，在`PySide6` 中，大部分常用的类都是继承了`QObject`类的，所以这个问题倒无需担心，只需知道有这一概念即可。

信号和槽必须是**相同**的**参数类型**。在定义信号和槽时，必须确保它们的参数类型和个数是相同的，否则无法正确连接和触发信号和槽。



### 连接信号和槽

在 **PySide6** 中，可以使用` connect()` 方法将信号和槽相连接，如下所示：

- 下面代码将`sender`对象的`my_signal`信号与`receiver`对象的`my_slot`槽相连接
- 当`sender`对象发射`my_signal`信号时，`receiver`对象的`my_slot`槽将被调用

```python
sender = MyThread()
receiver = MyThread()

sender.my_signal.connect(receiver)
```




其实就是 使用` connect `将两者连接起来；

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
```



接受数据

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)
```



存储数据

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print(self.button_is_checked)
```



[参考资料](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/)

[参考资料2](https://frica.blog.csdn.net/article/details/130432353)





## PySide6网络

`QNetworkAccessManager` 的基本功能

- 发送 HTTP/HTTPS 请求（GET、POST、PUT、DELETE 等）。
- 支持异步请求，防止阻塞主线程（特别适用于 GUI 程序）。
- 处理多种类型的网络协议（HTTP、HTTPS、FTP 等）。
- 提供回调机制，通过信号处理响应。
- 支持 SSL/TLS 等安全协议。

2. **常用方法**

- **`get(QNetworkRequest)`**：发送 GET 请求。
- **`post(QNetworkRequest, data)`**：发送 POST 请求。
- **`put(QNetworkRequest, data)`**：发送 PUT 请求。
- **`deleteResource(QNetworkRequest)`**：发送 DELETE 请求。

3. **`QNetworkRequest` 与 `QNetworkReply`**

- **`QNetworkRequest`**：用于指定网络请求的 URL 和其他参数，如 HTTP 头、请求超时等。
- **`QNetworkReply`**：用于接收请求的响应，它包含了响应的数据和状态码。

4. **信号与槽机制**

`QNetworkAccessManager` 是异步工作的，因此使用信号与槽来处理响应。常用信号包括：

- **`finished(QNetworkReply \*)`**：当网络请求完成时发出信号。
- **`error(QNetworkReply::NetworkError)`**：网络请求失败时发出信号。



携带Token

```python
# 设置目标 URL
url = QUrl("https://jsonplaceholder.typicode.com/posts")
request = QNetworkRequest(url)

# 添加 JWT Token 到 Authorization 头
jwt_token = "your_jwt_token_here"  # 将其替换为实际的 JWT Token
authorization_header = f"Bearer {jwt_token}"
request.setRawHeader(b"Authorization", QByteArray(authorization_header.encode('utf-8')))

# 发送 GET 请求
self.manager.get(request)
```



### 使用步骤

**创建 `QNetworkAccessManager` 实例**

`QNetworkAccessManager` 管理所有的网络请求和响应。通常，应该将它作为一个对象成员来管理其生命周期。

```python
class NetworkClient(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QNetworkAccessManager Example")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Waiting for server response...", self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Initialize QNetworkAccessManager
        self.manager = QNetworkAccessManager(self)
        self.manager.finished.connect(self.handle_response)

        # Start network request
        self.start_request()
```

**发送请求**

创建 `QNetworkRequest` 对象并设置 URL。然后使用 `QNetworkAccessManager` 的 `get()`, `post()`, `put()`, `delete()` 方法发送请求。

```python
def start_request(self):
    url = QUrl("https://api.example.com/data")  # 替换为实际的 URL
    request = QNetworkRequest(url)
    self.manager.get(request)  # 发送 GET 请求
```

**处理响应**

`QNetworkAccessManager` 的 `finished` 信号在请求完成时发射，处理响应通常在这个信号的槽中进行。

```python
@Slot(QNetworkReply)
def handle_response(self, reply: QNetworkReply):
    if reply.error() == QNetworkReply.NoError:
        # 读取响应数据
        response_data = reply.readAll().data().decode()
        self.label.setText("Response: " + response_data)
    else:
        # 处理错误
        self.label.setText(f"Error: {reply.errorString()}")
    reply.deleteLater()  # 释放资源
```



`QTimer` 是 Qt 框架提供的一个定时器对象，它可以在后台线程中运行。
当定时器超时触发 `self.fetch_data` 时，这个方法会在事件循环中被调度执行，而不会直接影响主线程的任务执行。

事件循环（Event Loop）是一种编程模式，主要用于处理异步事件和用户交互。具体来说：
监听事件：事件循环不断监听来自外部的各种事件（如用户输入、定时器超时等）。
调度事件：当检测到事件时，事件循环将相应的事件放入事件队列。
处理事件：事件循环从队列中取出事件，并调用对应的处理函数（如槽函数）。
在 Qt 框架中，事件循环通过 `QApplication` 的` exec_() `函数启动，确保应用程序能够响应各种事件而不阻塞主线程