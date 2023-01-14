from pprint import pprint

import pytest

from parameterized import parameterized, parameterized_class

import unittest

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {
  'user1': [213, 213, 213, 15, 213],
  'user2': [54, 54, 119, 119, 119],
  'user3': [213, 98, 98, 35]
      }

stats = {
  'facebook': 55, 
  'yandex': 120, 
  'vk': 115, 
  'google': 99, 
  'email': 42, 
  'ok': 98
        }


def check_visit(data):
    visit_list = []
    for  visit in geo_logs:
        for flight in visit.values():
            if flight[1] == 'Россия':
                visit_list.extend(flight)

    return visit_list


def receive_unique_values(data):
    name1, name2, name3 = ids.values()
    return list(set(name3) | set(name2) | set(name1))


def receive_max_value(data):
    max_value = max(list(stats.values()))
    for companys_stats in stats.items():
        list_stats = list(companys_stats) 
        name, value = list_stats
        if max_value == value: 
            return name



# FIXTURE_visit1 = [[
#     ({'visit1': ['Москва', 'Россия']}, ['Москва', 'Россия']),
#     ({'visit2': ['Дели', 'Индия']}, ['Дели', 'Индия']),
#     ({'visit3': ['Владимир', 'Россия']}, ['Владимир', 'Россия']),
#     ({'visit4': ['Лиссабон', 'Португалия']}, ['Лиссабон', 'Португалия']),
#     ({'visit5': ['Париж', 'Франция']}, ['Париж', 'Франция']),
#     ({'visit6': ['Лиссабон', 'Португалия']}, ['Тула', 'Россия']),
#     ({'visit7': ['Тула', 'Россия']}, ['Тула', 'Россия']),
#     ({'visit8': ['Тула', 'Россия']}, ['Тула', 'Россия']),
#     ({'visit9': ['Курск', 'Россия']}, ['Курск', 'Россия']),
#     ({'visit10': ['Архангельск', 'Россия']}, ['Архангельск', 'Россия'])
                #  ]]




FIXTURE_visit2 = [('Москва', 'Россия'),
                 ('Владимир', 'Россия'),
                 ('Тула', 'Россия'),
                 ('Тула', 'Россия'),
                 ('Курск', 'Россия'),
                 ('Архангельск', 'Россия')]


class TestFunc(unittest.TestCase):

    @parameterized.expand(check_visit(geo_logs), FIXTURE_visit2)
    def test_check_visit(self, data, etalon):
        # value = 'Россия'
        result = check_visit(data)
        self.assertEqual(result, etalon)        
        # self.assertIn(value ,result)


    # def receive_unique_values(self):
    #     result = receive_unique_values(ids)
    #     etalon = [98, 35, 213, 54, 119, 15]
    #     self.assertEqual(result, etalon) 



    # def receive_max_value(self):
    #     result = receive_max_value(stats)
    #     etalon = 'yandex'
    #     self.assertEqual(result, etalon) 

        



# if __name__ == '__main__':
#     pprint(check_visit(geo_logs))
#     print()
#     pprint(receive_unique_values(ids))
#     print()
#     pprint(receive_max_value(stats))