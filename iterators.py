class MyIterator:

    #
    def __init__(self, my_list):
        self.my_list = sum(my_list, [])

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.my_list):
            raise StopIteration
        else:
            return self.my_list[self.index]

