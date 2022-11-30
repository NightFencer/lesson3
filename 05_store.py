# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

# TODO здесь ваш код
goods_names = []
goods_codes = []
for goods_name,goods_code in goods.items():
    goods_names.append(goods_name)
    goods_codes.append(goods_code)
print(goods_names)
print(goods_codes)


for product in goods_codes:
    count_product = len(store[product])

    i=0
    product_cost = 0
    total_product_quantity =0
    while i <count_product:

        product_price=store[product][i]['price']
        product_quantity = store[product][i]['quantity']
        #print('Art', product,'цена',product_price,'кол-во',product_quantity)
        product_cost = product_cost+product_price*product_quantity
        total_product_quantity = total_product_quantity+product_quantity
        i = i + 1
    current_product= goods_names[(goods_codes.index((product)))]
    # print(current_product)
    # print(total_product_quantity)
    # print(product_cost)
    print(current_product,'количество',total_product_quantity,'шт. общей стоимостью',product_cost,'руб')

print(42*27+510*22+520*32+1200*2+1150*1+5000+95*12+97*43)


