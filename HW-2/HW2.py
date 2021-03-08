my_list_string = str(input('Введите строку символов (цифры, буквы) без пробелов: '))
my_list = list(my_list_string)
length_list = len(my_list)
even = length_list % 2
if even == 0:
    i = 1
    while i <= length_list:
        a = my_list.pop(i)
        my_list.insert(i-1, a)
        i += 2
    print(my_list)
elif even == 1:
    last_element = my_list.pop(length_list - 1)
    i = 1
    while i <= (length_list-1):
        a = my_list.pop(i)
        my_list.insert(i-1, a)
        i += 2
    my_list.append(last_element)
    print(my_list)

    
