documents = [ {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
              {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
              {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"} ]


directories = { '1': ['2207 876234', '11-2', '5455 028765'],
                '2': ['10006'],
                '3': [] }

from pprint import pprint

##################################################

def people(data): 

  number = input('Введите номер документа: ')
  
  for dict in data:

    if number == dict["number"]:
      print()
    
      return dict["name"]
      
  return 'Введите корректные данные!' 
  

#########################################

def shelf(data): 

  number = input('Введите номер документа: ')

  for rack in data: 
    
    if number in data[rack]:      
      print()    
      
      return rack 
      
  return 'Введите корректные данные!' 
  

#######################################

def list(data): 

  for person in data:
    doc_list = ( f' {person["type"]} {person["number"]} {person["name"]} ')
    print(doc_list)     


######################################

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
      

#######################################

def delete(data, addition): 


  new_number = input('Введите номер документа: ')
  
  for person in data:
    print()
  
    if new_number == person["number"]:
      
      data. remove(person)
    
      
  for rack in addition.values():
    print()
    
    if new_number in rack:
      
      rack.remove(new_number) 
      
      return data, addition
    
  else:
      
    mistake = f'Введите корректные данные! Данного документа не существует!'

    return mistake  
      
####################################################

    
def move (addition): 
  
  new_number = input('Введите номер документа: ')
  new_rack = input('Введите номер новой полки: ')

  for keys in addition.keys():
    if new_number in addition[keys]:
      rack = keys
      print()
      
  values = sum(addition.values(), [])
  print()

  if new_number not in values:
  
    mistake = f'Введите верный номер документа!'
    return mistake
    
  elif new_number in addition[rack] and new_rack == rack:
    
    mistake = f'Данный документ уже содержится на полке!'
    return mistake
  
  elif new_rack in addition.keys() and new_number in values and new_rack != rack:
    addition[rack].remove(new_number)
    addition[new_rack].append(new_number)
     
    return addition    
 

  elif new_rack not in addition.keys(): 

    mistake = f'Введите верный номер полки для перемещения документа'
    return mistake 

    
####################################################
    
def add_shelf(addition):
   
  new_rack = input('Введите номер новой полки: ')
  
  print()
       
  if new_rack not in addition.keys():
      
    addition[new_rack] = []
    
    return addition
  
  else:
    
    mistake = f'Введите корректные данные! Данная полка уже существует!'
    
    return mistake
    
####################################################
def main(data, addition):
  
  while True:
    print()
    command = input('Введите команду(p, s, l, a, d, m, as): ')
    print()
    if command == 'p':
      print(people(documents))
      
    elif command == 's':
      print(shelf(directories))
  
    elif command == 'l':
      list(documents)
  
    elif command == 'a':
      print(add(documents, directories))
  
    elif command == 'd':
      print(delete(documents, directories))
      return
    elif  command == 'm':
      print(move(directories))
      return
      
    elif  command == 'as':
      print(add_shelf(directories))
      return
      
    else:
      mistake = f'Введите верную команду!'
      return mistake
      
pprint(main(documents, directories))