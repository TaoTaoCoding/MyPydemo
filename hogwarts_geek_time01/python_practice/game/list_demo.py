"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# 定义一个列表
students = []
print(students)
# 列表的追加
students.append("张三")
print(students)
students.append("李四")
students.append("王五")
# [] 计算机所有的计算方式都是从0开始
# 删除操作，要求传入列表的索引。
students.pop(0)
# 删除操作，可以传入列表的具体的值
students.remove("王五")
print(students)

# for 临时变量 in 列表
for i in students:
    print(i)