import math
import random
import time
from unittest import TestCase

from base.implement import Seq_DynamicArray, Seq_LinkedList, Seq_AVLTree


class TestSeq_DynamicArray(TestCase):
    def setUp(self) -> None:
        self.n = 1000
        self.seq = Seq_AVLTree(range(self.n))

    def reset(self):
        self.setUp()

    def test_build(self):
        self.seq = Seq_AVLTree(range(self.n))

    def test_get_at(self):
        for i in range(self.n):
            index = random.randint(0, self.seq.len() - 1)
            self.assertEqual(self.seq.get_at(index), index)

    def test_set_at(self):
        for i in range(self.n):
            index = random.randint(0, self.seq.len() - 1)
            new_value = random.randint(0, self.seq.len() - 1)
            self.seq.set_at(index, new_value)
            self.assertEqual(self.seq.get_at(index), new_value)
        self.reset()

    def test_insert_first(self):
        for i in range(self.n):
            new_value = random.randint(0, self.seq.len() - 1)
            self.seq.insert_first(new_value)
            self.assertEqual(self.seq.get_at(0), new_value)
            self.assertEqual(self.seq.len(), self.n + i + 1)
        print(self.seq.data.height)
        self.reset()

    def test_delete_first(self):
        for i in range(self.n - 1):
            self.seq.delete_first()
            self.assertEqual(self.seq.get_at(0), i + 1)
            self.assertEqual(self.seq.len(), self.n - i - 1)
        self.reset()

    def test_insert_last(self):
        for i in range(self.n):
            new_value = random.randint(0, self.seq.len() - 1)
            self.seq.insert_last(new_value)
            self.assertEqual(self.seq.get_at(self.seq.len() - 1), new_value)
            self.assertEqual(self.seq.len(), self.n + i + 1)
        self.reset()

    def test_delete_last(self):
        for i in range(self.n - 1):
            self.seq.delete_last()
            self.assertEqual(self.seq.get_at(self.seq.len() - 1), self.seq.len() - 1)
            self.assertEqual(self.seq.len(), self.n - i - 1)
        self.reset()


class Test(TestCase):
    def setUp(self) -> None:
        self.n = 100000
        self.times = 5

    def test_bench(self):
        n, times = self.n, self.times
        implementations = {
            "Seq_DynamicArray": Seq_DynamicArray,
            "Seq_LinkedList": Seq_LinkedList,
            "Seq_AVLTree": Seq_AVLTree}
        methods = {
            "build": [(range(n),)] * times,
            "get_at": [(random.randint(0, n - 1),) for _ in range(times)],
            "set_at": [(random.randint(0, n - 1), random.randint(0, n - 1)) for _ in range(times)],
            "insert_at": [(random.randint(0, n - 1), random.randint(0, n - 1)) for _ in range(times)],
            "delete_at": [(random.randint(0, n - 1),) for _ in range(times)],
            "insert_first": [(random.randint(0, n - 1),) for _ in range(times)],
            "delete_first": [() for _ in range(times)],
            "insert_last": [(random.randint(0, n - 1),) for _ in range(times)],
            "delete_last": [() for _ in range(times)]
        }
        costs = {method: {key: 0 for key in implementations.keys()} for method in methods.keys()}
        min_cost = math.inf
        for imp_name, imp in implementations.items():
            ins = imp([])
            for method, args_list in methods.items():
                start_time = time.time()
                for args in args_list:
                    getattr(ins, method)(*args)
                costs[method][imp_name] = time.time() - start_time
                min_cost = min(min_cost, costs[method][imp_name])
        print("              method" + ("{:>30s}" * len(implementations)).format(*implementations.keys()))
        for method, cost in costs.items():
            print("{:>30s}".format(method), end="")
            for imp in implementations.keys():
                print("{:>10d}".format(int(cost[imp] / min_cost)), end="")
                print(" {:<19s}".format("*" * int(math.log2(int(cost[imp] / min_cost)) + 1)), end="")
            print()
