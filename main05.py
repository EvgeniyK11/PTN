# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем
with open('new_file.txt', 'a') as file:
    while True:
@@ -9,13 +8,6 @@
        if not user_answ:
            break
# Со 2 по 6 задание
@@ -24,10 +16,9 @@ def count_info():
    try:
        with open('new_file.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            print(f'Количество строк в файле {len(my_list)}')
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                print(f'В {i + 1}-ой строке {len(new_l)} слов(а)')
                print(f'Количество строк в файле {len(my_list)}. В {i + 1}-ой строке {len(new_l)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'

@@ -76,12 +67,12 @@ def rewrite_file():
    new_text = []
    try:
        with open('file.txt', 'r+', encoding="utf-8") as file:
            l = file.readlines()
            for i in l:
                i = i.split(' ', 1)
                new_text.append(num[i[0]] + ' ' + i[1])
        with open('one_file.txt', 'r+', encoding="utf-8") as new_file:
            new_file.writelines(new_text)
            with open('new_file.txt', 'r+', encoding="utf-8") as new_file:
                l = file.readlines()
                for i in l:
                    i = i.split(' ', 1)
                    new_text.append(num[i[0]] + ' ' + i[1])
                new_file.writelines(new_text)
    except FileNotFoundError:
        return 'Файл не найден.'

@@ -119,16 +110,17 @@ def count_subjects():
            for line in fobj:
                name, stats = line.split(':')  # name = Информатика, stats = 100(л) 50(пр) 20(лаб).
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                """1. [i for i in stats if i == ' ' or ('0' <= i <= '9')] - Перебирает все элементы и берет только цифры и пробелы(для разделения цифр: [' ', '1', '0', '0', ' ', '5', '0', ' ', '2', 
                 '0']) 
                """1. [i for i in stats if i == ' ' or ('0' <= i <= '9')] - Перебирает все элементы и берет только цифры
                        и пробелы(для разделения цифр: [' ', '1', '0', '0', ' ', '5', '0', ' ', '2', '0'])
                 2. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]) с помощью join объединяет
                 получившееся: _100_50_20  (где _ это пробел)
                 2. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]) с помощью join объединяет
                        получившееся: _100_50_20  (где _ это пробел)
                 3. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split() - делит по пробелам методом .split(): ['100', '50', '20']
                 3. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()
                        - делит по пробелам методом .split(): ['100', '50', '20']
                 4. map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split())
                 - с помощью map(int, ['100', '50', '20']) приводит все элементы списка к типу int
                 4. map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split())
                        - с помощью map(int, ['100', '50', '20']) приводит все элементы списка к типу int
                 5. с помощью sum(['100', '50', '20']) суммирует все элементы списка """
                mydict[name] = name_sum
            print(f"{mydict}")  # вывод:{'Информатика': 170}
    except FileNotFoundError:
    return 'Файл не найден.'
    count_subjet()
"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме@""

mport json
def get_statistics():
    try:
        with open('file.txt', 'r+', encoding='utf-8') as file:
            statistics = []
            profit = {}
            average_profit = {}
            av = 0
            prof = 0
            i = 3
            for line in file:
                name, firm, earning, damage = line.split()
                total = int(earning) - int(damage)
                if total >= 0:
                    prof = prof + total
                else:
                    i -= 1
                profit[name] = total
            statistics.append(profit)
            if i != 0:
                (av) = prof / i
                average_profit['average_profit'] = round(av)
                statistics.append(average_profit)
            else:
                print('Все компании работают в убыток')
            print(statistics)
        with open('file.json', 'a+', encoding='utf-8') as json_file:
            json.dump(statistics, json_file)
    except FileNotFoundError:
        return 'Файл не найден.'
get_statistics()