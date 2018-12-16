
 
 
# 数据库
	创建数据库: create database 数据库名 charset = utf8;
	删除数据库: drop database 数据库名;
	切换数据库: use 数据库名;
	显示所有数据库: show databases;
	显示当前使用的数据库: select database()
	连接sqlmy: mysql -h(ip) -P(端口) -u(用户名) -p 点击回车输入密码
	在连接时确保在mysql数库的user中，允许用户登入，主要是修改用户的主机号为%即可。
	查看版本号: select version()
	
# 表的操作
	显示所有表: show tables;
	创建表: create table 表名 (
			字段名称 数据源类型 auto_incerement primary key
			name varchar(100) not null default 
			 );
	查看表结构: desc 表名
	删除表: drop 表名
	修改表: alter table 表名 add|change|drop 列名 类型；(只能更改数据的类型不能更改数据的名字)
	修改表名: rename table 原名字 to 新名字;
	查看表的创建语句: show create table 表名

# 数据的操作
	添加: insert into 表名 values()
	缺省添加: insert into 表名(列名) values('','','')
	添加多个: insert into 表名 values(),values()
	修改: update 表名 set ''='',''='' where ''=''
	删除: delete from 表名 where '' =''
	替换: update 表名 set 字段名=REPLACE (字段名,'原来的值','要修改的值')

# 数据的查询
	查询所有: select * from 表名
	查询结果去除重复: select distinct id from 表名 where ''=''
	模糊查询: select * from 表名 where ''like ''%(%0个到多个, _匹配一个)
	范围查询: select * from 表名 where id in(1,3,5)(表示查询id为1,3,5的数据)(也可以使用删除和修改)
			  select * from 表名 where id between 3 and 8(查询id在3到8范围内的数据,包括3和8) 	
	判断空: select * from 表名 where name is null(表示用户名为空的数据，非空加上not)	
	聚合: select count(*) from 表名 (只显示查询出来了多少个数据,可以加as来重命名，还有sum(列名)(求和),		
		  max(列名)(最大),min(列名)(最小),avg(列名)(平均值))
	分组: select 性别 count(*) from 表名 group by 性别(group by 就好比重新生成了一个表这个表按照性别来分然后再where进行每一组的求和)
		  加上having就是再多分组后的数据再进行筛选，select 性别 count(*) from 表名 group by 性别 having 性别='男'(或者 count(*)>1)
		  having: 是对group by进行筛选，
		  where: 是对from进行筛选
	排序: select * from 表名 order by 列名 asc(小到大)|desc(大到小){默认小到大，有多个排序的画先进行前一个的排序，再进行后一给的排序}
	分页: select * from 表名 limit start,count;(start表示从哪一个开始，count取多少个)
	书写的先后顺序: select * from stude where sex=1 group by sex order by id limit 0,1;
	
	

# 数据的备份和恢复
	备份: 首先休要进入超级管理员sudo -s 然后进入mysql的目录cd/var/lib/mysql 然后运行mysqldump命令mysqldump 
		  -u用户名 -p 需要备份的数据库名称 > 备份到哪去(~/Desktop/名称.sql) 回车输入密码
	恢复: 首先需要创建一个数据库 然后退出myql执行mysql -u用户名 -p 数据库名称 < 备份文件的目录然后点击回车
		  输入密码
 			 