import unittest
from exercise3 import remove_all_after

class TestRemoveAllAfter(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(remove_all_after([1, 2, 3, 4, 5], 3), [1, 2, 3])

    def test_target_not_in_list(self):
        self.assertEqual(remove_all_after([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(remove_all_after([], 3), [])

    def test_target_is_first_element(self):
        self.assertEqual(remove_all_after([3, 4, 5], 3), [3])

    def test_target_is_last_element(self):
        self.assertEqual(remove_all_after([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_list_with_duplicate_targets(self):
        self.assertEqual(remove_all_after([1, 2, 3, 2, 4, 5], 2), [1, 2])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_all_after("not a list", 3)

    def test_target_is_none(self):
        self.assertEqual(remove_all_after([1, 2, 3, None, 4, 5], None), [1, 2, 3, None])

    def test_list_with_mixed_data_types(self):
        self.assertEqual(remove_all_after([1, "two", 3.0, True, 5], 3.0), [1, "two", 3.0])

    def test_single_element_list_target_matches(self):
        self.assertEqual(remove_all_after([3], 3), [3])

    def test_single_element_list_target_does_not_match(self):
        self.assertEqual(remove_all_after([1], 3), [1])

if __name__ == "__main__":
    unittest.main()