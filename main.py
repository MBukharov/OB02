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

    # получение имени пользователя
    def get_user_name(self):
        return self.__name

    #Изменение имени пользователя
    def change_user_name(self,name):
        old_name = self.__name
        self.__name = name
        print(f"Имя пользователя {old_name} заменено на {name}")

class Admin(User):
    def __init__(self,name,admin_level):
        super().__init__(name,level='admin')
        self.__admin_level = admin_level
        self.__id = self.__generate_id()

    def __generate_id(self):
        return int("".join(random.choices('0123456789',k=5)))

    #Добавление нового пользователя
    def add_user(self,name):
        u = User(name)
        users.append(u)
        print(f"Новый пользователь ID = {u.get_user_id()} добавлен")

    #удаление пользователя
    def remove_user(self,user_name):
        for i,u in enumerate(users):
            if user_name == u.get_user_name():
                users.pop(i)
                print(f"Пользователь {u.get_user_name} удален")
                break

    #вывод данных об админе
    def admin_info(self):
        print(f"ID: {self.__id}, Имя: {self.__name}, уровень доступа: {self.__level}, уровень админа {self.__admin_level}")

#Тестирование
admin = Admin('Суровый',"Высокий")
admin.admin_info()
#Добавление пользователей
admin.add_user("Вася")
admin.add_user("Анна")
admin.add_user("Коля")
admin.add_user("Рита")

#Вывод данных о пользователях
for u in users: u.user_info()

#Изменение имени пользователя
users[2].change_user_name("Миша")

#Удаление пользователя
admin.remove_user("Вася")