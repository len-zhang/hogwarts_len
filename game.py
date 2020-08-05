# -*- coding:utf-8 -*-
import random


def game():
    my_hp = 1000
    enemy_hp = 2000
    my_power = random.randint(100, 200)
    enemy_power = random.randint(1, 100)
    game_round = 0
    while True:
        game_round += 1
        print("回合：" + str(game_round))
        my_hp = my_hp - enemy_power
        print("我的当前血量：", my_hp)
        enemy_hp = enemy_hp - my_power
        print("敌人当前血量：", enemy_hp)
        if my_hp <= 0:
            print("我输了")
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break


if __name__ == '__main__':
    game()
