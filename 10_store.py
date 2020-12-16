#!/usr/bin/env python
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

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
print()
# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# РЕШЕНИЕ
table_code = goods['Стол']

table_quantity_N1 = store[table_code][0]['quantity']
table_quantity_N2 = store[table_code][1]['quantity']

table_price_N1 = store[table_code][0]['price']
table_price_N2 = store[table_code][1]['price']

tableN1_cost = table_quantity_N1*table_price_N1
tableN2_cost = table_quantity_N2*table_price_N2
print('на складе', table_quantity_N1, 'шт Столов №1 на общую сумму', tableN1_cost, 'руб' )
print('на складе', table_quantity_N2, 'шт Столов №2 на общую сумму', tableN2_cost, 'руб' )
print()
sofa_code = goods['Диван']

sofa_quantity_N1 = store[sofa_code][0]['quantity']
sofa_quantity_N2 = store[sofa_code][1]['quantity']

sofa_price_N1 = store[sofa_code][0]['price']
sofa_price_N2 = store[sofa_code][1]['price']

sofa_N1_cost = sofa_quantity_N1*sofa_price_N1
sofa_N2_cost = sofa_quantity_N2*sofa_price_N2

print('на складе', sofa_quantity_N1, 'шт Диванов №1 на общую сумму', sofa_N1_cost, 'руб' )
print('на складе', sofa_quantity_N2, 'шт Диванов №2 на общую сумму', sofa_N2_cost, 'руб' )
print()


chair_code = goods['Стул']
chair_quantity_N1 = store[chair_code][0]['quantity']
chair_quantity_N2 = store[chair_code][1]['quantity']
chair_quantity_N3 = store[chair_code][2]['quantity']

chair_price_N1 = store[chair_code][0]['price']
chair_price_N2 = store[chair_code][1]['price']
chair_price_N3 = store[chair_code][2]['price']

chair_N1_cost = chair_quantity_N1*chair_price_N1
chair_N2_cost = chair_quantity_N2*chair_price_N2
chair_N3_cost = chair_quantity_N3*chair_price_N3

print('на складе',chair_quantity_N1, 'шт Стульев №1 на общую сумму', chair_N1_cost, 'руб' )
print('на складе',chair_quantity_N2, 'шт Стульев №2 на общую сумму', chair_N2_cost, 'руб' )
print('на складе',chair_quantity_N3, 'шт Стульев №2 на общую сумму', chair_N3_cost, 'руб' )
print()

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






