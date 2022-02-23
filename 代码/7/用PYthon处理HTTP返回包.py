# # ！/usr/bin/python3
# -*- coding: utf-8 -*-
# 当前项目名称：python_基础教程
# 文件名称： 用PYthon处理HTTP返回包
# 登录用户名： yanshaoyou
# 作者： 闫少友
# 邮件： 2395969839@qq.com
# 电话：17855503800
# 创建时间： 2021/10/12  9:47

# dumps是将dict转化成str格式，loads是将str转化成dict格式。
# dump和load也是类似的功能，只是与文件操作结合起来了,简单的就是需要2个参数json.dump(a, 文件名)
import json
data = {'phone':'18199990000','type':1}
json_str = json.dumps(data)
print(json_str,type(json_str))

data2 = "{'phone':'18199990000','type':1}"
json_str2 = eval(data2)
print(json_str2,type(json_str2))

test_list = [1,2,3,2,3,4]
test_set = set(test_list)
print(test_set,type(test_set),list(test_set))



