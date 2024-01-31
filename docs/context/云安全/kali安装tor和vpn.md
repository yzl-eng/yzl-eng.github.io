

### 配置VPN

> apt-get install network-manager-openvpn-gnome network-manager-pptp network-manager-pptp-gnome

> apt-get install network-manager-strongswan

> apt-get install network-manager-vpnc network-manager-vpnc-gnome

![image-20230314171030518](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906935.png)

**修改/etc/NetworkManager/下的NetworkManager.conf文件**

> cd /etc/NetworkManager/

![image-20230314171435168](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906936.png)

**将`NetworkManager.conf`文件中的`managed=false`改为`managed=true`**

![image-20230314171602085](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906937.png)

**点击网络，选择VPN连接，选择PPTP**

![image-20230314172529055](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906938.png)

**添加网关和用户名**

![image-20230314172741773](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906939.png)

**选择高级，勾选MPPE**

![image-20230314172854142](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906940.png)



![image-20230314173652137](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906941.png)



### TOR安装与验证

> apt-get install tor

![image-20230314173850454](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906942.png)

> apt-get install torbrowser-launcher

![image-20230314174116092](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906943.png)



### 配置安全测试浏览器及系统清理备份

> apt -y install firefox-esr-l10n-zh-cn

![image-20230314174916535](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906944.png)



![image-20230314175234771](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906945.png)

![image-20230314175311804](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906946.png)





![image-20230314175135794](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906947.png)



![image-20230314175446206](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906948.png)



![image-20230314175534391](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906949.png)

**下载Hcon**

![image-20230315002232442](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906950.png)



> tar jxvf HconSTF_v0.5_Prime_Linux_x64.tar.bz2

**解压文件**

![image-20230315002651845](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906951.png)

**删除安装过的文件包，命令为apt-get autoclean**

**自动卸载没用的软件，命令为：apt-get autoremove**

![image-20230315003235957](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311906952.png)

**系统备份**

**虚拟机使用快照完成备份**