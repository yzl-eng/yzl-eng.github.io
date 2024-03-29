## 在Windows server 2008虚拟机中配置IIS

打开服务器管理，添加角色

![image-20230411180418702](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311857288.png)

选择安装Web服务器

![image-20230411180510536](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311857768.png)

添加角色，选择下一步

![image-20230411180618223](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311857680.png)

安装需要的服务

![image-20230411180746805](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311857031.png)

完成安装

![image-20230411181004391](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311857806.png)

![image-20230411181158343](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311857072.png)



## 搭建dvwa靶机

开启windows server 的远程桌面访问

![image-20230411181322454](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311857517.png)

![image-20230411181402402](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311857399.png)

从物理机远程连接控制windows server

![image-20230411181558326](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311857672.png)



传入文件dvwa压缩包phpstudy安装包

![image-20230413170833569](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311857368.png)

安装phpstudy

![image-20230414085708518](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858137.png)

将dvwa文件放在inetpub文件夹下的wwwroot文件夹中

![image-20230414085533096](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858915.png)

在浏览器中访问http://localhost/dvwa/setup.php，创建用户

![image-20230418002325273](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858074.png)

出现错误

![image-20230418002451627](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858955.png)

更改配置文件

![image-20230418002553021](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858685.png)

更改成如下配置

![image-20230418002644673](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858465.png)

在浏览器中访问http://localhost/dvwalogin.php，

![image-20230418002911565](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858038.png)

username：admin

 password

进入http://localhost/dvwa/index.php，搭建完成

![image-20230418003056219](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858759.png)





步骤1:在Kali虚拟机中打开Burp Suite工具并设置。
打开`Proxy`选项卡，选中`Proxy setting`子选项卡，单击“Add”按钮，增加一个监听代理，通常设置为127.0.0.1:8080，。

![image-20230411173059436](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858528.png)

步骤2:启动Kali虚拟机中的浏览器，单击右上角的菜单按钮，选择“设置”选项

![image-20230411174739246](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858371.png)

步骤3:打开网络设置的“设置“（连接设置”对话框，进行手动代理设置，如图所示。）

![image-20230411175005946](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858229.png)

步骤4:在Kali中打开“Intercept”子选项卡，下面的“Intercept is on”表示开启数据包拦截功能,反之即是放行所有Web流量，如图所示。

![image-20230411175339792](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858382.png)

步骤5:打开Kali中的浏览器，并在地址栏中输入服务器IP，如图所示。

![image-20230418082839086](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311858306.png)

步骤6:在 Burp Suite中可以看到所拦截的数据，如图所示。

![image-20230418082700819](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859388.png)







## Burp_Suite专业版安装

**kali自带的Burp Suite为社区版，部分选项卡无法找到，所以需要更换JDK版本，以及重新安装专业版的Burp Suite**

```shell
cd ~/下载
tar -zxvf jdk-8u131-linux-x64.tar.gz
```

![image-20230418085247979](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859732.png)



```shell
mv jdk1.8.0_131 /opt
cd /opt/jdk1.8.0_131
```

![image-20230418090159753](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859232.png)

```shell
vi /etc/profile
```

![image-20230418090248934](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859469.png)

配置环境变量

``` shell
export JAVA_HOME=/opt/jdk1.8.0_131
export CLASSPATH=.:${JAVA_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
```

更新环境

```shell
source /etc/profile
```

 安装注册jdk

```shell
update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_131/bin/java 1
update-alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_131/bin/javac 1
update-alternatives --set java /opt/jdk1.8.0_131/bin/java
update-alternatives --set javac /opt/jdk1.8.0_131/bin/javac
```

 

![image-20230418090909668](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859477.png)

**JDK安装完成**

![image-20230418091249715](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859318.png)





**Burp_Suite_Pro_v1.7.37_Loader_Keygen**  

下载连接：https://wwm.lanzoul.com/iJmSJkavl2j 密码:7bwp



移入虚拟机中，先解压

```shell
unzip Burp_Suite_Pro_v1.7.37_Loader_Keygen.zip 
```

![image-20230418092352846](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859725.png)

打开Burp解压包把两个.jar文件剪切到`/usr/bin`目录里，然后`Java -jar `启动burp激活软件

```shell
mv burp-loader-keygen.jar burpsuite_pro_v1.7.37.jar /usr/bin 
cd /usr/bin
java -jar burp-loader-keygen.jar
```

![image-20230418092808469](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859959.png)

![image-20230418092918008](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859763.png)

![image-20230418093003635](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859235.png)

![image-20230418093043585](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859070.png)

![image-20230418093141164](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859135.png)

![image-20230418093259340](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311859728.png)

![image-20230418093344226](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900340.png)

 先退出

![image-20230418093503565](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900837.png)

配置快捷方式:在`/usr/bin`下创建**burpsuite**（如果有先删除再创建）

```shell
mousepad burpsuite_pro
```



```shell
#!/bin/sh
java -Xbootclasspath/p:/usr/bin/burp-loader-keygen.jar -jar /usr/bin/burpsuite_pro_v1.7.37.jar
```

 增加执行权限`chmod +x burpsuite `进入`/usr/share/applications`，创建并编辑burpsuite的快捷方式 

```shell
chmod +x burpsuite_pro
cd /usr/share/applications/
mousepad burpsuite_pro.desktop
```



```sell
[Desktop Entry]
Name=burpsuite_pro
Encoding=UTF-8
Exec=sh -c "/usr/bin/burpsuite_pro"
Icon=kali-burpsuite
StartupNotify=false
Terminal=false
Type=Application
Categories=03-webapp-analysisc;03-06-web-application-proxies;
X-Kali-Package=burpsuite
```

**相关资料**

[kali安装专业版burpsuite - 木讷叶 - 博客园 (cnblogs.com)](https://www.cnblogs.com/yeblade/p/14266385.html)



## Brup Suite Target功能

**步骤一：启动Burp Suite 打开Target ->Site map**

![image-20230418083804605](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900508.png)



![image-20230418144512530](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900226.png)

**步骤三：Target Scope目标域规则设置**

![image-20230418144630698](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900534.png)



![image-20230418144853657](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900853.png)



## Burp Suite Spider功能

**步骤1:打开 Burp Suite，根据前面Target 中的有关配置，选中要测试的页面链接。右击目标网站地址，选中`Spider this host`命令，如图所示。**

![image-20230418145329125](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900098.png)

**步骤2:对“Spider”选项卡下的“Options”子选项卡的有关选项取默认配置，如图所示。**

![image-20230418145528108](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900046.png)

**步骤3:单击“Spider”选项卡中的`Control`标签，单击`Spider is running`按钮，如图所示，下方显示已经请求数量、字节传输量、爬虫范围等信息。**

![image-20230418145639077](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900822.png)



## Burp Suite Scanner功能

**步骤1:启动 Burp Suite，正确配置Burp Proxy并设置浏览器代理，同时在`Target`选项卡的`Site map`子选项卡中配置好需要扫描的域和URL模块路径，右击需要扫描的站点，选择快捷菜单中的`Actively Scan this host`命令，如图所示。**

![image-20230418150003829](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900390.png)

**步骤2:打开主动扫描配置向导，如图4-31所示，可以选择是否移除有关的页面项**

![image-20230418154521980](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311900127.png)

**步骤3:单击图中的`Next`按钮，打开图所示的窗口，继续对扫描项进行配置，将不需要扫描的网址移除,以提高扫描效率。**

![image-20230418154549592](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901058.png)

**步骤4:对攻击插入点进行配置，如图所示。**

![image-20230418154652754](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901565.png)



**步骤5:进入`Scanncr`选项卡的`Scan queue`子选项卡，查看当前扫描的进度，如图所示。**

![image-20230418154742457](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901946.png)

**步骤6:配置主动扫描与被动扫描,如图所示**

![image-20230418154839559](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901059.png)

**步骤7:在`Target`选项卡的`Site map`子选项卡下选择某个子目录进行扫描，则会弹出更优化的扫描选项，可以对选项进行设置，指定哪些类型的文件不在扫描范围内，如图所示。**

![image-20230418160110313](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901143.png)

**步骤8:在图所示的`Target`选项卡的`Site map`子选项卡中选中需要添加的网址，单击鼠标右键，在弹出的快捷菜单中选择`Add to scope`命令，将该网址添加到作用域中，然后进行自动扫描。**

![image-20230418160043144](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901443.png)

**步骤9:进入`Scanner`选项卡的`Live scanning`子选项卡，在Live Active Scanning 中选择`Use suite scope[defined in Target tab]”`单选按钮，Burp Scanner将自动扫描经过 Burp Proxy的交互信息，如图4-38所示。**

![image-20230418160335611](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901551.png)

**步骤10:查看扫描结果。选择`Results`子选项卡，可以查看此次扫描的结果，如图4所示。**

![image-20230418160925837](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901062.png)



## Burp Suite Intruder爆破应用

**步骤1:启动Burp Suite，并按照任务一的介绍完成代理配置。**

![image-20230418161114964](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901185.png)

**步骤2:用浏览器访问网站 `本机IP/dvwa`，这里以渗透测试系统 dvwa为靶机站点,如图所示。**

![image-20230421175024202](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901489.png)

![image-20230418161030091](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901718.png)

**步骤3:单击图中的`Brute Force`按钮，并单击Burp Suite的`Proxy`选项卡下的`Forward`按钮，在浏览器中打开图所示的界面，输入登录账号及密码，假定已知登录账号为admin，而密码需要爆破，因此随意输入一个密码。**

![image-20230418161217753](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311901622.png)

![image-20230418161409064](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311902307.png)

**步骤4:单击图中的`Login`按钮，并在 Burp Suite中截取登录数据，如图所示。**

![image-20230418162746429](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311902816.png)

![image-20230421175548999](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311902961.png)

**步骤5:选中图中的所有数据并在右键快捷菜单中选择`Send to Intruder`命令，如图所示。**

![image-20230418162923186](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311902891.png)



**步骤6:选择`Intruder`选项卡，并选择`Positions`子选项卡，对爆破变量进行配置,如图所示。**

![image-20230418163038940](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311902293.png)

**步骤7:对图4-47中自动标记的变量进行爆破，单击右边的`Clearf`按钮，然后选中密码后面的123456，再添加为爆破变量,如图所示。**

![image-20230418163337450](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311902164.png)



![image-20230418163511132](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311902576.png)

**步骤8:选择`Intruder`选项卡，并选择`Payloads`子选项卡，对爆破变量所需的密码文件进行配置,如图所示。**

注:这里的密码文件可以从网上下载，也可以自定义，其中要包括本次测试用的密码，路径不能有中文

![image-20230421175448772](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311902152.png)

**步骤9:设置完成后，单击 Burp Suite 中的`Intruder`菜单项，选择`Start attack`命令如图所示**

![image-20230418163849810](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311902803.png)

**步骤10:在爆破结果中，对密码文件中的密码进行逐个测试,**

![image-20230418165712060](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311903686.png)
