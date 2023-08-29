"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""


class MyList2:

    def __init__(self, data: list):
        self.data: list = data

    def __iter__(self):
        self.cur = 0
        self.cur_end = len(self.data)
        return self

    def __next__(self):
        self.cur += 1

        if self.cur > self.cur_end:
            raise StopIteration

        return self.data[self.cur - 1]

    def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError('index must be int')

        if index > self.cur_end:
            raise IndexError('index out of range')

        return self.data[index]

    def __len__(self):
        return len(self.data)


my_list = MyList2([1, 2, 3])

for i in my_list:
    print(i)  # 1 2 3

print(my_list[1])  # 2

it = iter(my_list)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # raise


