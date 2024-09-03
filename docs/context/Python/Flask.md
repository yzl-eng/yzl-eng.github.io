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



## 路由

现代 web 应用都使用有意义的 URL ，这样有助于用户记忆，网页会更得到用户的青睐， 提高回头率。

使用 `route()` 装饰器来把函数绑定到 URL:

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

但是能做的不仅仅是这些！你可以动态变化 URL 的某些部分， 还可以为一个函数指定多个规则。



### 变量规则

通过把 URL 的一部分标记为 `<变量名>` 就可以在 URL 中**添加变量**。标记的部分会作为**关键字参数**传递给函数。

```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

```

> `escape` 函数来自于 `markupsafe` 库，它用于将输入中的特殊字符转换为 HTML 实体。这是为了防止跨站脚本攻击（XSS），确保用户输入的内容不会被解释为 HTML 代码，从而提高 Web 应用程序的安全性。

通过使用 `<转换器:变量名>` ，可以选择性的加上一个**转换器**，为变量指定规则。

| 类型     | 作用                                |
| -------- | ----------------------------------- |
| `string` | （缺省值） 接受任何不包含斜杠的文本 |
| `int`    | 接受正整数                          |
| `float`  | 接受正浮点数                        |
| `path`   | 类似 `string` ，但可以包含斜杠      |
| `uuid`   | 接受 UUID 字符串                    |

**示例：**

```python
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
```



### 唯一的 URL / 重定向行为

以下两条规则的不同之处在于是否使用尾部的斜杠:

```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

`projects` 的 URL 是中规中矩的，尾部有一个斜杠，看起来就如同一个文件夹。 访问一个**没有斜杠**结尾的 URL 时 Flask 会**自动**进行**重定向**，帮你在尾部**加上**一个斜杠。例如访问 `/projects` 会自动重定向到 `/projects/`

`about` 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个 URL 时添加了尾部斜杠（即 `/about/`）就会得到一个 404 错误。这样可以**保持 URL 唯一**，并帮助搜索引擎避免重复索引同一页面。



### URL 构建

`url_for()` 函数用于构建指定函数的 URL。它把函数名称作为第一个参数。它可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量。未知变量将添加到 URL 中作为查询参数。

为什么不在把 URL 写死在模板中，而要使用反转函数 `url_for()`动态构建？

1. 反转通常比硬编码 URL 的描述性更好。
2. 你可以只在一个地方改变 URL ，而不用到处乱找。
3. URL 创建会为你处理特殊字符的转义和 Unicode 数据，比较直观。
4. 生产的路径总是绝对路径，可以避免相对路径产生副作用。
5. 如果你的应用是放在 URL 根路径之外的地方（如在 `/myapplication` 中，不在 `/` 中）， `url_for()` 会为你妥善处理。

例如，这里我们使用 `test_request_context()` 方法来尝试使用 `url_for()` 。 `test_request_context()`告诉 Flask 正在处理一个请求，而实际上也许我们正处在交互 Python shell 之中， 并没有真正的请求。参见 [本地环境](https://flask.github.net.cn/quickstart.html#context-locals) 。

```python
from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```





参考资料：

[快速上手_Flask中文网 (github.net.cn)](https://flask.github.net.cn/quickstart.html#id14)

