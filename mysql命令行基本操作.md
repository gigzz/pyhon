
 
 
# ���ݿ�
	�������ݿ�: create database ���ݿ��� charset = utf8;
	ɾ�����ݿ�: drop database ���ݿ���;
	�л����ݿ�: use ���ݿ���;
	��ʾ�������ݿ�: show databases;
	��ʾ��ǰʹ�õ����ݿ�: select database()
	����sqlmy: mysql -h(ip) -P(�˿�) -u(�û���) -p ����س���������
	������ʱȷ����mysql�����user�У������û����룬��Ҫ���޸��û���������Ϊ%���ɡ�
	�鿴�汾��: select version()
	
# ��Ĳ���
	��ʾ���б�: show tables;
	������: create table ���� (
			�ֶ����� ����Դ���� auto_incerement primary key
			name varchar(100) not null default 
			 );
	�鿴��ṹ: desc ����
	ɾ����: drop ����
	�޸ı�: alter table ���� add|change|drop ���� ���ͣ�(ֻ�ܸ������ݵ����Ͳ��ܸ������ݵ�����)
	�޸ı���: rename table ԭ���� to ������;
	�鿴��Ĵ������: show create table ����

# ���ݵĲ���
	���: insert into ���� values()
	ȱʡ���: insert into ����(����) values('','','')
	��Ӷ��: insert into ���� values(),values()
	�޸�: update ���� set ''='',''='' where ''=''
	ɾ��: delete from ���� where '' =''
	�滻: update ���� set �ֶ���=REPLACE (�ֶ���,'ԭ����ֵ','Ҫ�޸ĵ�ֵ')

# ���ݵĲ�ѯ
	��ѯ����: select * from ����
	��ѯ���ȥ���ظ�: select distinct id from ���� where ''=''
	ģ����ѯ: select * from ���� where ''like ''%(%0�������, _ƥ��һ��)
	��Χ��ѯ: select * from ���� where id in(1,3,5)(��ʾ��ѯidΪ1,3,5������)(Ҳ����ʹ��ɾ�����޸�)
			  select * from ���� where id between 3 and 8(��ѯid��3��8��Χ�ڵ�����,����3��8) 	
	�жϿ�: select * from ���� where name is null(��ʾ�û���Ϊ�յ����ݣ��ǿռ���not)	
	�ۺ�: select count(*) from ���� (ֻ��ʾ��ѯ�����˶��ٸ�����,���Լ�as��������������sum(����)(���),		
		  max(����)(���),min(����)(��С),avg(����)(ƽ��ֵ))
	����: select �Ա� count(*) from ���� group by �Ա�(group by �ͺñ�����������һ������������Ա�����Ȼ����where����ÿһ������)
		  ����having�����ٶ�����������ٽ���ɸѡ��select �Ա� count(*) from ���� group by �Ա� having �Ա�='��'(���� count(*)>1)
		  having: �Ƕ�group by����ɸѡ��
		  where: �Ƕ�from����ɸѡ
	����: select * from ���� order by ���� asc(С����)|desc(��С){Ĭ��С�����ж������Ļ��Ƚ���ǰһ���������ٽ��к�һ��������}
	��ҳ: select * from ���� limit start,count;(start��ʾ����һ����ʼ��countȡ���ٸ�)
	��д���Ⱥ�˳��: select * from stude where sex=1 group by sex order by id limit 0,1;
	
	

# ���ݵı��ݺͻָ�
	����: ������Ҫ���볬������Աsudo -s Ȼ�����mysql��Ŀ¼cd/var/lib/mysql Ȼ������mysqldump����mysqldump 
		  -u�û��� -p ��Ҫ���ݵ����ݿ����� > ���ݵ���ȥ(~/Desktop/����.sql) �س���������
	�ָ�: ������Ҫ����һ�����ݿ� Ȼ���˳�myqlִ��mysql -u�û��� -p ���ݿ����� < �����ļ���Ŀ¼Ȼ�����س�
		  ��������
 			 