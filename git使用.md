


## git学习
 - 参考https://blog.csdn.net/lemon_cookie/article/details/79058151
 
	- cmd 输入git --version判断是否配置号环境变量
	- 打开gitbash
	- $ git config –global user.name “Yourname”

	- $ git config –global user.email “Youremail@xxx.com

	- 生成ssh-key 如果没有 输入ssh-keygen -t rsa -C “Youremail@xxx.com”连续敲回车3次
	  输完后连敲三个回车，进入用户目录打开.ssh文件，进入会看到生成的 id_rsa 以及 id_rsa.pub，
	  前者是私钥最好不要泄露，后者是公钥可以告诉别人。
	  
	- 打开github
		setting → SSH and GPG keys → New SSH key
		
	- 然后创建自己的仓库new repository ，复制clone or download git@github.com:gigzz/pyhon.git

	- 然后自己的目录运行$ git clone git@github.com:gigzz/pyhon.git

	- git push 从远程服务器下载到本地

	- git add 添加的文件(或者./当前目录的舍友文件)

	- git commit -m '修改信息'(提交)

	- git push origin master(上传到服务器)

	- git log 查看记录

	- git reset 版本 (恢复之前版本，该命令运行后只是将仓库区的内容回至暂存区，HEAD表示当前版本后面加上^表示上一个版本)

	- git checkout 指定哪个文件 (从暂存区中返回之前记录)

	-  多人使用时需要先代码下载下来再上传上去git pull origin master(拉下来), 再上传git push -u origin master(再上传上去)
	
	- 忽略上传可以在.git/info/exclude里添加忽略的文件名
	
	- 添加本地已有的项目
	 ```$xslt	
				git init
	            git add ./
     			git commit -m "update"
     			git remote add origin github地址
     			git push -u origin master

      ```
	

