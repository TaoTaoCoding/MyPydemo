"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'

1. 实现英雄的添加功能。

```
请输入数字，选择需要完成的操作：1
请输入英雄的名称：jinx
请输入英雄的血量：20
请输入英雄的攻击力：30
创建成功
```

"""
print("""
    1. **创建英雄**
    2. **查看英雄信息**
    3. **修改英雄信息**
    4. **删除英雄**
    5. **退出系统**
""")
# 问题： 按目前的实现，添加功能和查看都是针对的一个英雄。
# 解决方案： 将多个英雄数据保存下来。-> 列表
hero_list = []
while True:
    res = input("请输入对应的选项，即可执行对应的操作：")
    if res == "1":
        hero_name = input("请输入英雄的名称：")
        hero_volume = input("请输入英雄的血量：")
        hero_power = input("请输入英雄的攻击力：")
        hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}
        # 语法 f"123"
        # 语法 f""
        print(f"创建成功！英雄名称为{hero_name} ，英雄的血量为{hero_volume} ，英雄的攻击力为{hero_power}")
        hero_list.append(hero_info)
    # 如果想要实现 查看jinx 的血量，jinx 的所有信息。
    elif res == "2":
        pass

        # 在字符串中，如果用到了引号，符合内单外双， 内双外单的规则
        # print(f"查看英雄{hero_info['name']}对应的血量为{hero_info['volume']}")
    elif res == "3":
        print("修改英雄信息")
    elif res == "4":
        print("删除英雄信息")
    else:
        print("退出系统")
        break

print(f"英雄列表中的所有元素为{hero_list}")