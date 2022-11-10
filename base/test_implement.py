import random
from unittest import TestCase

from base.implement import Seq_DynamicArray


class TestSeq_DynamicArray(TestCase):
    def setUp(self) -> None:
        self.n = 10000
        self.seq = Seq_DynamicArray(range(self.n))
        self.debug()

    def reset(self):
        self.setUp()

    def test_build(self):
        self.seq = Seq_DynamicArray(range(self.n))

    def test_get_at(self):
        for i in range(self.n):
            index = random.randint(0, self.seq.length - 1)
            self.assertEqual(self.seq.get_at(index), index)

    def test_set_at(self):
        for i in range(self.n):
            index = random.randint(0, self.seq.length - 1)
            new_value = random.randint(0, self.seq.length - 1)
            self.seq.set_at(index, new_value)
            self.assertEqual(self.seq.get_at(index), new_value)
        self.reset()

    def test_insert_first(self):
        for i in range(self.n):
            new_value = random.randint(0, self.seq.length - 1)
            self.seq.insert_first(new_value)
            self.assertEqual(self.seq.get_at(0), new_value)
            self.assertEqual(self.seq.length, self.n + i + 1)
        self.reset()

    def test_delete_first(self):
        for i in range(self.n - 1):
            self.seq.delete_first()
            self.assertEqual(self.seq.get_at(0), i + 1)
            self.assertEqual(self.seq.length, self.n - i - 1)
        self.reset()

    def test_insert_last(self):
        for i in range(self.n):
            new_value = random.randint(0, self.seq.length - 1)
            self.seq.insert_last(new_value)
            self.assertEqual(self.seq.get_at(self.seq.length - 1), new_value)
            self.assertEqual(self.seq.length, self.n + i + 1)
        self.reset()

    def test_delete_last(self):
        for i in range(self.n - 1):
            self.seq.delete_last()
            self.assertEqual(self.seq.get_at(self.seq.length - 1), self.seq.length - 1)
            self.assertEqual(self.seq.length, self.n - i - 1)
        self.reset()
