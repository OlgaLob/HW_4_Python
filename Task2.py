#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
def find_mult(num):
    multipliers = []
    div = 2
    while num > 1:
        while num % div == 0:
            multipliers.append(div)
            num //= div
        div += 1
    multipliers1 = list(set(multipliers))
    return  multipliers1

number = int(input('Введите натуральное число: '))
print(f'Список простых множителей числа {number} - {find_mult(number)}')