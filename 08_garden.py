#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# РЕШЕНИЕ
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
# РЕШЕНИЕ
all_together = garden_set|meadow_set
print('все виды цветов:', end=' ')
print(*all_together, sep=',')
print()

# выведите на консоль те, которые растут и там и там
# РЕШЕНИЕ

everywhere_grow = garden_set&meadow_set
print('растут везде:', end = ' ')
print(*everywhere_grow, sep=', ')
print()

# выведите на консоль те, которые растут в саду, но не растут на лугу
# РЕШЕНИЕ
only_in_garden = garden_set-meadow_set
print('растения, которые растут в саду, но не растут на лугу:', end=' ')
print(*only_in_garden, sep=', ')
print()

# выведите на консоль те, которые растут на лугу, но не растут в саду
# РЕШЕНИЕ
only_in_meadow = meadow_set- garden_set
print('растения, которые растут на лугу, но не растут в саду:', end=' ')
print(*only_in_meadow, sep=', ')
print()

