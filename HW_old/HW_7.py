from pprint import pprint

with open(r'recipes.txt', 'rt', encoding='utf-8') as file:
                data = file.readlines()
                data = [line.rstrip() for line in data]
                del(data[1])
                del(data[6])
                del(data[12])
                del(data[17])
                data.remove('')
                data.remove('')
                data.remove('')

                def compile_list_ing(ddd):
                        dish = []
                        for i in data:
                                if "|" in i:
                                        ing = i.split('|')
                                        dish.append({'ingredient_name': ing[0], 'quantity': ing[1], 'measure': ing[2]})                
                        return dish

                cook_book = {data[0]:compile_list_ing(data)[0:3], data[4]:compile_list_ing(data)[3:7], data[9]:compile_list_ing(data)[7:10], data[13]:compile_list_ing(data)[10:15]}

                print()
                                        
                def get_shop_list_by_dishes(dishes, person_count):
                        for dish in cook_book:
                                if dish in dishes:
                                        
                                        for ing_nam in cook_book[dish]:
                                                ing_nam['quantity'] = int(ing_nam['quantity']) * person_count
                                                list_by_dishes = {ing_nam.pop('ingredient_name'): ing_nam}
                                                print(list_by_dishes)                                                                
                                
                pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5))



with open(r"C:\Users\Андрей-сан\Desktop\py-homework-basic-files\2.4.files\sorted\1.txt", "rt", encoding='utf-8') as f:
                data = f.readlines()
                i=0
                for line in data:
                                i+=1    
                                print(i)
                                 
# Для определения количества строк и местоположения файла при записи использовал этот цикл.

from pprint import pprint

with open(r"C:\Users\Андрей-сан\Desktop\py-homework-basic-files\2.4.files\sorted\1.txt", 'rt', encoding='utf-8') as f:
                data_1 = f.readlines()
                data_1 = [line.rstrip() for line in data_1]
with open(r"C:\Users\Андрей-сан\Desktop\py-homework-basic-files\2.4.files\sorted\2.txt", 'rt', encoding='utf-8') as f:
                data_2 = f.readlines()
                data_2 = [line.rstrip() for line in data_2]
with open(r"C:\Users\Андрей-сан\Desktop\py-homework-basic-files\2.4.files\sorted\3.txt", 'rt', encoding='utf-8') as f:
                data_3 = f.readlines()
                data_3 = [line.rstrip() for line in data_3]       

words_2 = data_2
words_1 = data_1
words_3 = data_3

file1 = open('neu1.txt', 'x', encoding='utf-8')
file1.write("2.txt\n")
file1.write("1\n")
file1.write('\n'.join(words_2))
file1.write("\n1.txt\n")
file1.write("8\n")
file1.write('\n'.join(words_1))
file1.write("\n3.txt\n")
file1.write("9\n")
file1.write('\n'.join(words_3))
            