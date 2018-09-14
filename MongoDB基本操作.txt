
# MongoDB 是非关系型数据库

#问题 :
	1. mongodb遇到dbpath (/data/db) does not exist
		因为homebrew将mongodb.conf放在了/usr/local/etc/mongodb.conf这个位置，但是mongod启动时默认查找的/etc/mongodb.conf这个位置，
		而且默认的dbpath是在/data/db这个目录下。以非root用户身份其实是进入不了这个目录的，一定会遇到权限问题。mkdir无法直接创建/data目录，
		一定需要用sudo，但即便用sudo mkdir创建了/data/db目录后也没有解决权限的问题。所以还是不要在这条路上继续越陷越深了。
		我换了个思路想了一下，既然没有数据库所在文件夹，那么给他指定一个就可以了。所以启动时我用了mongod –dbpath myDbPath启动后，一切正常了。
		rails项目也可以正常访问了。
		总的来说就是无法插件数据库，因为没有权限，使用吧mongodb 的数据库放在有权限的位置即可


# 基本操作
	启动服务: sudo service mongod start
	默认端口: 27017
	配置未见目录: /etc/mongod.conf
	进入服务端: mongo
	查看状态: db.stats()
	退出: exit(),ctrl+c
	查看当前数据库: db
	查看所有数据库: show dbs
	切换数据库: use 数据库名
	默认数据库为test之后添加的集合默认放在者数据库中
	添加数据库: 不需要添加只是要use 数据库名.
	删除数据库: db.dropDatabase()
	创建集合(也就是mysql里的表): db.createCollection('集合名'，{capped:true,size:10})后面{}里的表示
								 这个集合最多存放10条数据，超过的将最先加入的删除，使用siez时capped
								 要为true
	显示当前数据库的集合: show collection
	删除一个集合: db.集合名.drop()

# 支持的数据类型: Object ID: ID
					String: 字符串
					Boolean: 布尔值
					Integer: 整数
					Double: 浮点数
					Arrays: 数组或集合
					Object: 嵌套文档（数据）
					Null: 
					Timestamp: 时间戳
					Date: 时间

# 比较运算符
	等于: :
	小于: $lt
	小于等于: $lte
	大于: $gt
	大于等于: $gte
	不等于: $ne
	与: ,  或: $or db.test.find({$or:[{age:$gte:18},{name:'hei'}]})
	支持正则表达式: db.test.find({name:'/^huang/'})huang子开头
	
					

# 文档的基本操作
	插入: db.集合名.insert({name:'gj',age:18})
	查询: db.集合名.find()
			  db.集合.find({age:{$lt:18}})
			  查询支持js函数db.test.find({$where:function(){return this.name==hon}})
			  db.test.find({},{name:1})后面的表示显示数据里面的那个数据，1表示显示，0表示不显示
	排序: db.test.find({}).sort({age:1})1表示顺序，-1表示降序
	统计个数: db.test.find({}).sort({age:1}).count()或db.test.count({age:18}){}里面填写查询条件
	查询满足条件的一条数据: db.集合名.findOne()
	分页: db.test.find().limit(2).skip(2) skip表示跳过几行，limit表示显示几行
	修改数据: db.集合名.update({条件},{改为什么数据},{multi:true})如果不加$set的话这条数据将会
			  改成第二个{}里的数据，且只修改第一条，如果加了multi:true修改全部
	删除数据: db.集合名.remove({条件},{justOne:true})加上justOne后只删除一条
	
# 高级操作聚合
	db.集合名.aggergate([管道:{表达式}])
	分组: db.user.aggregate([
			  {$group:{_id:'$sex',counter(列的名称):{$sum:'$age'}}}
		  ])查询以sex分组后求年龄的和counter中还可以写$avg,$sum,$max,$min,$first,$last
		
	投影: db.user.aggregate([
			  {$project:{name:1,_id:0}}
		  ])只显示name列
	
	筛选: db.user.aggregate([
			  {$match:{age:18}}
		  ])筛选age为18的数据和find()类似
		  
	排序: db.user.aggregate([
			  {$sort:{age:1}}
		  ])排序安装age来排序wei1时升序，-1降序。
	
	分页: db.user.aggregate([
			  {$limit:3}
		  ])显示几条数据。
	
	跳过: db.user.aggregate([
			  {$skip:3}
		  ])跳过几条数据
		  
	拆分: unwind 9:03	
	
	这些操作可以一起使用每一个管道可以得到数据在为下一个管道提供数据先后顺序需要注意，$skip需要放在limit上面

	索引: 创建:db.集合名.ensuerIndex({name:1,....}); 
		  性能监测: db.find.find({name:'test1000'}).explain('executionStats');
		  删除: db.集合名.dropIndexes(索引名)
		  获取: db.集合名.getIndexes()

# 安全 
	角色 -- 用户 -- 数据库
		角色：root(超级管理员)，Read(读取某个数据库),readWrite(读写某个数据库)
	创建: db.createUser({user:'admin',pwd:'123456',roles:[{role:'root',db:'admin'}]});
		  db.createUser({user:'zheng',pwd:'19910623',roles:[{role:'readWrite',db:'test'}]})
		  然后需要在配置文件中修改登入方式 
			security:
				authorization: enabled

	登入: mongo -u admin -p 123456 --authenticationDatabase admin

# 副本操作
	下载安装xshell经常多服务器的部署，ssh ip地址连接
	创建并启动: mongod --bind_ip 192.168.50.129 --port 27018 --dbpath ~/Desktop/ti --replSet zheng
	连接服务: mongo --host ip --port 27018
		启动两个服务端后再主服务端运行rs.initiate() 然后添加从服务器rs.add('地址:端口') rs.status()查看状态
		后再'主'服务上添加数据，'从'服务器会复制一份从服务器需要运行rs.slaveOk()
	删除一个'从': rs.remove('地址:端口')
	主从切换: 把主服务器关闭，然后需要重启才可以切换。
	
恢复和备份
	备份: mongodump -h 'ip' -p 'port' -o dbdirectory(位置) 0:输出 -d '数据库名'
			如果开了认证: mongodump -uadmin -p123456 --authenticationDatabase admin -d test -o ~/Desktop/db/
	恢复: mongorestore -h 地址 -d 数据库名 --dir 地址
			如果开了认证: mongorestore -u admin -p123456 --authenticationDatabase admin -dtest1 --dir ~/Desktop/db/test/

	
		

	
	
	

