import abc
from typing import Any


class Seq(abc.ABC):
    @abc.abstractmethod
    def get_at(self, i: int):
        # get the i th element of the sequence
        pass

    @abc.abstractmethod
    def set_at(self, i: int, x):
        # set the i th element
        pass

    @abc.abstractmethod
    def insert_first(self, x):
        # insert a element at the beginning of the sequence
        pass

    @abc.abstractmethod
    def delete_first(self):
        # delete the first element of the sequence
        pass

    @abc.abstractmethod
    def insert_last(self, x):
        # insert a element at the end of the sequence
        pass

    @abc.abstractmethod
    def delete_last(self):
        # delete the last element of the sequence
        pass

    @abc.abstractmethod
    def insert_at(self, i: int, x):
        # insert a element into the sequence right after the i th element
        pass

    @abc.abstractmethod
    def delete_at(self, i: int):
        # delete the i th element from the sequence
        pass


class Set(abc.ABC):
    @abc.abstractmethod
    def find(self, key):
        # find the element with the given key
        pass

    @abc.abstractmethod
    def insert(self, x):
        # add x to set, replace item with key x.key if one already exist
        pass

    @abc.abstractmethod
    def build(self, A):
        # build sequence from items in a given iterable A
        pass

    @abc.abstractmethod
    def iter_ord(self):
        # return the stored items one-by-one in key order
        pass

    @abc.abstractmethod
    def find_min(self):
        # return the stored item with the smallest key
        pass

    @abc.abstractmethod
    def find_max(self):
        # return the stored item with the largest key
        pass

    @abc.abstractmethod
    def find_next(self, key):
        # return the stored item with the smallest key larger than the given key
        pass

    @abc.abstractmethod
    def find_perv(self, key):
        # return the stored item with the largest key smaller than the given key
        pass


class PriorityQueue(object):
    def build(self):
        pass

    def insert(self, x):
        pass

    def delete_max(self) -> Any:
        pass

    def find_max(self) -> Any:
        pass
