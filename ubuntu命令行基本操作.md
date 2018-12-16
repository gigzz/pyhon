命令格式
command  options   parameterl
 命令      选项   	-参数

命令 --help（命令的使用帮助）
命令后面加上&后台运行

tree显示目录结构

clear清屏

ctrl+c退出执行

sftp user@192.168.1.11回车输入密码使用put来发送数据，get来获取数据 在进入sftp后使用lls来查看本地的文件

ls 查看当前目录下的文件.
ls -a 查看当前目录下的所有文件（在创建文件时以.开头的文件为隐藏文件）.
ls -h查询出来的文件显示文件大小时显示以k来显示.
ls -l查看文件按行来显示.
ll等于 ls -ahl
（可以组合使用先后顺序不重要例如 ls -ahl）
（后面可以使用正则表达式）
ls > 文件名字（将打印的出来的内容保存到文件）
ls>> 文件名字（将打印出来的内容追加到文件后，文件如果不存在促进啊文件）

cd进入某个文件夹

查看系统架构:dpkg --print-architecture

pwd查看当前文件路径

touch创建当前文件夹下的文件

mkdri创建文件夹（在创建有子文件夹的时候需要加上-p）
rm删除文件（无法删除文件夹时加上-r）
rmdir

cat查看文件内容
gedit编辑文本内容
vi编辑文本内容
more查看大文件（q退出）
ls -alh | more（文件夹下很多文件时使用more来查看比较方便）

cp拷贝文件（如果需要拷贝文件加需要加入-r）

ln -s 原件名 快捷方式的文件名(软连接window的快捷方式一样原文件删除后快捷方式无法使用）
#硬连接 重新复制一份，原文件删除后不影响，
#在linux系统中每个文件都有指向他的引用，
#叫做硬连接数当这个数字为0 时文件会被系统删除
ln 原件名 复制的文件名（硬连接）
mv 原文件名 修改的名字 （重命名）

find ./-name(siz) '需要查找的文件'

tar -cvf 打包后的文件名.tar 需要打包的文件（打包不是压缩包）
tar -xvf 需要解包的名字（解包）
tar -zcvf  压缩后的文件名.tar.-gz 需要压缩的文件（压缩）
tar -jcvf  压缩后的文件名.tar.-bz2 需要压缩的文件（压缩）
zip 压缩后的文件名.zip 需要压缩的文件 需要压缩的文件（压缩）
tar -zxvf需要解压的名字.tar.gz（解压）
tar -jxvf需要解压的名字.tar.bz2（解压）
unzip 需要解压的名字.zip（解压）

（查看进程）
top
ps
hop
ps jax|grep redis 查询进程中是否存在某程序
kill -9 强制删除进程

shutdown -h（init 0）（关机）
reboot（init 6）（重启）

sudo useradd -m 用户名（添加用户，并为其添加目录）
su 切换用户（加上 - 的的话目录一起切换）
添加到用户组  sudo usermod -a -G sudo xxxx
添加到用户组 sudo usermod -a -G adm xxx
sudo userdel（删除用户 加-r的话把目录一起删除）
sudo passwd 用户名 （添加密码或修改密码）
who或(w) 查看当前使用这个用户的人数 

#文件权限(重点)
#文件有3个权限分别是rwx 如果没有权限用-表示，文件有创建者权限 组员权限，和其他人权限
	字母法
		chmod u=wrx,g=r,o=x 文件名称(为文件修改权限 u表示创建者，g表示组员，o表示其他)
	数字法	
		x=1 w=2 r=4
		chmod 346 文件名 （给文件添加创建者写和执行的权限 组员读的操纵，其他读写操作）
		
# 解决
	- ping: 当虚拟机的设置完全正确时，就是无法ping通主机是主机防火墙的问题https://jingyan.baidu.com/article/020278116062961bcd9ce548.html
	- python无法连接，显示超时，有可能是主服务中对3306进行了限制，在防火墙中的高级设置中的入站规则中添加3306为允许连接
 
