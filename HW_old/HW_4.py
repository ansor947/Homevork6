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

for  visit in geo_logs:
  for flight in visit.values():
    if flight[1] == 'Россия':
      print(visit)

#########################################################

ids = {
  'user1': [213, 213, 213, 15, 213],
  'user2': [54, 54, 119, 119, 119],
  'user3': [213, 98, 98, 35]
      }

name1, name2, name3 = ids.values()

print (list(set(name3) | set(name2) | set(name1)))


#########################################################




queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


w1 = 0
w2 = 0  
w3 = 0
sum_words = 0

for request in queries:

  splited_request = len(request.split())

  sum_words += 1
  
  if splited_request == 3:
    
    w3 += 1    

  elif splited_request == 2:

    w2 += 1
    
  else: 

    w1 += 1
  
w3_persent =  round(w3 * 100 / sum_words, 2)
print(f'Поисковых запросов из трёх слов: {w3_persent}%')
w2_persent =  round(w2 * 100 / sum_words, 2)
print(f'Поисковых запросов из двух слов: {w2_persent}%') 
w1_persent =  round(w1 * 100 / sum_words, 2)
print(f'Поисковых запросов из одного слова: {w1_persent}%')

#########################################################



stats = {
  'facebook': 55, 
  'yandex': 120, 
  'vk': 115, 
  'google': 99, 
  'email': 42, 
  'ok': 98
        }


max_value = max(list(stats.values()))


for companys_stats in stats.items():
  
  list_stats = list(companys_stats)
  
  name, value = list_stats
  
  if max_value == value:
    
    print(name)