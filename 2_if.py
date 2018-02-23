def inputs():
    first = input("введите первое слово:")
    second = str(input("повтори или напиши еще что нибуть:"))
    if first == second:
        print("1")
    elif first != second:
        if second == "learn":
            print("3")
        else:
            print("2")


def inputs2():
    first = input("введите первое слово:")
    second = str(input("повтори или напиши еще что нибуть:"))
    if first != second and second == "learn":
        print("3")
    elif first == second:
        print("1")
    else:
        print('2')

inputs()
inputs2()