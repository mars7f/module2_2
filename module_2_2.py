first = int(input('Введите первое число:'))
print(first)
second = int(input('Введите второе число:'))
print(second)
third = int(input('Введите третье число:'))
print(third)
if first == second == third:                                 # Условие, при котором все числа равны
    print(3)                                                   # Вывод  "3"
elif first ==second or first == third or second == third:    # Условие равенства двух из трех чисел
    print(2)                                                   # Вывод  "2"
else:                                                        # Условие, если равных чисел нет
    print(0)                                                   # Вывод  "0"

# elif first != second != third:       # Возможно и такое условие
    # print(0)

