#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

# Есть словарь координат городов

sities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {} #словарь с растояниями м-ду городами пока пустой
#РЕШЕНИЕ
moscow = sities['Moscow'] #вводим переменную moscow - координаты Москвы из словоря sities
london = sities['London'] #вводим переменную london - координаты Лондона из словоря sities
paris = sities ['Paris']  #вводим переменную paris - координаты Парижа из словоря sities

moscow_london = ((moscow[0]-london[0])**2+(moscow[1]-london[1])**2)**0.5 #расстояние Москва-Лондон
moscow_paris = ((moscow[0]-paris[0])**2+(moscow[1]-paris[1])**2)**0.5   #расстояние Москва-Париж

distances['Moscow'] = {} #В словарь distances под ключ Moscow задается пуcтой словарь
distances['Moscow']['London'] = moscow_london #В словарь Moscow (кот. внутри сл-ря distances) Под ключ Лондон задается раст. Москва-Лондон
distances['Moscow']['Paris'] = moscow_paris #В словарь Moscow (кот. внутри сл-ря distances) Под ключ Париж задается раст. Москва-Париж

london_paris = ((london[0]-paris[0])**2+(london[1]-paris[1])**2)**0.5 #Расстояние Лондон-Париж
london_moscow = moscow_london #Расстояние Лондон-Москва (то же что и Москва-Лондон)

distances['London'] = {} #В словарь distances под ключ London задается пуcтой словарь
distances['London']['Paris'] =london_paris #В словарь London (кот. внутри сл-ря distances) Под ключ Париж задается раст. Лондон-Париж;
distances['London']['Moscow'] = london_moscow #В словарь London (кот. внутри сл-ря distances) Под ключ Москва задается раст. Лондон-Москва

paris_london = london_paris #Расстояние до Парижу уже посчитано
paris_moscow = moscow_paris

distances['Paris'] = {} #В словарь distances под ключ Paris задается пуcтой словарь
distances['Paris']['London'] =paris_london #В словарь Paris (кот. внутри сл-ря distances) Под ключ Лондон задается раст. Париж-Лондон;
distances['Paris']['Moscow'] = paris_moscow #В словарь Paris (кот. внутри сл-ря distances) Под ключ Москва задается раст. Париж-Москва




# TODO здесь заполнение словаря

pprint(distances)




