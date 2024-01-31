## Nmap安装与扫描基础

**安装好Nmap**

![image-20230316175629557](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910158.png)

**扫描主机**

![image-20230316180433754](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910159.png)

**扫描虚拟机**

![image-20230316180618244](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910160.png)

**扫描整个子网**

![image-20230316180813188](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910161.png)

**扫描所有主机，并确定系统类型**

`namp -sS -O ip`

![image-20230331131318091](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910162.png)

**随机选择任意10台主机检查80端口是否运行**

![image-20230316181602501](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910163.png)



## 选择和排除扫描目标



**用-iR随机扫描3台主机**

![image-20230331131609182](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910164.png)



**扫描192.168.1.0/24网段的主机但排除192.168.1.11**

![image-20230331131913440](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910165.png)

![image-20230331131945554](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910167.png)

![image-20230331132001473](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910168.png)





## 扫描发现存活的目标主机



**用-sL在网络上扫描nesst.com域的主机**

![image-20230331132417594](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910169.png)



**用-sn参数发现网络中192.168.1.1-20 的20台主机中存活主机**

![image-20230331132936142](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910170.png)



**-Pn参数将所有指定的主机视为开启状态，跳过主机发现的过程，直接报告端口开放情况**

![image-20230331133239899](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910171.png)



**组合参数探测**

![image-20230331133424302](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910172.png)



## 识别目标操作系统

**使用nmap -O目标主机地址来探测操作系统类型**

![image-20230331133808840](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910173.png)

**使用namp -O --osscan-guess目标主机地址来猜测操作系统类型**

![image-20230331134250269](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910174.png)



## 识别目标主机的服务及版本

**使用-sV进行基本版本扫描**

![image-20230331134644050](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910175.png)



**详尽的列出探测过程**

![image-20230331134817914](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910176.png)



**轻量级探测**

![image-20230331134904266](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910177.png)



**尝试使用所有probes探测**

![image-20230331135017270](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311910178.png)