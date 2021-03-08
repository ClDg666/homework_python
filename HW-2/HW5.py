my_list = [7, 5, 3, 3, 2]
rating = int(input('Ввод рейтинга: '))
length_list = len(my_list)
i = 0
while i < (length_list):
    a = my_list[i]
    last_el = my_list[length_list-1]
    if (rating > a):                        # самое большое число - записать в список
        my_list.insert(i, rating)
        break
    elif (rating < last_el):
        my_list.append(rating)              # самое мальенькое число - записать в список
        break
    elif (rating < a):                      # перебираем далее
        i += 1
    elif (rating == a):                     # перебираем далее
        i += 1
print(my_list)
