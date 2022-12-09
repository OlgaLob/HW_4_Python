#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
from random import randint
rand_list=[]

n = random.randint(1, 11)
for i in range(n):
    rand_list.append(random.randint(1, 11))
print(rand_list)
rand_list_new = [x for i, x in enumerate(rand_list) if i != rand_list.index(x)]
list_new = list(set(rand_list) ^ set(rand_list_new)) # set(nums)^set(new_nums) 'Исключающее или' Возвращает значение, которое не встречаются в двух множествах одновременно
print(list_new)