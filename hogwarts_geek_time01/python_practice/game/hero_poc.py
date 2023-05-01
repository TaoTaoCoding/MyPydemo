"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'

"""


def update_hero(hero_list, hero_name):
    for i in hero_list:
        if i.get("name") == hero_name:
            hero_volume = input("请问你要将血量修改为多少？")
            i["volume"] = hero_volume
            return hero_list
    return "没有找到"


def console():
    print("""
    1. **创建英雄**
    2. **查看英雄信息**
    3. **修改英雄信息**
    4. **删除英雄**
    5. **退出系统**
    """)
    hero_list = []
    while True:
        result = input("请输入数字，选择需要完成的操作：")
        if result == "5":
            print("退出系统")
            break
        elif result == "1":
            name = input("请输入英雄的名称：")
            volume = input("请输入英雄的血量：")
            power = input("请输入英雄的攻击力：")
            hero_data = {"name": name, "volume": volume, "power": power}
            hero_list.append(hero_data)
            print(f"创建成功")
        elif result == "2":
            hero_name = input("请输入需要查询的英雄信息：")
            for i in hero_list:
                if i.get("name") == hero_name:
                    print(f"英雄{hero_name}的信息为{i}")
                    break
        elif result == "3":
            hero_name = input("请问你要修改哪个英雄的血量？")
            result_list = update_hero(hero_list, hero_name)
            print(f"更新之1后的结果为{result_list}")
        elif result == "4":
            hero_name = input("请问你要删除哪个英雄？")
            for i in range(len(hero_list)):
                if hero_list[i].get("name") == hero_name:
                    hero_list.pop(i)
                    break
            print(f"删除之后所有的英雄的数据信息为{hero_list}")


if __name__ == '__main__':
    console()
