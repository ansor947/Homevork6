import os

import datetime 

from pprint import pprint

documents = [ {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
              {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
              {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"} ]


directories = { '1': ['2207 876234', '11-2', '5455 028765'],
                '2': ['10006'],
                '3': [] }


def logger(old_function):

    def new_function(*args, **kwargs):

        with open('main_test.log', 'a', encoding='utf-8') as file:
            start = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            file.write(f'Время вызова функции: {start}\n')
            file.write(f'{old_function.__name__}\n')
            file.write(f'{args} {kwargs}\n')
            file.write(f'{result}\n\n')
            return result     
        
    return new_function

@logger
def list(data): 

  for person in data:
    doc_list = ( f' {person["type"]} {person["number"]} {person["name"]} ')
    print(doc_list) 

list(documents)


@logger
def people(data): 

  number = input('Введите номер документа: ')
  
  for dict in data:

    if number == dict["number"]:
      print()
    
      return dict["name"]
      
  return 'Введите корректные данные!' 


@logger
def add(data, addition): 

  new_type = input('Введите тип документа: ') 
  new_number = input('Введите номер документа: ')
  new_name = input('Введите имя владельца: ') 
  rack = input('Введите номер полки: ')
  
  print()
    
  new_person = { "type":new_type, "number":new_number, "name":new_name}
       
  if rack in addition.keys():

    data.append(new_person)
      
    addition[rack].append(new_number)
    
    return data, addition
  
  else:
    
    mistake = f'Введите корректные данные! Данной полки не существует!'
    
    return mistake 

list(documents)
people(documents)
add(documents,directories)