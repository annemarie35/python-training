import unittest

from chap_4_code import find_root, find_root_refactored, find_root_bounds, bisection_solve
from finger_ex_4_1 import print_sum_of_roots, is_in
from finger_ex_4_2 import find_log_base
from finger_ex_4_4 import create_lambda
from finger_ex_4_5 import find_last


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

class TestRefactoringFindRoot(unittest.TestCase):
    def test_find_root_refactored(self):
        result = find_root_refactored(9, 2, 0.01)
        self.assertEqual(round(result), 3)

    def test_find_root_refactored_return_none_for_negative_value(self):
        result = find_root_refactored(-9, 2, 0.01)
        self.assertEqual(result, None)

    def test_find_root_refactored_return_none_for_power_below_2(self):
        result = find_root_refactored(9, 0, 0.01)
        self.assertEqual(result, None)

    def test_find_root_refactored_return_none_for_epsilon_is_negative(self):
        result = find_root_refactored(9, 2, -0.01)
        self.assertEqual(result, None)

    def test_find_root_bounds(self):
        result = find_root_bounds(9, 2)
        self.assertEqual(result, (-1, 9) )

    def test_bisection_solve(self):
        result = bisection_solve(9, 2, 0.01, -1, 9)
        self.assertEqual(round(result), 3)

class TestFingerExerciseFindLog(unittest.TestCase):
    def test_find_log_return_power(self):
        result = find_log_base(125, 3, 0.01)
        self.assertEqual(round(result), 4)

    def test_find_log_return_none_for_x_is_1(self):
        result = find_log_base(1, 3, 0.01)
        self.assertEqual(result, None)

    def test_find_log_return_none_for_x_negative(self):
        result = find_log_base(-125, 3, 0.01)
        self.assertEqual(result, None )

    def test_find_log_return_none_for_epsilon_negative(self):
        result = find_log_base(125, 3, 0)
        self.assertEqual(result, None)

class TestFingerExerciseLambda(unittest.TestCase):
    def test_create_lambda(self):
        result = create_lambda()
        self.assertEqual(result(10, 2), 5)

class TestFingerExerciseFindLast(unittest.TestCase):
    def test_find_last_sub_does_not_occur(self):
        self.assertEqual(find_last('marvellous', 'day'), None)

    def test_find_last_sub_is_empty_string(self):
        self.assertEqual(find_last('marvellous', ''), None)

    def test_find_last_s_is_empty_string(self):
        self.assertEqual(find_last('', 'day'), None)

    def test_find_last(self):
        self.assertEqual(find_last('marvellous day, a really marvellous day', 'day'), 36)

    def test_find_last(self):
        self.assertEqual(find_last('  marvellous day', 'marvellous'), 2)

if __name__ == '__main__':
    unittest.main()
