"""
每个操作封装成一个函数
创建英雄：当前游戏中，创建英雄角色，定义好对应英雄的血量及其攻击力。
查看英雄信息：查看当前游戏中所有的英雄信息。
修改英雄信息：修改英雄的血量。
删除英雄：英雄太弱，不需要，删除掉。
退出系统：结束程序
"""


def add_hero(hero_name, hero_volume, hero_power, hero_list):
    hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}
    print(f"创建成功！英雄名称为{hero_name} ，英雄的血量为{hero_volume} ，英雄的攻击力为{hero_power}")
    hero_list.append(hero_info)
    return hero_list


def find_hero(hero_name, hero_list):
    find_hero_info = ""
    for i in hero_list:
        if hero_name == i["name"]:
            print(f"英雄{hero_name}的信息为{i}")
            find_hero_info = i
        else:
            print("英雄不存在")
            find_hero_info ="英雄不存在"
    return find_hero_info


def modify_hero(hero_name, hero_volume, hero_list):
    for i in hero_list:
        if hero_name == i["name"]:
            i["hero_volume"] = hero_volume
            print(f"修改后英雄{hero_name}的信息为{i}")
        else:
            print("英雄不存在")
    return hero_list


def delete_hero(hero_name, hero_list):
    for i in hero_list:
        if hero_name == i["name"]:
            # print(f"英雄{res}的信息为{i}")
            hero_list.remove(i)
            print(f"修改后英雄列表的信息为{hero_list}")
        else:
            print("英雄不存在")
    return hero_list


if __name__ == "__main__":
    hero_list = []
    while True:
        res = input("请输入对应的选项，即可执行对应的操作：")
        if res == "1":
            hero_name = input("请输入英雄的名称：")
            hero_volume = input("请输入英雄的血量：")
            hero_power = input("请输入英雄的攻击力：")
            hero_list = add_hero(hero_name, hero_volume, hero_power, hero_list)
        elif res == "2":
            hero_name = input("请输入英雄的名称：")
            find_hero(hero_name, hero_list)
        elif res == "3":
            hero_name = input("请输入英雄的名称：")
            hero_volume = input("请输入英雄的血量：")
            modify_hero(hero_name, hero_volume, hero_list)
        elif res == "4":
            hero_name = input("请输入英雄的名称：")
            delete_hero(hero_name, hero_list)
        else:
            print("退出系统")
            break
