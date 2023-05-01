"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'

1. 实现英雄的删除功能。
1. 如果被删除的英雄不存在，则给出提示信息。
1. 函数

```
请问你要删除哪个英雄？ez
删除之后所有的英雄的数据信息为[{'name': 'jinx', 'volume': '20', 'power': '30'}]
```
"""
print("""
    1. **创建英雄**
    2. **查看英雄信息**
    3. **修改英雄信息**
    4. **删除英雄**
    5. **退出系统**
""")


def delete_hero(hero_list, hero_name):
    """
    :param hero_list:  英雄列表信息
    :param hero_name:  英雄的名字
    :return:
    """
    for i in hero_list:
        # 直到匹配到被删除的英雄
        # if 要查询的英雄名字 == 遍历的每个英雄的名字
        if hero_name == i["name"]:
            # print(f"英雄{res}的信息为{i}")
            hero_list.remove(i)
            # 如果找到了，则修改标志位
            print(f"删除之后所有的英雄的数据信息为{hero_list}")
            return hero_list
    print("没有找到要删除的英雄")
    return hero_list

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
        print(f"创建成功！英雄名称为{hero_name} ，英雄的血量为{hero_volume} ，英雄的攻击力为{hero_power}")
        hero_list.append(hero_info)
    elif res == "2":
        res = input("请输入需要查询的英雄信息：")
        # 遍历所有的英雄信息，
        for i in hero_list:
            # 直到匹配到被查询的英雄
            # if 要查询的英雄名字 == 遍历的每个英雄的名字
            if res == i["name"]:
                print(f"英雄{res}的信息为{i}")
    elif res == "3":
        print("更新英雄信息")

    elif res == "4":
        # ==== 没有使用函数的实现
        # res = input("请输入需要删除的英雄信息：")
        # # ["a", "b", "c"]
        # # 遍历完所有的列表元素， **发现没有要删除的信息**，就提示被删除的英雄不存在。
        # is_find = False
        # for i in hero_list:
        #     # 直到匹配到被删除的英雄
        #     # if 要查询的英雄名字 == 遍历的每个英雄的名字
        #     if res == i["name"]:
        #         # print(f"英雄{res}的信息为{i}")
        #         hero_list.remove(i)
        #         # 如果找到了，则修改标志位
        #         is_find = True
        # # 如果 is_find 为False，代表，遍历完所有元素依然没有找到。
        # if is_find == False:
        #     print("没有找到要删除的英雄")
        # else:
        #     print(f"删除之后所有的英雄的数据信息为{hero_list}")
    # 使用函数的实现
        res = input("请输入需要删除的英雄信息：")
        delete_hero(hero_list, res)
    else:
        print("退出系统")
        break

print(f"英雄列表中的所有元素为{hero_list}")