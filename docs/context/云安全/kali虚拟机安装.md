首先，通过如下操作创建一个空的虚拟机

![image-20230308144521685](kali虚拟机安装.assets/image-20230308144521685.png)

![image-20230308144632793](kali虚拟机安装.assets/image-20230308144632793.png)

客户机操作系统选择**Linux**，版本选**Debian 8.x**

![image-20230308144712511](kali虚拟机安装.assets/image-20230308144712511.png)

随后选择虚拟机名称后，按默认设置，完成虚拟机配置

![image-20230308144959566](kali虚拟机安装.assets/image-20230308144959566.png)

![image-20230308145020489](kali虚拟机安装.assets/image-20230308145020489.png)

![image-20230308145033998](kali虚拟机安装.assets/image-20230308145033998.png)

创建完成后，将下载好的系统文件挂载进虚拟机，系统版本为2022.4

![image-20230308145243686](kali虚拟机安装.assets/image-20230308145243686.png)

随后启动虚拟机，选择第一个**Graphical install**选项

![image-20230308145518630](kali虚拟机安装.assets/image-20230308145518630.png)

选择中文，键盘选择汉语

![image-20230308145717103](kali虚拟机安装.assets/image-20230308145717103.png)

等待系统相关操作完成后，选择主机名等操作

![image-20230308145851562](kali虚拟机安装.assets/image-20230308145851562.png)

配置密码

![image-20230308145954511](kali虚拟机安装.assets/image-20230308145954511.png)

选择默认的操作

![image-20230308150048574](kali虚拟机安装.assets/image-20230308150048574.png)

选择是

![image-20230308150114323](kali虚拟机安装.assets/image-20230308150114323.png)

随后等待系统安装

点击继续，然后继续等待

![image-20230308150520157](kali虚拟机安装.assets/image-20230308150520157.png)

选择**是**，并继续

![image-20230308151759128](kali虚拟机安装.assets/image-20230308151759128.png)

选择第二个

![image-20230308151833136](kali虚拟机安装.assets/image-20230308151833136.png)

安装完成

![image-20230308152218348](kali虚拟机安装.assets/image-20230308152218348.png)





密码错误可修改

![image-20230308154132316](kali虚拟机安装.assets/image-20230308154132316.png)

![image-20230308152629552](kali虚拟机安装.assets/image-20230308152629552.png)



输入账号密码进入系统

![image-20230308152916102](kali虚拟机安装.assets/image-20230308152916102.png)

在终端中输入`vim /etc/apt/sources.list`,配置国内源



> #中科大
> deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
> deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
> #阿里云
> #deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
> #deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
> #清华大学
> #deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
> #deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
> #浙大
> #deb http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free
> #deb-src http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free
> #东软大学
> #deb http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
> #deb-src http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
> #重庆大学
> #deb http://http.kali.org/kali kali-rolling main non-free contrib
> #deb-src http://http.kali.org/kali kali-rolling main non-free contrib



![image-20230308153242195](kali虚拟机安装.assets/image-20230308153242195.png)



输入`apt-get update` 更新索引    `apt-get dist-upgrade` 升级

输入`apt-get install ibus ibus-pinyin`下载输入法

![image-20230308153708246](kali虚拟机安装.assets/image-20230308153708246.png)

输入`im-config`  选择启用ibus输入法

![image-20230308153925785](kali虚拟机安装.assets/image-20230308153925785.png)

![image-20230308154018675](kali虚拟机安装.assets/image-20230308154018675.png)