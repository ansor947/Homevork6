from pprint import pprint

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.counter =  -1
        

    def __iter__(self):
        self.counter += 1
        self.counter_values = 0
        return self

    def __next__(self):
        if len(self.list_of_list[self.counter]) == self.counter_values:
            iter(self)
        if self.counter >= len(self.list_of_list):
            raise StopIteration


        self.nested_lists = self.list_of_list[self.counter]
        self.values = self.nested_lists[self.counter_values]
        self.counter_values += 1
        return self.values


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
    test_1()
    pprint("Yes")
