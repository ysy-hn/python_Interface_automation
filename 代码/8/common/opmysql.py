# # ！/usr/bin/python3
# -*- coding: utf-8 -*-
# 当前项目名称：python_基础教程
# 文件名称： opmysql
# 登录用户名： yanshaoyou
# 作者： 闫少友
# 邮件： 2395969839@qq.com
# 电话：17855503800
# 创建时间： 2021/11/17  14:13
"""
定义对MYSQL数据库基本操作的封装
1、包括基本的单条语句操作、如删除、修改、更新
2、独立的查询单条、多条数据
3、独立的添加多条数据
"""
import logging,os,pymysql
from public import config


class OperationDbInterface(object):
    """初始化数据库连接"""
    def __init__(self, host_db='本地ip地址', user_db='账号', passwd_db='密码',
                 name_db='数据表名称', port_db=3306, link_type=0):
        """
        :param host_db: 数据库服务主机
        :param user_db: 数据库用户名
        :param passwd_db: 数据库密码
        :param name_db: 数据库名称
        :param port_db: 端口号，整型数据
        :param link_type: 连接类型，用于设置输出数据时元组还是字典，默认0：字典
        :return: 游标
        """
        try:
            if link_type == 0:
                self.conn = pymysql.connect(host=host_db, user=user_db,passwd=passwd_db,
                                          db=name_db, port=port_db, charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)  # 创建数据库连接，返回字典
            else:
                self.conn = pymysql.connect(host=host_db, user=user_db,passwd=passwd_db,
                                          db=name_db, port=port_db, charset='utf8')  # 创建数据库连接，返回元组
            self.cur = self.conn.cursor()
        except pymysql.Error as e:
            print("创建数据库连接失败|MYsql Error %d: %s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=config.src_path + '/log/syserror.log',
                                level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)


    # 定义单条数据操作，包含删除、更新操作
    def op_sql(self, condition):
        """
        :param condition: SQL语句,该通用方法可用来替代updateone,deleteone
        :return: 字典形式
        """
        try:
            self.cur.execute(condition)  # 执行sql语句
            self.conn.commit()  # 提交游标数据
            result = {'code': '0000', 'message': '执行通用操作成功','data': []}
        except pymysql.Error as e:
            self.conn.rollback()  # 执行回滚操作
            result = {'code': '9999', 'message': '执行通用操作异常', 'data': []}
            print("数据库错误|op_sql %d: %s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=config.src_path + '/log/syserror.log',
                                level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result


    # 查询表中单条数据
    def select_one(self, condition):
        """
        :param condition: SQL语言
        :return: 字典形式的单条查询结果
        """
        try:
            rows_affect = self.cur.execute(condition)
            if rows_affect > 0:  # 查询结果返回数据大于0
                results = self.cur.fetchone()  # 获取一条数据
                result = {'code':'0000', 'message':'执行单条查询操作成功', 'data':results}
            else:
                result = {'code':'0000', 'message':'执行单条查询操作成功', 'data':[]}
        except pymysql.Error as e:
            self.conn.rollback()  # 执行回滚操作
            result = {'code': '9999', 'message': '执行通用操作异常', 'data': []}
            print("数据库错误|op_sql %d: %s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=config.src_path + '/log/syserror.log',
                                level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result


    # 查询表中多条数据
    def select_all(self, condition):
        """
        :param condition: SQL语句
        :return: 字典形式的批量查询结果
        """
        try:
            rows_affect = self.cur.execute(condition)
            if rows_affect > 0:  # 查询结果返回数据大于0
                self.cur.scroll(0, mode='absolute')  # 将鼠标光标放回到初始位
                results = self.cur.fetchall()  # 获取游标中所有结果
                result = {'code':'0000', 'message':'执行单条查询操作成功', 'data':results}
            else:
                result = {'code':'0000', 'message':'执行单条查询操作成功', 'data':[]}
        except pymysql.Error as e:
            self.conn.rollback()  # 执行回滚操作
            result = {'code': '9999', 'message': '执行通用操作异常', 'data': []}
            print("数据库错误|op_sql %d: %s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=config.src_path + '/log/syserror.log',
                                level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result


    # 定义表中插入数据操作的方法
    def insert_data(self, condition, params):
        """
        :param condition:insert语句
        :param params: insert数据,列表形式[('3','Tom', '1 year 1 class','6'),('3', 'Jack', '2 year 1 class', '7'),]
        :return: 字典形式的批量插入数据结果
        """
        try:
            results = self.cur.executemany(condition, params)  # 返回插入的数据条数
            self.conn.commit()
            result = {'code': '0000', 'message': '执行单条查询操作成功', 'data': results}
        except pymysql.Error as e:
            self.conn.rollback()  # 执行回滚操作
            result = {'code': '9999', 'message': '执行通用操作异常', 'data': []}
            print("数据库错误|op_sql %d: %s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=config.src_path + '/log/syserror.log',
                                level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result


    # 关闭数据库
    def __del__(self):
        if self.cur != None:
            self.cur.close()  # 关闭游标
        if self.conn != None:
            self.conn.close()  # 释放数据库资源

if __name__ == "__main__":
    test = OperationDbInterface()  # 实例化类
    result_select_all = test.select_all("SELECT * FROM config_total")  # 查询多条数据
    result_select_one = test.select_one("SELECT * FROM config_total WHERE id=1")  # 查询一条数据
    result_op_sql = test.op_sql("update config_total set value_config='test' WHERE id=1")  # 通用操作
    result = test.insert_data("insert into config_total(key_config, value_config, description, status) values(%s, %s, %s, %s)",
                              [('mytest1', 'mytest11', '我的测试1', 1), ('mytest2', 'mytest22', '我的测试2', 0)])  # 插入操作
    print(result_select_all['data'], result_select_all['message'])
    print(result_select_one['data'], result_select_one['message'])
    print(result_op_sql['data'], result_op_sql['message'])
    print(result['data'], result['message'])
    if result['code'] == '0000':
        print(result['data'], result['message'])
    else:
        print(result['message'])
