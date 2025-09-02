import unittest

from chap_4_code import find_root
from finger_ex_4_2 import find_log_base
from finger_ex_4_1 import print_sum_of_roots, is_in


class TestChapter4(unittest.TestCase):
    def test_find_root(self):
        result = find_root(9, 2, 0.01)
        self.assertEqual(round(result), 3)

    def test_find_root_negative(self):
        result = find_root(-9, 2, 0.01)
        self.assertEqual(result, None)

    def test_print_sum_of_roots(self):
        result = print_sum_of_roots(25, -8, 16, 0.001 )
        self.assertEqual(round(result), 5)

    def test_is_in_totally(self):
        result = is_in('Python', 'python')
        self.assertEqual(result, True)

    def test_is_in_partially(self):
        result = is_in('p', 'python')
        self.assertEqual(result, True)

    def test_is_not(self):
        result = is_in('x', 'python')
        self.assertEqual(result, False)

    def test_log_base_returns_none_if_x_is_negative(self):
        result = find_log_base(-16, 2, 0.01)
        self.assertEqual(result, None)

    def test_log_base_returns_none_if_x_is_negative(self):
        result = find_log_base(-16, 2, 0.01)
        self.assertEqual(result, None)

    def test_log_base_returns_none_if_x_is_below_1(self):
        result = find_log_base(1, 2, 0.01)
        self.assertEqual(result, None)

    def test_log_base_returns_none_if_epsilon_is_below_0(self):
        result = find_log_base(2, 0, 0)
        self.assertEqual(result, None)

    def test_log_base_returns_4(self):
        result = find_log_base(16, 2, 0.001)
        self.assertEqual(result, 4)

    def test_log_base_returns_5(self):
        result = find_log_base(125, 3, 0.1)
        self.assertEqual(round(result), 4)

if __name__ == '__main__':
    unittest.main()
