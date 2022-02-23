# # ！/usr/bin/python3
# -*- coding: utf-8 -*-
# 当前项目名称：python_基础教程
# 文件名称： 用python操作MYsql数据库
# 登录用户名： yanshaoyou
# 作者： 闫少友
# 邮件： 2395969839@qq.com
# 电话：17855503800
# 创建时间： 2021/10/12  9:46
# MYSQl基础语法
# 1、增加数据：insert into table1(field1, field2) values(value1, value2)
# 2、删除数据：delete from table1 where 范围
# 3、修改数据：update table1 set field1=value1 where 范围
# 4、查询数据：select * from table1 where 范围
# 5、嵌套数据：select * from table1 where id in (select id from table2)
# 6、清空表数据：TRUNCATE TABLE table1

# 1、插入单条数据
# INSERT INTO 'config_total'('key_config', 'value_config', 'description',
#                            'status') VALUES('test', 'value_test', '测试配置', '1')
# # table:表的意思；value：值的意思

# 2、插入多条数据
# INSERT INTO 'config_total'('key_config', 'value_config', 'description',
#                            'status') VALUES[('mytest1', 'mytest11', '我的测试1', 1),
#                                       ('mytest2', 'mytest22', '我的测试2', 0)]

# 3、结合python以参数化插入单条数据
# INSERT INTO 'config_total'('key_config', 'value_config', 'description',
#                            'status') VALUES(%s, %s, %s, %s), %(param1,param2,param3,param4)

# 4、删除数据（一般不用，都是逻辑删除，即修改状态
# DELETE FROM 'config_total' WHERE 'key_config'='test' AND 'status'='1'

# 5、修改数据
# UPDATE 'config_total' SET 'value_config'='config1' WHERE 'key_config'='test' AND 'status'='1'

# 6、结合python参数化修改数据
# "UPDATE config_total SET key_config='%s', value_config='%s', value_config='%s' WHERE id=%s"
# %(param1,param2,param3,param4)

# 7、查询所有数据
# SELECT * FROM 'config_total1'
#
# 8、查询符合指定条件数据的所有字段值
# SELECT * FROM 'config_total' WHERE 'key_config'='test'

# 9、查询符合指定条件数据的指定字段值
# SELECT 'key_config', 'value_config' FROM 'config_total' WHERE 'key_config'='test'

# 10、结合python参数化查询数据
# "SELECT * from case_interface where id_task=%s and case_status=1" %id_task

# 11、结合python参数化嵌套查询数据
# "SELECT id_module,desc_case FROM case_module where id_module in (SELECT id
# from module where status_module=1 and name_module='%s')" %name_module

# 12、清空表数据：
# TRUNCATE TABLE 'config_total'