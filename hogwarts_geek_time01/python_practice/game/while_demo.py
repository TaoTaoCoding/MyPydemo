"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# while 判断条件:
#       如果为真，则一直执行代码块内的内容
#       如果为假，则不会执行代码块里面的内容
# while True:
#     # 需要被重复执行的代码加一个缩进
#     # ctrl + D 复制当前行代码
#     print("菠萝蜜")
#     # 问题： 死循环。给出中止条件
#     break

count = 0
while count<5:
    # print(count)
    # 自增
    count = count+1
    if count == 4:
        continue
    print(count)
