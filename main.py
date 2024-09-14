import random

users = []
class User():
    def __init__(self, name,level = 'user'):
        self.__id = self.__generate_id()
        self.__name = name
        self.__level = level

    #генератор ID
    def __generate_id(self):
        return int("".join(random.choices('0123456789',k=5)))

    #вывод данных о пользователе
    def user_info(self):
        print(f"ID: {self.__id}, Имя: {self.__name}, уровень доступа: {self.__level}")

    #получение id пользователя
    def get_user_id(self):
        return self.__id

    #Изменение имени пользователя
    def set_user_name(self,name):
        self.__name = name

class Admin(User):
    def __init__(self,name,admin_level,level = 'admin'):
        super().__init__(name,level)
        self.__admin_level = admin_level
        self.__d = self.__generate_id()

    def __generate_id(self):
        return super().__generate_id()

    #Добавление нового пользователя
    def add_user(self,name):
        u = User(name)
        users.append(u)
        print(f"Новый пользователь ID = {u.get_user_id()} добавлен")

    #удаление пользователя
    def remove_user(self,user_id):
        for i,u enumerate(users):
            if user_id == u.get_user_id():
                users.pop(i)
                print(f"Пользователь ID = {u.get_user_id} удален")
                break

