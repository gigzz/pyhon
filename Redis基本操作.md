

# Redis
	Ĭ�϶˿�: 6379
	�����ļ�Ŀ¼: sudo cat /etc/redis/redis.conf
	��־λ��: logfile /var/log/redis/redis-server.log
	Ĭ��16�����ݿ�����0~15
	����: sudo service redis start
	����: redis-cli
	ѡ�����ݿ�: select ���ݿ��� 
# ��windown����ϵͳ
	��������: redis-server --service-install redis.windows.conf --loglevel notice --service-name Redis_new
	��������ȥ����������
	
# ���ݸ�ʽ: 
	�ַ���: string ���512MB ���Դ洢2�����ļ�
	��ϣ: hash
	�б�: list
	����: set
	���򼯺�: zset
	
# ���ݲ���	
	String:
		���ü�: set 'key' 'vaule'(Ҳ���޸ģ����ڵĻ��޸�û�еĻ����)
		���ü�����ʱ��: setex key seconds��λ�� value 
		�鿴��ֵʣ���ʱ��: ttl key
		���ö����: mest key value key value 
		��ȡֵ: get key
		��ȡ���ֵ: mget ket ket
		׷������: append key value
		
	������: 
		���ü�ֵ�Ĺ���ʱ��: expire key seconds
		keys value(֧������)
		�ж�ֵ�Ƿ����: exists ֵ
		�жϼ���Ӧ��ֵ������: type key
		ɾ������Ӧ��ֵ: del key key key key ���Զ��
	
	hash����:
		hash���ڴ洢����
		���: hset ����(����) ���� ֵ 
		��Ӷ��: hmset ����(����) ���� ֵ �������ö������
		��ȡһ��: hget ����(����) ����
		��ȡ���: hmget ����(����) ���� 
		��ȡȫ��: hgetall ����(����)
		��ȡ��������: hkeys ����(����)
		��ȡ���е�����ֵ: hvals ����(����)
		���Ը���: hlen ����(����)
		�ж��Ƿ����: Hexists ���� ����
		ɾ������: Hdel ����(����) ���� ���ԶԸ�
		��������ֵ�ĳ���: hstrlen ����(����) ����
		
	list ����:
		��߲�������: lpush list��(����) value...
		�ұ߲�������: rpush list��(����) value...
		�����ȡ��һ��ֵ: lpop list��(����)
		���ұ�ȡ��һ��ֵ: rpop list��(����)
		λ�ò���: linsert key(����) BEFORE|AFTER pivot valu
		��ȡ��Χ����: lrange list��(����) ��ʼint ����int
		���س���: llen list��(����)
		����������Ӧ��ֵ: lindex list��(����) index
		
	set����:
		���ظ����ݣ�����
		���: sadd key 123 12
		�鿴��������: smembers key
		��ȡ����: scard key
		�󼯺Ͻ���: SINTER key [key ...]
		�󼯺ϲ�: sdiff key []
		�󼯺ϲ�: sunion key [](ȥ��)
		�ж��Ƿ����: sismember key member 
		ɾ��: spop key index
		ɾ��: srem key ֵ
		
	zset����
		�������ظ�����һ��Ȩ��ֵ�Ǹ���������
		���: zadd key 1 'ss' 2 'gg' 3 'c'
		��Χ: zrange ket index index
		����: zcard key
		��ȡȨ�ط�Χ: zcount key 1 4 ���ظ���
		����ĳ��ֵ��Ȩ��: zscore key ss
		
# ��������
	��Ϣ��ʽ:
		����: subscribe ����Ƶ��
			  ���: Reading messages... (press Ctrl-C to quit)
					  1) "subscribe" (��ʾ����)
					  2) "py3"		(�ж�)
					  3) (integer) 1(message)
		
		����: publish Ƶ�� messages
		ȡ������: unsubscribe
		��Ϣ: message
		
��������
	��Ҫ�������ļ��������ļ���Ҫ�޸�Ϊbind ip slaveof ����ip �˿�
	�ǵøĻ����ſ�������ʹ��
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
