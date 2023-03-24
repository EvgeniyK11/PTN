# 1. Создать список и заполнить его элементами различных типов данных......
type_list = ["cat", 1, (2,), [1,2], 3.1, False, frozenset("1"), set ("1")]
for el in type_list:
    print(type (el))

# 2.Для списка реализовать обмен значений соседних элементов......
my_list =list(int("введите значения: "). split (" "))
my_list = list(int("введите значения: "). split ())
    new_list = []
    for i in range(0, len (my_list), 2):
        next_i = i + 2
        a = my_list [i:next_i]
        a.reverse()
        new_list.extend(a)
        print(new_list)

# 3.Пользователь вводит месяц в виде целого числа от 1 до 12......
my_list = list(input("Введите значение : ").split())
for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list
    print(my_list)
#3...
seaso = {
    "winter": [12,1,2],
    "spring": [3,4,5],
    "summer": [6,7,8],
    "autum": [9,10,11]
}
month = int(input("Введите номер месяца"))
for key, value in season.items():
    if month in value:
        print(key)
        break
    else:
        print("Not a month")

# 4.Пользователь вводит строку из нескольких слов, разделённых пробелами...
my_list = input("Enter number").split("")
my_list = input("Enter number").split()
for i, el in enumerate(my_list, 1):
    print(i, el [0:10])

# 5. . Реализовать структуру «Рейтинг»....
my_list = [7, 5, 3, 3, 2]
a = False
while not a:
    try:
        new_score = int(input("New score is:"))
        if new_score < 0:
            print("Должно быть положительное число")
            continue
        if new_score > max(my_list):
            my_list.insert(0, new_score)
            break
        if new_score < min(my_list)
            my_list.append(new_score)
            break
        for i, el in enumerate(my_list):
            if my_list[-1] == new_score:
                my_list.append(new_score)
                a = True
                break
            if el == new_score and el != my_list[i+1]:
                my_list.insert(i+1, new_score)
                a = True
                break
    except ValueError:
        print("Долно быть положительное число")
    print(f"Измененный список {my_list}")

# 6. * Реализовать структуру данных «Товары»......
goods = []
analytics = {"name" : [],
             'price': [],
             "quantiny" : [],
             "unit" : []}
num = 1
while True:
    name = input("Введите название товара:")
    price = int (input("Введите цену товара:"))
    quantity = int(input("Введите количество товара:"))
    unit = input("Введите единицу измерения товара:")
    params = {
        "name": name,
        "price":price,
        "qiantity" : quantity,
        "unit": unit
    }
    good = (num,params)
    goods.append(good)
    for key, value in params.items():
        i = analytics.get(key)
        if value in i:
            continue
        i.append(value)
        continue
    num+=1
    exit_answer = input("Ввести ещё позицию?").lower()
    if exit_answer == "нет":
        break
    print(analytics)
    
