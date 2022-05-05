from iterators import MyIterator
from generators import my_generator

iter_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

gener_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

if __name__ == "__main__":
    for item in MyIterator(iter_list):
        print(item)

    flat_list = [item for item in MyIterator(iter_list)]
    print(flat_list)

    for item in my_generator(gener_list):
        print(item)