import os
import random
import Global
from User import User


def clear_console():
    os.system('cls')


def menu2():
    pass


def menu1():
    print("Главное меню:")
    print("\t1) Войти в пользователя")
    print("\t2) Создать пользователя")


if __name__ == '__main__':
    Global.clients.append(User(random.randint(0, len(Global.users))))
    Global.clients.append(User(random.randint(0, len(Global.users))))
    while 1:
        print("Главное меню:")
        print("\t1) Войти в пользователя")
        print("\t2) Создать пользователя")
        c = int(input())
        clear_console()
        match c:
            case 1:
                print("\nДоступные пользователи:")
                users = ""
                for user in Global.clients:
                    users += "[" + user.__str__() + "]"
                print(users)
                print("Введите номер пользователя:")
                num = input()
                print(num)
