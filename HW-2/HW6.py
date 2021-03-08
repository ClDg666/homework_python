products = []
analytic = {}
var_item = []
var_price = []
var_qty = []
var_unit = []

n = int(input('Введите количество товаров для ввода: '))
i = 1
while i <= n:
    pos = int(input(f'Позиция {i}-го товара: '))
    item = str(input(f'Название {i}-го товара: '))
    price = float(input(f'Цена {i}-го товара: '))
    qty = int(input(f'Количество {i}-го товара: '))
    unit = str(input(f'Единицы измереня {i}-го товара: '))
    var = (pos, {"название": item, "цена": price, "количество": qty, "единицы измерения": unit})
    products.append(var)
    i += 1
    var_item.append(item)
    var_price.append(price)
    var_qty.append(qty)
    var_unit.append(unit)
analytic = {"название": var_item, "цена": var_price, "количество": var_qty, "единицы измерения": var_unit}

print (products)
print(analytic)