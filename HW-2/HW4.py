string = input('Введите предложение: ')
list_string = string.split(' ')
length_string = len(list_string)
n = 1
for word in list_string:
    # for n in length_string:
        print(str(n) + ' ' + word[:10])
        n += 1