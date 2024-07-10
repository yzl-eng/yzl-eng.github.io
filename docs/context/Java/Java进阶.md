## 反射基础



#### 得到Class类的几种方式
对象照镜子后可以得到的信息:某个类的属性、方法和构造器、某个类到底实现了哪些接口.对于每个类而言，JRE 都为其保留一个不变的Class类型的对象。

一个Class对象包含了特定某个结构(`class/interface/enum/annotation/primitive type/void/[]`)的有关信息。

- Class本身也是一个类

- Class对象只能由系统建立对象

- 一个加载的类在JVM中只会有一个Class实例

- 一个Class对象对应的是一个加载到JVM中的一个.class文件

- 每个类的实例都会记得自己是由哪个Class实例所生成

- 通过Class可以完整地得到一个类中的所有被加载的结构

- Class类是Reflection的根源，针对任何你想动态加载、运行的类，唯有先获得相应的Class对象

  

**获取class类的实例**

1. 若已知具体的类，通过类的class属性获取，该方法最为安全可靠，程序性能最高

   > Class class = User.class; 

2. 已知某个类的实例，调用该实例的`getClass()`方法获取Class对象

   > Class class = user.getClass();

3. 已知一个类的全类名，且该类在类路径下，可通过Class类的静态方法`forName()`获取，可能抛出`ClassNotFoundException` [参考](https://www.cnblogs.com/chanshuyi/p/head_first_of_reflection.html)

   > Class class = Class.forName("reflect.User")

4. 内置基本数据类型可以直接用类名.Type

5. 利用ClassLoader,通过类加载器`xxxClassLoader.loadClass()`传入类路径获取

   > ClassLoader.getSystemClassLoader().loadClass("reflect.User");



**举例**

```java
package com.example.demo;

class Person{
    public String name;

    public Person(){}

    public Person(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                '}';
    }
}

class Student extends Person{
    public Student(){
        this.name = "学生";
    }
}
class Teacher extends Person{
    public Teacher(){
        this.name = "老师";
    }
}


public class ReflectTest1 {
    public static void main(String[] args) throws ClassNotFoundException {
        Person person = new Student();
        System.out.println(person.name);

        //方式一：通过对象获得
        Class c1 = person.getClass();
        System.out.println(c1.hashCode());
        //方式二：forNmae()获得
        Class c2 = Class.forName("com.example.demo.Student");
        System.out.println(c2.hashCode());
        //方式三：通过类名.class获得
        Class c3 = Student.class;
        System.out.println(c3.hashCode());
        //方式四：基本内置类型的包装类都有一个Type属性
        Class c4 = Integer.TYPE;
        System.out.println(c4);
        //获得父类类型
        Class c5 = c1.getSuperclass();
        System.out.println(c5);

    }
}
```

结果

![image-20240627193404501](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202406271934602.png)



### 反射的用途

**反射功能通常用于检查或修改Java虚拟机运行中（runtime）的应用程序的行为**，这一句话就精准的描述了反射的全部功能，更详细来说可以分为以下几点：


 1. 在运行中分析类的能力，可以通过完全限定类名创建类的对象实例。

 2. 在运行中查看和操作对象，可以遍历类的成员变量。

 3. 反射允许代码执行非反射代码中非法的操作，可以检索和访问类的私有成员变量，包括私有属性、方法等。




### 利用反射获取构造方法

**Class类中用于获取构造方法的方法**

`Constructor<?>[]getConstructors()`:返回所有公共构造方法对象的数组

`Constructor<?>[]getDeclaredConstructors()`:返回所有构造方法对象的数组

`Constructor<T>getConstructor(Class<?>... parameterTypes)`:返回单个公共构造方法对象

`Constructor<T>getDeclaredConstructor(Class<?>... parameterTypes)`:返回单个构造方法对象

**Constructor类中用于创建对象的方法**

`TnewInstance(Object...initargs)`:根据指定的构造方法创建对象

`setAccessible(boolean flag)`:设置为`true`,表示取消访问检查