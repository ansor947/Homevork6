from pprint import pprint




list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]



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

# for i in FlatIterator(list_of_lists_1):
#     pprint(i)



for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
    
    pprint(check_item)



    if flat_iterator_item == check_item:

        pprint("Yes")

    else:
        pprint("No")



# class FlatIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.cursor = -1
#         self.list_len = len(self.lst)

#     def __iter__(self):
#         self.cursor += 1
#         self.nest_cursor = 0
#         return self

#     def __next__(self):
#         if self.nest_cursor == len(self.lst[self.cursor]):
#           iter(self)
#         if self.cursor == self.list_len:
#           raise StopIteration
#         self.nest_cursor += 1     
#         return self.lst[self.cursor][self.nest_cursor - 1]

# for i in FlatIterator(list_of_lists_1):
#     pprint(i)




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

# def test_3():

#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]

#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):

#         assert flat_iterator_item == check_item

#     assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


# if __name__ == '__main__':
#     test_3()