# Вроде решил, через связку ключ - значение я пытался реализовать решение изначально, но не смог, поэтому раздробил все на этапы. 
# Если у вас есть возможность дать ссылку на решение задачи подобным образом - буду признателен.



import csv
import re
from pprint import pprint

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter="\n")
    contacts_list = list(rows)

# pprint(contacts_list)

def processing_number(data):
    list = []
    pattern = r"(\+7|8)[\s]?\(?(495)\)?[\-\s]?(\d{3})[\-\s]?(\d{2})[\-\s]?(\d{2})\s*\(?(доб.)?\s*(\d+)?[\)]?"
    string = r"+7(\2)\3-\4-\5 \6\7"
    for person_list in contacts_list:
        for data_person_pn in person_list:
            org_num = re.sub(pattern, string, data_person_pn)
            list.append(org_num)
    return list

# pprint(processing_number(contacts_list))

def put_commas():
    list = []
    pattern = r"(^[А-Я]\w*)[,\s]?([А-Я]\w*)[,\s]?([А-Я]\w*)?"
    string = r"\1,\2,\3,"
    for data_person_pt in processing_number(contacts_list):
        put_list = re.sub(pattern, string, data_person_pt)
        list.append(put_list)
    return list

# pprint(put_commas())

def separate_email():
    list = []
    pattern = r"(\b[a-zA-Z0-9]\w+[\.]?[a-zA-Z0-9]+@\w+\.\w+)"
    string = r"\1"
    for data_person_cl in put_commas():
        separate_list = re.sub(pattern, string, data_person_cl)
        list.append(separate_list)
    return list

# pprint(separate_email())

def clearing_commas():
    list = []
    pattern = r"\,+"
    string = r","
    for data_person_cl in separate_email():
        clean_list = re.sub(pattern, string, data_person_cl)
        clean_list = clean_list.rstrip(",")
        list.append(clean_list)
    return list

# pprint(clearing_commas())

def split_data():
    split_list =[]
    for person in clearing_commas():
        split_data = person.split(",")
        split_list.append(split_data)
    return split_list

# pprint(split_data())

def lastname_repeats():
    lastname_list = []
    lastname_repeats = []
    for argument in split_data():
        lastname_list.append(argument[0])
        x = lastname_list.count(argument[0])
        if x > 1:
            lastname_repeats.append(argument[0])
    return lastname_repeats

# pprint(lastname_repeats())

def list_repeats():
    lastname_list = []
    list_repeats = []
    for argument in split_data():
        lastname_list.append(argument[0])
        x = lastname_list.count(argument[0])
        if x > 1:
            if argument[0] in argument:
                list_repeats.append(argument)
    return list_repeats

# pprint(list_repeats())


def create_merge_list():
    create_dict = []
    for argument in split_data():
        if argument[0] in lastname_repeats():
            create_dict.append(argument)
    return create_dict

# pprint(create_merge_list())

def looking_first_value():
    first_value =[]
    for argument in create_merge_list():
        if (argument not in list_repeats()[0:]):
            first_value.append(argument)  
    return first_value
    
# pprint(looking_first_value())

def merge_repeats():
    join_repeats = []
    for argument in list_repeats():
        for element in looking_first_value():
            if ((element[0] == argument[0]) and (element[1] == argument[1])):
                a = [item for item in argument if item  in element]
                b = [item for item in element if item  not in argument]
                c = [item for item in argument if item not in element]
                join = a + b +c
                join_repeats.append(join)               
    return join_repeats
    
# pprint(merge_repeats())

def merge_list():
    list_unique = []
    for argument in  split_data():
            # pprint(element)
            if argument not in create_merge_list():
                list_unique.append(argument)
    join_list = list_unique + merge_repeats()
    return join_list

# pprint(merge_list())

def str_list():
    str_list = []
    for argument in merge_list():
        str_list.append([",".join(argument)])
    return str_list

# pprint(str_list())

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  
  datawriter.writerows(str_list())
