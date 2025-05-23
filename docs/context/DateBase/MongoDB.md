MongoDB是一个流行的开源文档型数据库，它使用类似 JSON 的文档模型存储数据，这使得数据存储变得非常灵活。

MongoDB 是一个基于**文档**的 NoSQL 数据库，由 MongoDB Inc. 开发。

MongoDB 旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。

MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。

Mongo最大的特点是它支持的查询语言非常强大，其语法有点类似于面向对象的查询语言，几乎可以实现类似关系数据库单表查询的绝大部分功能，而且还支持对数据建立索引

业务应用场景
传统的关系型数据库(如MySQL)，在数据操作的三高需求以及应对Web2.0的网站需求面前，显得力不从心，而 MongoDB可应对“三高“需求

High performance：对数据库高并发读写的需求

Huge Storage：对海量数据的高效率存储和访问的需求

High Scalability && High Availability：对数据库的高可扩展性和高可用性的需求

具体应用场景：

社交场景，使用 MongoDB存储存储用户信息，以及用户发表的朋友圈信息，通过地理位置索引实现附近的人、地点等功能。
游戏场景，使用 MongoDB存储游戏用户信息，用户的装备、积分等直接以内嵌文档的形式存储，方便查询、高效率存储和访问。
物流场景，使用 MongoDB存储订单信息，订单状态在运送过程中会不断更新，以 MongoDB内嵌数组的形式来存储，一次查询就能将订单所有的变更读取出来
物联网场景，使用 MongoDB存储所有接入的智能设备信息，以及设备汇报的日志信息，并对这些信息进行多维度的分析。
视频直播，使用 MongoDB存储用户信息、点赞互动信息等。
这些应用场景中，数据操作方面的共同特点是：

（1）数据量大

（2）写入操作频繁（读写都很频繁）

（3）价值较低的数据，对事务性要求不高

对于这样的数据，我们更适合使用 MongoDB来实现数据的存储。





选择要操作的数据库

```shell
use DatebaseName
```



### 集合相关



查看所有集合

```mongodb
show collections
```

创建集合(插入数据会隐式创建)

```mongodb
db.createCollection('集合名')
```

删除集合

```mongodb
db.集合名.drop()
```



## CURD

### 插入

```mongodb 
db.集合名.insert(json数据)
```

测试

```mongodb
//demo为所使用集合名
db.demo.insert({name:'zhangsan',age:'18'})

//循环插入数据
for(var i=1;i<10;i++){
	db.demo.insert({name:"a"+i,age:i})
}
```

我们也可以将数据定义为一个变量，如下所示：

```mongodb
temp={name:'lisi',age:19}
db.demo.insert(temp)
```



**示例：**

```mongodb
db.test0.insertOne(
  {
    title: "The Favourite",
    runtime: 121,
    year: 2018,
    type: "movie"
  }
)
```







### 查询 



查询所有数据` {}`或不写

```mongodb
db.test0.find({})
db.test0.find()
```

该操作等同于以下 SQL 语句：

```sql
SELECT * FROM test0
```



查询指定要求数据` {key:value}`或`{key:{运算符:value}}`

```mongodb
# 查找title为The Favorite的条目
db.test0.find({title: "The Favourite"})

# 查找所有age小于14
db.test0.find({age: {$lt:14}})
```

运算符

- `$eq `等于

- `$gt` 大于
- `$gte` 大于等于
- `$lt` 小于
- `$lte` 小于等于
- `$ne` 不等于
- `$nin` not in 不在指定数组中
- `$in` in 在指定数组中



```shell
db.tenant_col.find({'contracts': {'bills':{'status':{$ne:'settled'}}})
```





`$regex`为查询中的模式匹配*字符串*提供正则表达式功能。

```mongodb
target="The Favourite"
db.test0.find({'title': {'$regex': target, '$options': 'i'}})
```



查询的列(可选参数)
不写则查询全部列
`{key:1}` 只显示key列
`{key:0}` 除了key列都显示
注意:`_id`列都会存在

查询指定列的所有数据

查询指定条件的数据

排序
`db.集合名.find().sort(json数据)`

 json数据(key:value)

- key就是要排序的字段
- value为1表示升序,-1表示降序



### 删除

- 要删除多个文档，请使用 `db.collection.deleteMany()`
- 要删除单个文档，请使用 `db.collection.deleteOne()`



```mongodb
db.test0.deleteOne( { name: "a1" } )
```



```mongodb
db.test0.deleteMany( { name: {'$regex': 'a', '$options': 'i'}} )
```

以下方法在**mongosh**中已弃用

```mongodb
db.集合名.remove(删除条件,     
	{
	justOne: <boolean>,
	writeConcern: <document> 
	} 
)
```

- **justOne** : （可选）如果设为 `true` 或 1，则只删除一个文档，默认全部删除。
- **writeConcern** :（可选）抛出异常的级别。

测试

```mongodb
db.demo.remove(name:'zhangsan')
```

也可以使用以下方式实现全部删除

```mongodb
db.demo.remove({}) 
```



### 更新

- 要更新单个文档，请使用`db.collection.updateOne()` 
- 要更新多个文档，请使用`db.collection.updateMany()` 
- 要替换文档，请使用 `db.collection.replaceOne()`

示例：

```mongodb
db.test0.updateOne( { title: "The Favourite" },
{
  $set: {
    runtime:123
  },
  $currentDate: { lastUpdated: true }
})
```

更新操作：

- 使用`$set`操作符更新电影`The Favourite`的`  runtime`字段的值。

- 使用`$currentDate`操作符将`lastUpdated`字段的值更新为当前日期。如果`lastUpdated`字段不存在， `$currentDate`将创建该字段。

  

`$set`: 用于设置字段的值。如果字段不存在，它将会创建这个字段。

`$push`: 用于将一个值添加到数组的末尾。如果数组不存在，它会创建一个新的数组。



`$setOnInsert`:如果某一更新操作导致插入文档，则设置字段的值。文档不存在，则插入新文档时，通过该操作符，来设置字段

 `$addToSet`:与 `$push` 类似，但会确保不添加重复元素：

### 使用数组过滤器

在 MongoDB 中，使用数组过滤器可以对数组中的特定元素进行操作。数组过滤器是 `$[]` 和 `$[<identifier>]` 的结合使用，其中：

- `$[]`: 表示对数组中的所有元素进行操作。
- `$[<identifier>]`: 允许你指定特定的数组元素进行操作，`<identifier>` 是一个用于标识数组元素的变量名。



[参考资料](https://blog.csdn.net/efew212efe/article/details/124524863)





