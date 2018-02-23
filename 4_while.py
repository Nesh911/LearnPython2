# Задание 1 - найти Валеру используя в цикле метод list.pop()
# В итоге при каждом цикле удаляется последнее имя из списска пока не удалится Валера
def find_valera():
    names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    while True:
        for i in names:
            if i == "Валера":
                print('Валера! настало твое время!')
                names.pop()
            else:
                break


# Задание 2 - Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
def find_person(name):
    names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    while True:
        for i in names:
            if i == name:
                print(name + '! настало твое время!')
                names.pop()
            else:
                break


# Задание 3 - Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”,
# пока он не ответит “Хорошо”
# def ask_user():
#     inquiry = input("Как дела?  ").lower()
#     while True:
#         if inquiry == "хорошо":
#             print('A... Ну пока!')
#             break
#         else:
#             return ask_user()


# Задание 4
answer = {"привет": "И тебе привет!",
          "как дела": "Лучше всех",
          "пока": "Увидимся"}

def get_answer(inquiry, answers):
    return answers.get(inquiry)

def ask_user2(answer):
    while True:
        inquiry = input("Как дела?  ")
        result = get_answer(inquiry, answer)
        print(result)
        if inquiry == "Пока":
            print("ok")
            break


#
# find_valera()
# find_person(input('Введите имя: '))
# ask_user()
ask_user2(answer)
