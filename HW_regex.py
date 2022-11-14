С заданиями по этой теме я разобрался, а вот как соединить дубли - нет. Смог их выделить и хочу применить
union для множеств, но не могу составить универсальную функцию, чтобы разбить значения дублей по 
фамилии и имени и спарить. Прошу дать подсказку и вернуть работу, если это возможно.


import csv
import re
from pprint import pprint

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter="\n")
    contacts_list = list(rows)
    text_list = str(rows)
# pprint(type(text_list))


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


# pprint(split_list())

def receive_repeats():
    lastname_list = []
    firstname_list = []
    dict_repeats = []
    
    for argument in split_data():
        lastname_list.append(argument[0])
        firstname_list.append(argument[1])
        x = lastname_list.count(argument[0])
        i = firstname_list.count(argument[1])
        if x > 1 and i > 1:
            # dict_repeats[argument[0]] = dict_repeats.get(argument[0], argument[1])
            dict_repeats.append(argument[0])
    return dict_repeats

# pprint(receive_repeats())


def create_dict():
    create_dict = []
    for argument in split_data():
        if argument[0] in receive_repeats():
            create_dict.append(argument)
    return create_dict

# pprint(create_dict())

# def merge_data():
#     c = []
#     for arg in create_dict():
#         c.append(set(arg))
#         c = set(split_list()).intersection(create_dict())
#     return c
    
# c = set(split_data()).intersection(set(create_dict()))
# pprint(c)
# # pprint(merge_data())





# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
  
#   datawriter.writerows(contacts_list)
