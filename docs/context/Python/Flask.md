### WSGI

Web服务器网关接口(WSGI)已被采纳为Python Web应用程序开发的标准。 WSGI是Web服务器和Web应用程序之间通用接口的规范。

### WERKZEUG

它是一个WSGI工具包，它实现了请求，响应对象和其他实用程序功能。 这可以在其上构建Web框架。 Flask框架使用Werkzeug作为其一个基础模块之一。

### Jinja2

jinja2是Python的流行模板引擎。 网页模板系统将模板与特定的数据源结合起来呈现动态网页。

Flask通常被称为**微框架**。 它旨在保持应用程序的核心简单且可扩展。 Flask没有用于数据库处理的内置抽象层，也没有形成验证支持。 相反，Flask支持扩展以将这些功能添加到应用程序中。



### Conda安装

```shell
conda create -n Flaskenv python=3.9
activate Flaskenv
conda install pip
pip install Flask
```

安装报错，可能是代理问题，也可能未在管理员权限下使用



### virtualenv安装

virtualenv是一个虚拟的Python环境构建器。 它可以帮助用户并行创建多个Python环境。 因此，它可以避免不同版本的库之间的兼容性问题。

```shell
pip install virtualenv
```

该命令需要管理员权限。 在Linux/Mac OS上需要在`pip`之前添加sudo。 如果在Windows上，请以管理员身份登录。在Ubuntu上，virtualenv可以使用其包管理器进行安装。

```shell
sudo apt-get install virtualenv
```

安装完成后，新的虚拟环境将在文件夹中创建。

```shell
mkdir newproj
cd newproj
virtualenv venv
```

要激活相应的环境，请在Linux/OS X上使用以下命令 -

```shell
venv/bin/activate
```

在Windows上，可以使用以下命令 -

```shell
venv\scripts\activate
```

现在准备在这个环境中安装Flask。

```shell
 pip install Flask
```

[参考资料](https://www.yiibai.com/flask/flask_environment.html)



## 运行

```python
# hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def __name__ == '__main__':
    app.run()
```



运行

```shell
flask --app hello run
```

这样就启动了一个非常简单的**内建**的服务器。这个服务器用于测试应该是足够 了，但是用于生产可能是不够的。



打开调试模式

```shell
flask --app hello run --debug
```

开启后修改Python代码会自动重启
