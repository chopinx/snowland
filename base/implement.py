from base.interface import Seq


class Seq_DynamicArray(Seq):
    def __init__(self, A):
        self.array = [None]
        self.length = 0
        for x in A:
            self.insert_last(x)

    def __resize(self):
        if self.length + 1 > self.__capacity():
            new_array = [None] * (2 * self.__capacity())
        elif self.length * 3 < self.__capacity() and self.__capacity() > 1:
            new_array = [None] * (self.__capacity() // 2)
        else:
            return
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def __capacity(self):
        return len(self.array)

    def get_at(self, i: int):
        if i >= self.length:
            raise Exception("range index out of bounds")
        return self.array[i]

    def set_at(self, i: int, x):
        if i >= self.length:
            raise Exception("range index out of bounds")
        self.array[i] = x

    def insert_first(self, x):
        self.__resize()
        for i in range(self.length):
            self.array[i + 1] = self.array[i]
        self.array[0] = x
        self.length += 1

    def delete_first(self):
        if self.length == 0:
            raise Exception("sequence is already empty")
        self.__resize()
        for i in range(self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1

    def insert_last(self, x):
        self.__resize()
        self.array[self.length] = x
        self.length += 1

    def delete_last(self):
        if self.length == 0:
            raise Exception("sequence is already empty")
        self.__resize()
        self.length -= 1

    def insert_at(self, i: int, x):
        self.__resize()
        for j in range(i, self.length):
            self.array[j + 1] = self.array[j]
        self.array[i] = x
        self.length += 1

    def delete_at(self, i: int):
        if i >= self.length:
            raise Exception("range index out of bounds")
        self.__resize()
        for j in range(i + 1, self.length):
            self.array[j - 1] = self.array[j]
        self.length -= 1
