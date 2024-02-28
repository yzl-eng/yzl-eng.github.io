# MySQL数据库简介

MySQL 是一个关系型数据库管理系统，由瑞典 MySQL AB 公司开发，目前属于 Oracle 公司。MySQL 是一种关联数据库管理系统，关联数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。

- MySQL 是开源的，目前隶属于 Oracle 旗下产品。
- MySQL 支持大型的数据库。可以处理拥有上千万条记录的大型数据库。
- MySQL 使用标准的 SQL 数据语言形式。
- MySQL 可以运行于多个系统上，并且支持多种语言。这些编程语言包括 C、C++、Python、Java、Perl、PHP、Eiffel、Ruby 和 Tcl 等。
- MySQL 对PHP有很好的支持，PHP 是目前最流行的 Web 开发语言。
- MySQL 支持大型数据库，支持 5000 万条记录的数据仓库，32 位系统表文件最大可支持 4GB，64 位系统支持最大的表文件为8TB。
- MySQL 是可以定制的，采用了 GPL 协议，你可以修改源码来开发自己的 MySQL 系统。

# MySQL使用



## MySQL创建数据库

我们可以在登陆 MySQL 服务后，使用 `create` 命令创建数据库，语法如下:

```mysql
create database 数据库名;
```

 还可在创建数据库时设置数据库的字符编码。

```mysql
create database 数据库名 character set utf8mb4;
```

`character set `可以缩写成 `charset` ，效果是一样的。

**MySQL字符集编码**一般设为`UTF-8mb4`，它是`utf8`的**超集**，支持4字节`unicode`（`utf8`只支持3字节的`unicode`），例如：`emoji`表情就是4字节。



 **相关操作**

- 显示数据库的创建信息
  ```mysql
  show create database 数据库名
  ```

- 进入或切换数据库

   ```mysql
   use 数据库名;
   ```
  
   刚连接上 MySQL 时，没有处于任何一个数据库中，如果要使用某一个数据库，就需要进入到这个数据库中。
  
  `use 数据库名` 这个命令后面的分号**可以省略**，这是 SQL 语句中**唯一**可以省略分号的语句。



## 数据表使用

1. **查看当前数据库中的表**

使用 `show tables;`查看当前数据库中有哪些表。

```mysql
show tables;
```

2. **创建表**

使用 `create table 表名(字段1 字段类型,字段2 字段类型,字段3 字段类型,…); `来创建一张表。

```mysql
create table Student(id INT, name CHAR(20), grade INT);
```

如上所示，在所选择的数据库中中创建了一个叫 `Student` 的数据表，这张表有三个字段 `id`，`name`，`grade`。

3. **显示表信息**

用 `show create table 表名;`来显示**已创建**的表的信息。

```mysql
show create table Student;
```

4. **给表增加字段**

使用 `alter table 表名 add 字段名 数据类型; `为已存在的表添加一个新字段。

```mysql
alter table Student add sex CHAR(20);
```

5. **删除表的字段**

使用 `alter table 表名 drop 字段名;` 删除一个表中**已存在**的字段。

```mysql
alter table Student drop sex;
```

6. **修改字段的数据类型**

使用 `alter table 表名 modify 字段名 数据类型; `修改表中现有字段的**数据类型**。

```mysql
alter table Student modify name VARCHAR(12);
```

修改之后，该字段的数据类型发生改变。

7. **修改字段的数据类型并且改名**

使用` alter table 表名 change 原字段名 新字段名 数据类型;` 修改表中现有字段的**字段名**和**类型**。

```mysql
alter table Student change name pname CHAR(18);
```

8. **删除数据表**

```mysql
 drop table 数据表名;
```

9. 插入数据

```mysql
insert into 数据表名(column1,column2...)
VALUES (值1,值2,...);
```

## 插入数据

MySQL 表中使用 **INSERT INTO** SQL语句来插入数据。

你可以通过 mysql> 命令提示窗口中向数据表中插入数据，或者通过PHP脚本来插入数据。

**语法**

以下为向MySQL数据表插入数据通用的 **INSERT INTO** SQL语法：

```mysql
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );
```

如果数据是字符型，必须使用单引号或者双引号，如："value"。

## 查询数据

MySQL 数据库使用`select`语句来查询数据。

以下为在MySQL数据库中查询数据通用的 SELECT 语法：

```mysql
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]
```

- 查询语句中你可以使用一个或者多个表，表之间使用逗号`,`分割，并使用`where`语句来设定查询条件。

- `select`命令可以读取一条或者多条记录。

- 你可以使用星号`*`来代替其他字段，`select`语句会返回表的所有字段数据

- 你可以使用 `where` 语句来包含任何条件。

- 你可以使用 `limit` 属性来设定返回的记录数。

- 你可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。

### where子句

- 查询语句中你可以使用一个或者多个表，表之间使用逗号`,` 分割，并使用WHERE语句来设定查询条件。
- 你可以在` WHERE` 子句中指定任何条件。
- 你可以使用 `AND` 或者 `OR` 指定一个或多个条件。
- `WHERE` 子句也可以运用于 SQL 的 `DELETE` 或者 `UPDATE` 命令。
- WHERE 子句类似于程序语言中的 if 条件，根据 MySQL 表中的字段值来读取指定的数据。

### update更新

如果我们需要修改或更新 MySQL 中的数据，我们可以使用 SQL UPDATE 命令来操作。

**语法**

以下是 UPDATE 命令修改 MySQL 数据表数据的通用 SQL 语法：

```mysql
UPDATE 数据表名 SET field1=new-value1, field2=new-value2
[WHERE Clause]
```

- 你可以同时更新一个或多个字段。
- 你可以在 `WHERE` 子句中指定任何条件。
- 你可以在一个单独表中同时更新数据。



### delete语句

你可以使用 SQL 的` DELETE FROM `命令来删除 MySQL 数据表中的记录。

**语法**

以下是 SQL DELETE 语句从 MySQL 数据表中删除数据的通用语法：

```mysql
DELETE FROM 数据表名 [WHERE Clause]
```

- 如果没有指定 WHERE 子句，MySQL 表中的所有记录将被删除。
- 你可以在 WHERE 子句中指定任何条件
- 您可以在单个表中一次性删除记录。



### like子句

我们知道在 MySQL 中使用 SQL SELECT 命令来读取数据， 同时我们可以在 `SELECT` 语句中使用` WHERE` 子句来获取指定的记录。

SQL LIKE 子句中使用百分号 `%`字符来表示任意字符，类似于`UNIX`或**正则表达式**中的星号 `*`。

如果没有使用百分号 `%`, `LIKE` 子句与等号 `=` 的效果是一样的。

**语法**

以下是 SQL SELECT 语句使用 LIKE 子句从数据表中读取数据的通用语法：

```mysql
SELECT field1, field2,...fieldN 
FROM 数据表名
WHERE field1 LIKE condition1 [AND [OR]] filed2 = 'somevalue'
```

- 你可以在 `WHERE `子句中指定任何条件。
- 你可以在` WHERE` 子句中使用`LIKE`子句。
- 你可以使用`LIKE`子句代替等号 `=`。
- `LIKE` 通常与`%` 一同使用，类似于一个元字符的搜索。
- 你可以使用 `AND` 或者 `OR` 指定一个或多个条件。
- 你可以在 `DELETE` 或` UPDATE` 命令中使用 `WHERE...LIKE` 子句来指定条件。



### union

MySQL UNION 操作符用于连接两个以上的 `SELECT` 语句的结果组合到一个结果集合中。多个 `SELECT` 语句会删除重复的数据。

**语法**

MySQL UNION 操作符语法格式：

```mysql
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION [ALL | DISTINCT]
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];
```

**参数**

- **expression1, expression2, ... expression_n**: 要检索的列。
- **tables:** 要检索的数据表。
- **WHERE conditions:** 可选， 检索条件。
- **DISTINCT:** 可选，删除结果集中重复的数据。默认情况下 UNION 操作符已经删除了重复数据，所以 DISTINCT 修饰符对结果没啥影响。
- **ALL:** 可选，返回所有结果集，包含重复数据。



## MySQL聚集函数

**COUNT() 函数 计算总行数**

Count() 函数进行计数。 可以利用Count() 函数确定表中行的数目或符合特定条件的行的数目。

COUNT() 函数的两种使用方式：

　　1、使用Count（*） 对表中的数目进行计数，**不管表列中包含的是空值（NULL） 还是非空值**。

　　2、使用count(column) 对特定列中具有值的行进行计数，忽略NULL 值

## MySQL排序

我们知道从 MySQL 表中使用 SQL SELECT 语句来读取数据。

如果我们需要对读取的数据进行排序，我们就可以使用 MySQL 的` ORDER BY` 子句来设定你想按哪个字段哪种方式来进行排序，再返回搜索结果。

**语法**

以下是 `SQL SELECT` 语句使用 `ORDER BY `子句将查询数据排序后再返回数据：

```mysql
SELECT field1, field2,...fieldN FROM table_name1, table_name2...
ORDER BY field1 [ASC [DESC][默认 ASC]], [field2...] [ASC [DESC][默认 ASC]]
```

- 你可以使用任何字段来作为排序的条件，从而返回排序后的查询结果。
- 你可以设定多个字段来排序。
- 你可以使用` ASC` 或 `DESC `关键字来设置查询结果是按**升序**或**降序**排列。 默认情况下，它是按升序排列。
- 你可以添加 `WHERE...LIKE` 子句来设置条件。

## MySQL分组

`GROUP BY` 语句根据一个或多个列对结果集进行**分组**。

在分组的列上我们可以使用 `COUNT`, `SUM`, `AVG`,等函数。

**语法**

```mysql
SELECT column_name, function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name;
```

### Having子句



### 使用 WITH ROLLUP

## MySQL 连接的使用

使用 MySQL 的 JOIN 在两个或多个表中查询数据。

你可以在 SELECT, UPDATE 和 DELETE 语句中使用 Mysql 的 JOIN 来联合多表查询。

JOIN 按照功能大致分为如下三类：

- **INNER JOIN（内连接,或等值连接）**：获取两个表中字段匹配关系的记录。
- **LEFT JOIN（左连接）：**获取左表所有记录，即使右表没有对应匹配的记录。
- **RIGHT JOIN（右连接）：** 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。

一般我们`join`后的表，并不是我们想要的，这时，可以用 `ON` 来加一些条件：

## MySQL ALTER命令

当我们需要修改数据表名或者修改数据表字段时，就需要使用到MySQL ALTER命令。

## MySQL 索引

## 普通索引

### 创建索引

这是最基本的索引，它没有任何限制。它有以下几种创建方式：

```mysql
CREATE INDEX indexName ON table_name (column_name)
```

如果是CHAR，VARCHAR类型，length可以小于字段实际长度；如果是BLOB和TEXT类型，必须指定 length。

### 修改表结构(添加索引)

```mysql
ALTER table tableName ADD INDEX indexName(columnName)
```

### 创建表的时候直接指定

```mysql
CREATE TABLE mytable(  
 
ID INT NOT NULL,   
 
username VARCHAR(16) NOT NULL,  
 
INDEX [indexName] (username(length))  
 
);  
```

### 删除索引的语法

```mysql
DROP INDEX [indexName] ON mytable; 
```

## MySQL视图

```tex
en
conf t
ip route 192.168.1.0 255.255.255.0 192.168.3.1
end
show ip route
```

