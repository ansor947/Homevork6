# Огромная просьба вернуть на доработку. 
# Из-за проблем со сдачей ДЗ по ОПП и глупости, по которой я открыл параллельно это ДЗ, сделать его я не успел.
#  Многое еще не понятно, буду очень признателен на предоставленное дополнительное время. 
#  Если есть возможность, объясните, пожалуйста, что от меня хотят в3м задании? 
#  Я понял что нужно сшить файлы, но вот какие-то строки меня обескураживают! 
#  Я их просто должен между файлами отдельнвми командами прописать? Или как?

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
                dishes_list = []
                ing_dict = {}
                a = 0
                for food_name in cook_book:
                        if food_name in dishes:
                            for i in compile_list_ing(data):
                                    a += 1
                                    dishes_list.append(food_name)
                                    ing_dict[cook_book[food_name][a].pop('ingredient_name')] : cook_book[food_name][a]
                                    pprint(cook_book[food_name])
                        
                                        
                

        pprint(get_shop_list_by_dishes('Омлет', 2))

      
                

              