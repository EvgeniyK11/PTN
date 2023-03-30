#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника....
from sys import argv
def my_func_1():
    try:
        num = [int(_) for _ in argv[1:]]
        return (num[0]) * num[1]) + num[2]
    except ValueError:
        return "Вы ввели недопустимое значение"
    except IndexError:
        return "Вы ввели недостаточное количество параметров"
print(my_func_1())

# 2. Представлен список чисел......

def my_func_2():
    user_answer = input().split()
    num =[int(_) for _ in user_answer]
    return [a for i, a in enumerate(num) if a > num[i - 1]]
print(my_func_2())

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
def my_func_3():
    return [i for i in range (20,241) if i % 20 == 0 or i % 21 ==0]
print(my_func_3())

# 4. Представлен список чисел.......
my_list = [10, 10, 4, 6, 6, 9, 8]
res = [i for i in my_list if my_list.count(i) == 1]
print(res)

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.....
'''1 вариант'''

from functools import reduce

my_list = [_ for _ in range(100, 1000) if _ % 2 == 0]
print(reduce(lambda x, y: x * y, my_list))

'''2 вариант'''

el = 1
for i in my_list:
    el *= i
print(el)

# 6.  Реализовать два небольших скрипта
from itertools import count, cycle

def my_func():
    l = []
    ex = 0
    for el in count(5):
        if el > 10:
            break
        l.append(el)
    for i in cycle(l):
        if ex > 20:
            break
        ex += 1
        print(i)
my_func()

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.....
def fibo_gen():
    x = 1
    for el in range(1, 16):
        x *= el
        yield x
        
for el in fibo_gen():
    print
