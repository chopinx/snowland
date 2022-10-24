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

    def test_numberToWords(self):
        cases = [
            # name, args, wants
            ("sample", (123,), "One Hundred Twenty Three"),
            ("sample", (0,), "Zero"),
            ("sample", (12345,), "Twelve Thousand Three Hundred Forty Five"),
            ("sample", (1234567,), "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
            ("sample", (12345671234567,),
             "Twelve Thousand Three Hundred Forty Five Billion Six Hundred Seventy One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
            ("sample", (1000000,), "One Million"),
            ("sample", (1000001,), "One Million One"),
        ]
        for i in range(len(cases)):
            name, args, wants = cases[i]
            self.assertEqual(wants, oct.Solution().numberToWords(*args), "[%d]name=%s" % (i, name))

    def test_findAllConcatenatedWordsInADict(self):
        cases = [
            # name, args, wants
            ("sample", (["ab", "a", "b"],), ["ab"]),
            ("sample", (["abcd", "ab", "cd", "a"],), ["abcd"]),
            ("sample", (["abcd", "ab", "c", "a", "abc", "d"],), ["abcd", "abc"]),
        ]
        for i in range(len(cases)):
            name, args, wants = cases[i]
            self.assertEqual(wants, oct.Solution().findAllConcatenatedWordsInADict(*args), "[%d]name=%s" % (i, name))
