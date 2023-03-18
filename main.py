#. Поработайте с переменными....
var_one = str(input("Ваше имя"))
print(var_one)

var_two = int(input("Ваш возраст"))
print(var_two)

#2. Пользователь вводит время в секундах.
time = int(input("Время в секундах : "))
hours = time //3600
minutes = (time - hours * 3600) // 60
second = (time - hours * 3600) - minutes *60
print(f'{hours} : {minutes} : {second}')

#3 . Узнайте у пользователя число n.
n = int(input("Write a number: "))
print(n+int(str(n)*2)+int(str(n)*3))

#4. 4. Пользователь вводит целое положительное число....
n=int(input("write a number"))
max=n % 10
while True:
    n=n//10
    if n % 10 > max:
        max = n % 10
    elif n > 9:
        continue
    else:
        print(f"Максимальное число: {max}")
        break

#5.Запросите у пользователя значения выручки и издержек фирмы. + 6. Если фирма отработала с прибылью, вычислите рентабельность выручки +
revenue = int("Укажите сумму выручки: ")
costs = int("Укажите сумму издержек: ")
if  revenue > costs:
    profit= revenue - costs
    staff = int(input("Число сотрудников в компании"))
    print("Прибыль фирмы в рассчете на одного сотрудника составит: {} рублей".format(profit/staff))
elif revenue < costs:
    print("Сумма издержек превышает доход")
elif revenue==costs:
    print("Сумма издержек равна доходу")

#7. Спортсмен занимается ежедневными пробежками....
a = int(input("Сколько км пробежал спортсмен в первый день?: "))
b = int(input("Введите общий результат"))
day=1
while a < b:
    a +=a*0.1
    day +=1
print(f'На {day}-й день спортсмен достиг результата - не менее {b} км')