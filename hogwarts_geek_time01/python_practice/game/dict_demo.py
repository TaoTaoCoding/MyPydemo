"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""


# 创建

hero = {"key": "value"}
jinx = {"name": "jinx",
        "power": 100}
# 变量名["key"] -》 返回对应的value
print(jinx["name"])

# 如果字典中没有这个元素，那么就会直接添加
jinx["volume"] = 200
print(jinx)
# 如果字典有这个元素，则会修改对应的值。
jinx["power"] = 10
print(jinx)

# KeyError: 'name1'， 为了解决抛异常的问题
print(jinx.get("name1", "不存在"))
print(jinx.get("name"))
