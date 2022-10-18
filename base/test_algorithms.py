from unittest import TestCase

import base.algorithms as alg


class Test(TestCase):
    def test_kosaraju(self):
        cases = [
            # name, args, wants
            ("sample", (2, [(0, 1)]), [0, 1]),
            ("sample", (2, [[1, 0], [0, 1]]), [0, 0]),
            ("sample", (5, [[0, 1], [1, 2], [2, 0], [3, 0], [0, 4]]), [0, 0, 0, 3, 4]),
            ("sample", (4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]), [0, 1, 2, 1]),
        ]
        for i in range(len(cases)):
            name, args, wants = cases[i]
            self.assertEqual(wants, alg.kosaraju(*args), "[%d]name=%s" % (i, name))
