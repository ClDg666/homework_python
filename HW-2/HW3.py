winter = [12, 1, 2]
spring = [3,  4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
month = int(input('Введите номер месяца: '))
if (month in winter):
    print('ЗИМА')
elif (month in spring):
    print('ВЕСНА')
elif (month in summer):
    print('ЛЕТО')
elif (month in autumn):
    print('ОСЕНЬ')
else:
    print('Неверно набран месяц')



year = {1 : 'ЗИМА', 2 : 'ЗИМА', 3 : 'ВЕСНА', 4 : 'ВЕСНА', 5 : 'ВЕСНА', 6 : 'ЛЕТО', 7 : 'ЛЕТО', 8 : 'ЛЕТО', +
 + 9 : 'ОСЕНЬ', + + 10 : 'ОСЕНЬ', 11 : 'ОСЕНЬ', 12 : 'ЗИМА'}

print(year.get(month))
