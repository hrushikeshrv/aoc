from aoc.cli import generate_template

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        generate_template(2023, 4)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
