#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# РЕШЕНИЕ

time_halo = violator_songs_list[3][1]
time_enjoy = violator_songs_list[5][1]
time_clean =  violator_songs_list[-1][1]
time_3songs = time_halo+time_enjoy+time_clean
print ('Три песни звучат', round(time_3songs,2), 'мин')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# РЕШЕНИЕ
song_1=violator_songs_dict['World in My Eyes']
song_2=violator_songs_dict['Sweetest Perfection']
song_3=violator_songs_dict['Personal Jesus']
song_4=violator_songs_dict['Halo']
song_5=violator_songs_dict['Waiting for the Night']
song_6=violator_songs_dict['Enjoy the Silence']
song_7=violator_songs_dict['Policy of Truth']
song_8=violator_songs_dict['Blue Dress']
song_9=violator_songs_dict['Clean']

time_3songs = song_2+song_7+song_8
other_songs = song_1+song_3+song_4+song_5+song_6+song_9
print ("Общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'", round(time_3songs,2), "минут")
print ("Общее время звучания остальных шести песен:", round(other_songs,2), "минут")

