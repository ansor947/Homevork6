from pprint import pprint

# Здравствуйте,
# это решение я нашел в интернете. Оно работает и написано под задание №1 ДЗ. Если исходить из посыла в лекции,
# что не стоит изобретать велосипед, а стоит погуглить, ибо все может быть предумано до меня, то я справился на 146%
# Но в лекции было сказано, что этот инструмент будет необходим далее, поэтому огромная просьба посмотреть код, дать 
# советы и вернуть работу на доработку, тем более, что задачу с yield еще не решил.


class FlatIterator:
    def __init__(self, lst):
        self.lst = lst
        self.cursor = -1
        self.list_len = len(self.lst)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self.lst[self.cursor]):
          iter(self)
        if self.cursor == self.list_len:
          raise StopIteration
        self.nest_cursor += 1     
        return self.lst[self.cursor][self.nest_cursor - 1]

for i in FlatIterator(list_of_lists_1):
    pprint(i)

# Это производное от моего решения решения, с понимание того, что я нашел в интернете. У меня нет желания копировать,
# поэтому старался понять логику и заимствовать минимум. Впринципе, почти получилось. Не могу получить значение
#  return строкой, а соответственно, собрать значения в виде одного списка и ловлю ошибку на второй проверке. 
# Можете подсказать, как доработать это решение, если это возможно?

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.counter =  -1
        

    def __iter__(self):
        self.counter += 1
        self.counter_values = 0
        return self

    def __next__(self):
        # if len(self.list_of_list) == self.counter_values:
        if len(self.list_of_list[self.counter]) == self.counter_values:
            iter(self)
        if self.counter > len(self.list_of_list):
            raise StopIteration


        self.nested_lists = self.list_of_list[self.counter]
        self.values = self.nested_lists[self.counter_values]
        self.counter_values += 1
        return self.values

# Это решение было первым. Тут мне удалось пользуясь знакомыми инструментами, получить спиок значений в нужном виде,
# но не удалось их распаковать. Мне не хватило знаний и найти подходящий способ в интернете я не смог. Можно
# было использовать допфункцию, но в условии, в классе, прописаны только 3 Кроме того, не знаю, насколько уместен в 
# решении цикл for. Если это уместно, подскажите, пожалуйста, как распаковать список?

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        self.nested_lists = []
        for item in self.list_of_list:
            self.nested_lists.extend(item)

            if self.counter == 1:
            
                raise StopIteration
    
        return self.nested_lists




def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    pprint("Yes")
    test_1()
