#1. Реализовать функцию, принимающую два числа....
def division (arg):
    try:
        dividend, divider = [int(_) for _ in arg]
        return f' {dividend / divider:.2f}'
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        print("Не хватает значения")
print(division(input("Введите делимое и делитель: ").split()))

#2.Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:

def funk_1(**kwargs):
    print("".join(str(i)for i in kwargs.values()))
funk_1(name="Tor", surnema="Loki", birth_year="1111", city="Asgard", email="tor@mail.ru", tel="01234")

#3. Реализовать функцию my_func(),.......
def my_func(arg_1,arg_2,arg_3):
    arr = [arg_1,arg_2,arg_3]
    a = list(filter(lambda x:x !=,max(arr),arr))
    return max(arr) + max(a)
print(my_func(9,8,45))

#4. Программа принимает действительное положительное число x и целое отрицательное число y......
def my_func(x,y):
    i=x
    for _ in range(abs(y) - 1):
        x *=i
    return 1/x
print (my_func(2, -4))

#5.Программа запрашивает у пользователя строку чисел, разделённых пробелом.......

def my_func():
    total =0
    a = False
    while not a:
        user_num = imput("Введите числа или нажмите q для выхода").split()
        result=0
        for i in range(lem(user_num)):
            if user_num[i] =="q":
                a = True
                break
            else:
                result += int(user_num[i])
        total +=result
        print(total)
my_func()

#6+76. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой..//
def int_func():
    word = input("Введите слова")
    return word.title()
print(int_func())
