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

| 转换器名 | 作用                                |
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



**`string`与`path`的区别：**

```python
@app.route('/user/<string:username>')
def show_user(username):
    return f'User: {username}'
```

如果你可以访问 `/user/jack`。但是，访问 `/user/jack/smith` 会返回 404 错误，因为 `string` 类型不匹配包含 `/` 的字符串。

```python
@app.route('/files/<path:filepath>')
def show_file(filepath):
    return f'File Path: {filepath}'
```

如果你访问 `/files/documents/work/file.txt`，`filepath` 会是 `'documents/work/file.txt'`。





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



## 蓝图

是一种用于组织代码和实现模块化应用的工具，尤其适合构建大型应用程序。

蓝图可以理解为一组**相关的**路由、视图、模板和静态文件的集合。它使你能够将应用程序拆分为多个部分，并可以独立开发和测试这些部分，最终再将它们注册到主应用程序中。

- 蓝图是 Flask 的扩展工具，用于创建可重用或模块化的应用结构。
- 它允许你将功能（如路由、模板、静态文件等）封装到独立的模块中，而不必把所有代码都放在一个单独的应用文件中。
- 蓝图并不直接运行，它们必须注册到 Flask 应用程序中。

类似于`Java`中的`Spring MVC Controllers`

### 蓝图使用

#### 1. 创建蓝图

蓝图的核心类是 `flask.Blueprint`。你首先需要实例化蓝图，然后定义路由、视图等。

例如，我们可以为用户管理功能创建一个蓝图：

```python
# users.py

from flask import Blueprint

# 创建蓝图实例
user_bp = Blueprint('user', __name__, url_prefix='/user')

# 定义路由
@user_bp.route('/<username>')
def show_user(username):
    return f'User: {username}'
```

这里，`user_bp` 是一个蓝图实例，`url_prefix='/user'` 指定了所有与用户相关的路由都会以 `/user` 开头。

#### 2. 注册蓝图到应用程序

在 Flask 应用主文件中，你需要使用`register_blueprint`注册蓝图到应用中：

```python
# app.py

from flask import Flask
from users import user_bp  # 导入用户蓝图

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
```

这样，你的应用现在可以访问 `/user/<username>` 这样的 URL 路径。

#### 3. 使用多个蓝图

假设你还需要一个管理后台模块，可以这样做：

```python
# admin.py

from flask import Blueprint

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def admin_home():
    return 'Admin Home Page'
```

然后在主文件中注册：

```python
# app.py

from flask import Flask
from users import user_bp
from admin import admin_bp

app = Flask(__name__)

# 注册用户和管理后台蓝图
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run(debug=True)
```

现在你的应用支持访问：

- `/user/<username>`：用户路由
- `/admin/`：管理后台路由

### 蓝图的优势

1. **组织代码**：通过蓝图，你可以将应用中的不同功能模块化，便于维护和扩展。
2. **独立开发**：每个蓝图可以独立定义自己的路由、视图函数、静态文件和模板。多个开发者可以并行开发不同的功能模块。
3. **灵活性**：蓝图可以通过不同的 `url_prefix` 轻松管理不同的 URL 路径，并且能够复用。

### 蓝图扩展功能

- **URL 前缀（`url_prefix`）**：为某一蓝图内的所有路由设置共同的 URL 前缀。
- **静态文件（`static_folder`）**：每个蓝图都可以有自己独立的静态文件目录。
- **模板（`template_folder`）**：蓝图可以拥有自己的模板文件夹，便于模块化管理不同的功能界面。







参考资料：

[快速上手_Flask中文网 (github.net.cn)](https://flask.github.net.cn/quickstart.html#id14)



# 数据库操作

## MongoDB

`pymongo`库

### 投影操作

在 MongoDB 中，投影是指指定查询结果中需要返回的字段。投影操作帮助你控制返回的文档中包含哪些字段，从而提高查询效率和减少传输的数据量。下面是投影操作的详解：

#### 1. 基本语法

在 PyMongo 中，你可以通过 `find()` 方法的第二个参数来指定投影：

```python
collection.find(query, projection)
```

- **query**: 查询条件
- **projection**: 投影字段的指定

#### 2. 选择特定字段

要选择返回的字段，可以在投影中将字段名设为 `1`，将不需要返回的字段设为 `0`。例如：

```python
# 只返回 name 和 age 字段，_id 字段会自动返回
result = collection.find({}, {"name": 1, "age": 1})
```

#### 3. 排除特定字段

如果你想排除某些字段而返回所有其他字段，可以将这些字段的值设为 `0`：

```python
# 排除 _id 字段，返回所有其他字段
result = collection.find({}, {"_id": 0})
```

#### 4. 结合选择和排除字段

你不能同时选择和排除字段，但可以选择一个字段并排除 `_id` 字段：

```python
# 只返回 name 字段，排除 _id 字段
result = collection.find({}, {"name": 1, "_id": 0})
```

#### 5. 嵌套字段的投影

对于嵌套文档，你可以指定特定的嵌套字段：

```python
# 返回 address 对象中的 city 字段
result = collection.find({}, {"address.city": 1})
```

#### 6. 使用投影操作符

MongoDB 支持一些特殊的投影操作符，例如 `$slice` 和 `$elemMatch`，用于处理数组字段：

- `$slice`: 用于限制数组字段中返回的元素数量

  ```python
  # 只返回 reviews 数组中的前 3 个元素
  result = collection.find({}, {"reviews": {"$slice": 3}})
  ```

- `$elemMatch`: 用于匹配数组中的特定元素

  ```python
  # 只返回 reviews 数组中符合条件的元素
  result = collection.find({}, {"reviews": {"$elemMatch": {"rating": {"$gte": 4}}}})
  ```

#### 7. 复杂的投影操作

你还可以在投影中使用表达式和计算，例如使用 `$cond` 操作符：

```python
# 计算 age 的值是否大于 30，并将结果作为新字段返回
pipeline = [
    {"$project": {"age_check": {"$cond": [{"$gt": ["$age", 30]}, True, False]}}}
]
result = collection.aggregate(pipeline)
```



### 聚合管道

MongoDB 的聚合管道（Aggregation Pipeline）是一种强大的数据处理工具，用于对集合中的文档进行逐步的转换和计算。通过一系列的阶段（stages），你可以对数据进行过滤、排序、分组、计算等操作。

- **管道（Pipeline）**：由多个阶段组成，每个阶段处理管道中传递的文档，最终生成所需的结果。

- **阶段（Stage）**：每个阶段都定义了特定的数据处理操作。文档从一个阶段传递到下一个阶段时，经过处理和转换。

语法：`db.集合名称.aggregate({管道:{表达式}})`

常用管道命令如下：

- `$group`： 将集合中的⽂档分组， 可⽤于统计结果
- `$match`： 过滤数据， 只输出符合条件的⽂档
- `$project`： 修改输⼊⽂档的结构， 如重命名、 增加、 删除字段、 创建计算结果
- `$sort`： 将输⼊⽂档排序后输出
- `$limit`： 限制聚合管道返回的⽂档数
- `$skip`： 跳过指定数量的⽂档， 并返回余下的⽂档



参考资料：

[MongoDB的聚合操作以及常用的管道表达式-CSDN博客](https://blog.csdn.net/qq_44096670/article/details/115558628)

