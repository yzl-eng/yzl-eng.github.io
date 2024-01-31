首先，通过如下操作创建一个空的虚拟机

![image-20230308144521685](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908761.png)

![image-20230308144632793](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908762.png)

客户机操作系统选择**Linux**，版本选**Debian 8.x**

![image-20230308144712511](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908763.png)

随后选择虚拟机名称后，按默认设置，完成虚拟机配置

![image-20230308144959566](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908764.png)

![image-20230308145020489](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908765.png)

![image-20230308145033998](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908766.png)

创建完成后，将下载好的系统文件挂载进虚拟机，系统版本为2022.4

![image-20230308145243686](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908767.png)

随后启动虚拟机，选择第一个**Graphical install**选项

![image-20230308145518630](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908768.png)

选择中文，键盘选择汉语

![image-20230308145717103](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908769.png)

等待系统相关操作完成后，选择主机名等操作

![image-20230308145851562](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908770.png)

配置密码

![image-20230308145954511](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908771.png)

选择默认的操作

![image-20230308150048574](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908772.png)

选择是

![image-20230308150114323](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908773.png)

随后等待系统安装

点击继续，然后继续等待

![image-20230308150520157](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908774.png)

选择**是**，并继续

![image-20230308151759128](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908775.png)

选择第二个

![image-20230308151833136](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908776.png)

安装完成

![image-20230308152218348](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908777.png)





密码错误可修改

![image-20230308154132316](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908778.png)

![image-20230308152629552](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908779.png)



输入账号密码进入系统

![image-20230308152916102](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908780.png)

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



![image-20230308153242195](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908781.png)



输入`apt-get update` 更新索引    `apt-get dist-upgrade` 升级

输入`apt-get install ibus ibus-pinyin`下载输入法

![image-20230308153708246](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908782.png)

输入`im-config`  选择启用ibus输入法

![image-20230308153925785](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908783.png)

![image-20230308154018675](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311908784.png)