# Задание - 1.Ввести строку
#           2.Вывести эту же строку вертикально: по одному символу на строку консоли.
string = input()

for score in string:
    print(score)


# Задание - Вывести на экран каждое из списка число, увеличенное на 1.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list1:
    j = i+1
    print(j)


# Задание - 1. Получить средний бал по школе
#           2. Получить средний бал в классе
# p.s. Кажется не по той дорожке я пошел...
school = [{'school_class': '4a', 'scores': [3,4,4,5,5,3,5,4,5,5,5]},
          {'school_class': '4b', 'scores': [4,5,2,3,4,4,5,3,5,3,4]}]

groups = [school[0],school[1]]
a = sum(groups[0]["scores"]) + sum(groups[1]["scores"])
b = len(groups[0]["scores"]) + len(groups[1]["scores"])
print('Средний бал по школе ' + str(a/b))
for i in groups:
    print('Средний бал в ' + i['school_class'] + ' классе ' + str(sum(i['scores'])/len(i['scores'])))
