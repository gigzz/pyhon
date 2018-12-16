

# Redis
	默认端口: 6379
	配置文件目录: sudo cat /etc/redis/redis.conf
	日志位置: logfile /var/log/redis/redis-server.log
	默认16个数据库名称0~15
	启动: sudo service redis start
	连接: redis-cli
	选择数据库: select 数据库名 
# 在windown操作系统
	创建服务: redis-server --service-install redis.windows.conf --loglevel notice --service-name Redis_new
	启动服务去服务里启动
	
# 数据格式: 
	字符串: string 最大512MB 可以存储2进制文件
	哈希: hash
	列表: list
	集合: set
	有序集合: zset
	
# 数据操作	
	String:
		设置键: set 'key' 'vaule'(也是修改，存在的话修改没有的话添加)
		设置键过期时间: setex key seconds单位秒 value 
		查看键值剩余的时间: ttl key
		设置多个键: mest key value key value 
		获取值: get key
		获取多个值: mget ket ket
		追加数据: append key value
		
	键命令: 
		设置键值的过期时间: expire key seconds
		keys value(支持正则)
		判断值是否存在: exists 值
		判断键对应的值的类型: type key
		删除键对应的值: del key key key key 可以多个
	
	hash命令:
		hash用于存储对象
		添加: hset 对象(键名) 属性 值 
		添加多个: hmset 对象(键名) 属性 值 可以设置多个属性
		获取一个: hget 对象(键名) 属性
		获取多个: hmget 对象(键名) 属性 
		获取全部: hgetall 对象(键名)
		获取所有属性: hkeys 对象(键名)
		获取所有的属性值: hvals 对象(键名)
		属性个数: hlen 对象(键名)
		判断是否存在: Hexists 对象 属性
		删除属性: Hdel 对象(键名) 属性 可以对个
		返回属性值的长度: hstrlen 对象(键名) 属性
		
	list 命令:
		左边插入数据: lpush list名(键名) value...
		右边插入数据: rpush list名(键名) value...
		从左边取出一个值: lpop list名(键名)
		从右边取出一个值: rpop list名(键名)
		位置插入: linsert key(键名) BEFORE|AFTER pivot valu
		获取范围数据: lrange list名(键名) 开始int 结束int
		返回长度: llen list名(键名)
		返回索引对应的值: lindex list名(键名) index
		
	set命令:
		无重复数据，无序
		添加: sadd key 123 12
		查看所有数据: smembers key
		获取个数: scard key
		求集合交集: SINTER key [key ...]
		求集合并: sdiff key []
		求集合差: sunion key [](去重)
		判断是否存在: sismember key member 
		删除: spop key index
		删除: srem key 值
		
	zset命令
		有序，无重复，有一个权重值是浮点数类型
		添加: zadd key 1 'ss' 2 'gg' 3 'c'
		范围: zrange ket index index
		个数: zcard key
		获取权重范围: zcount key 1 4 返回个数
		返回某个值的权重: zscore key ss
		
# 发布订阅
	消息格式:
		订阅: subscribe 订阅频道
			  结果: Reading messages... (press Ctrl-C to quit)
					  1) "subscribe" (表示订阅)
					  2) "py3"		(判断)
					  3) (integer) 1(message)
		
		发布: publish 频道 messages
		取消订阅: unsubscribe
		消息: message
		
主从设置
	需要改配置文件从配置文件需要修改为bind ip slaveof 主的ip 端口
	记得改回来才可以正常使用
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
