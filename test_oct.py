from unittest import TestCase

import oct


class TestSolution(TestCase):
    def test_canFinish(self):
        cases = [
            # name, args, wants
            ("sample", (2, [[0, 1], [1, 0]]), False),
            ("sample", (2, [[1, 0]]), True),
            ("sample", (5, [[0, 1], [1, 2], [2, 0], [3, 0], [0, 4]]), False),
            ("sample", (4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]), False),
            ("sample", (4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]), False),
        ]
        for i in range(len(cases)):
            name, args, wants = cases[i]
            self.assertEqual(wants, oct.Solution().canFinish(*args), "[%d]name=%s" % (i, name))

    def test_intToRoman(self):
        cases = [
            # name, args, wants
            ("sample", (2,), "II"),
            ("sample", (4,), "IV"),
            ("sample", (9,), "IX"),
            ("sample", (27,), "XXVII"),
            ("sample", (58,), "LVIII"),
            ("sample", (1994,), "MCMXCIV"),
        ]
        for i in range(len(cases)):
            name, args, wants = cases[i]
            self.assertEqual(wants, oct.Solution().intToRoman(*args), "[%d]name=%s" % (i, name))
