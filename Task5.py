# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.*
# Пример:
#             - 2*x² + 4*x + 5 = 0 
#             - 5*x² + 2*x + 43 = 0
#             - Результат: 7*x^2 + 6*x + 48 = 0

def destr(arg, sign = '+'):
    if 'x' in arg:
        C = int(sign + arg[:arg.index('*')])
        if '^' in arg:
            n = int(arg[arg.index('^') + 1:])
        else:
            n = 1
    else:
        C = int(arg)
        n = 0
    return[n, C]
def parce(file):
    string = file.readline().rstrip()[:-3]
    a, *args = string.split()
    new_args = {destr(a)[0]: destr(a)[1]}
    for i in range(1, len(args), 2):
        new_args[destr(args[i], args[i-1])[0]] = destr(args[i], args[i-1])[1]
    return new_args
with open('file4.txt', 'r') as file4, open('file5.txt', 'r') as file5, open('file7.txt', 'w') as output_file:
    result = parce(file4)
    data2 = parce(file5)
    for i in data2:
        if i in result:
            result[i] += data2[i]
        else:
            result[i] = data2[i]
    result_string = f'{result[max(result)]}*x^{max(result)}'
    del result[max(result)]
    for i in sorted(result, reverse = True):
        if result[i] > 0:
            result_string += '+' + str(result[i])
        elif result[i] < 0:
            result_string += '-' + str(result[i])[1:]
        else:
            continue
        if i > 1:
            result_string += '*x^' + str(i)
        elif i ==1:
            result_string += '*x'
    result_string += ' = 0'
    print(result_string, file = output_file)
