import unittest
from unittest import TestCase

import sep


class TestSolution(TestCase):
    def test_maxValue(self):
        cases = [
            # name, args, wants
            ("sample", ("-13", 2), "-123"),
            ("sample", ("-13", 4), "-134"),
            ("sample", ("-23", 1), "-123"),
            ("sample", ("13", 2), "213"),
        ]
        for case in cases:
            name, args, wants = case
            self.assertEqual(wants, sep.Solution().maxValue(*args), "name=%s" % name)

    def test_ladderLength(self):
        cases = [
            # name, args, wants
            ("sample", ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
            ("sample", ("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
            ("sample", ("talk", "tail", ["talk", "tons", "fall", "tail", "gale", "hall", "negs"]), 0),
        ]
        for i in range(len(cases)):
            name, args, wants = cases[i]
            self.assertEqual(wants, sep.Solution().ladderLength(*args), "[%d]name=%s" % (i, name))

    def test_copyRandomList(self):
        head = sep.Node(0)
        head.next = sep.Node(1)
        head.next.random = head

        new_head = sep.Node(0)
        new_head.next = sep.Node(1)
        new_head.next.random = new_head

        if head == new_head:
            print("ok")

        cases = [
            ("sample", (head,), new_head)
        ]
        for i in range(len(cases)):
            name, args, wants = cases[i]
            old_head = args[0]
            new_head = sep.Solution().copyRandomList(*args)
            while old_head or new_head:
                self.assertEqual(old_head, new_head, "[%d]name=%s" % (i, name))
                self.assertEqual(old_head.next, new_head.next, "[%d]name=%s" % (i, name))
                self.assertEqual(old_head.random, new_head.random, "[%d]name=%s" % (i, name))
                old_head, new_head = old_head.next, new_head.next

    def test_wordBreak(self):
        cases = [
            # name, args, wants
            ("sample", ("catsanddog", ["cat", "cats", "and", "sand", "dog"]), ["cats and dog", "cat sand dog"]),
            ("sample", ("c", ["cat", "cats", "and", "sand", "dog"]), []),
            ("sample", ("c", ["c", "cats", "and", "sand", "dog"]), ["c"]),
        ]
        for i in range(len(cases)):
            name, args, wants = cases[i]
            self.assertEqual(sorted(wants), sorted(sep.Solution().wordBreak(*args)), "[%d]name=%s" % (i, name))


if __name__ == '__main__':
    unittest.main()
