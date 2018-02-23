# Пример с перехватом ошибки
def get_answer():
    answer = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    question = (input("Скажы что нибуть: ")).lower()
    try:
        assert question in answer
        print(answer[question])
    except AssertionError:
        print("Чтото пошло не так...")

# Попробовал добавить перехвать ctrl-C но не получилось пока...
def get_answer2():
    while True:
        answer = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
        question = (input("Скажы что нибуть: ")).lower()
        try:
            assert question in answer
            print(answer[question])
        except:
            pass
        # except AssertionError:
        #     print("Чтото пошло не так...")

get_answer()