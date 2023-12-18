import random
import pprint

users = ["admin", "user1", "user2", "user3"]
objects = ["file1", "file2", "file3", "file4"]
actions = ["read", "write", "access denied"]

user_dict = {
    'admin': [{obj: "full access" for obj in objects}],
    'user1': [{obj: random.choice(actions) for obj in objects}],
    'user2': [{obj: random.choice(actions) for obj in objects}],
    'user3': [{obj: random.choice(actions) for obj in objects}]
}

pprint.pprint(user_dict)
command= 0

while True:
    user_id = input("Введите идентификатор пользователя: ")
    if user_id in users:
        print(f"Пользователь {user_id} вошел в систему.")
        print("Матрица доступа:")
        pprint.pprint(user_dict[user_id])

        while True:
            command = input("Введите команду (1.Открыть файл; 2.Редактировать таблицу доступа; 3.Смена аккаунта; 4.Выход из системы): ")

            if command == "1":
                object_name = input("С каким файлом будем работать? ")
                action = input("Что будем делать? Чтение/Запись: ")
                if user_dict[user_id][0][object_name] == action or user_id == 'admin':
                    print("Успешно")
                else:
                    print("Нет доступа")

            elif command == "2":
                if user_id == "admin":
                    user_name = input("Введите имя пользователя для редактирования: ")
                    print("Матрица доступа для этого пользователя:")
                    pprint.pprint(user_dict.get(user_name))

                    object_name = input("Введите объект для редактирования: ")
                    action_name = input("Введите действие")
                    user_dict[user_name][0][object_name] = action_name
                else:
                    print("Редактировать таблицу может только администратор!")
            elif command == "3":
                break
            elif command == "4":
                print("Выход из системы.")
                break

            elif command == "5":
                pprint.pprint(user_dict)
            else:
                print("Некорректная команда. Повторите ввод.")
        if command == "4":
            break
    else:
        print("Ошибка идентификации. Пользователь не найден.")





