

### 配置VPN

> apt-get install network-manager-openvpn-gnome network-manager-pptp network-manager-pptp-gnome

> apt-get install network-manager-strongswan

> apt-get install network-manager-vpnc network-manager-vpnc-gnome

![image-20230314171030518](kali安装tor和vpn.assets/image-20230314171030518.png)

**修改/etc/NetworkManager/下的NetworkManager.conf文件**

> cd /etc/NetworkManager/

![image-20230314171435168](kali安装tor和vpn.assets/image-20230314171435168.png)

**将`NetworkManager.conf`文件中的`managed=false`改为`managed=true`**

![image-20230314171602085](kali安装tor和vpn.assets/image-20230314171602085.png)

**点击网络，选择VPN连接，选择PPTP**

![image-20230314172529055](kali安装tor和vpn.assets/image-20230314172529055.png)

**添加网关和用户名**

![image-20230314172741773](kali安装tor和vpn.assets/image-20230314172741773.png)

**选择高级，勾选MPPE**

![image-20230314172854142](kali安装tor和vpn.assets/image-20230314172854142.png)



![image-20230314173652137](kali安装tor和vpn.assets/image-20230314173652137.png)



### TOR安装与验证

> apt-get install tor

![image-20230314173850454](kali安装tor和vpn.assets/image-20230314173850454.png)

> apt-get install torbrowser-launcher

![image-20230314174116092](kali安装tor和vpn.assets/image-20230314174116092.png)



### 配置安全测试浏览器及系统清理备份

> apt -y install firefox-esr-l10n-zh-cn

![image-20230314174916535](kali安装tor和vpn.assets/image-20230314174916535.png)



![image-20230314175234771](kali安装tor和vpn.assets/image-20230314175236338.png)

![image-20230314175311804](kali安装tor和vpn.assets/image-20230314175311804.png)





![image-20230314175135794](kali安装tor和vpn.assets/image-20230314175135794.png)



![image-20230314175446206](kali安装tor和vpn.assets/image-20230314175446206.png)



![image-20230314175534391](kali安装tor和vpn.assets/image-20230314175534391.png)

**下载Hcon**

![image-20230315002232442](kali安装tor和vpn.assets/image-20230315002232442.png)



> tar jxvf HconSTF_v0.5_Prime_Linux_x64.tar.bz2

**解压文件**

![image-20230315002651845](kali安装tor和vpn.assets/image-20230315002651845.png)

**删除安装过的文件包，命令为apt-get autoclean**

**自动卸载没用的软件，命令为：apt-get autoremove**

![image-20230315003235957](kali安装tor和vpn.assets/image-20230315003235957.png)

**系统备份**

**虚拟机使用快照完成备份**