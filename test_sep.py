from unittest import TestCase

import sep


class TestSolution(TestCase):
    def test_max_value(self):
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
