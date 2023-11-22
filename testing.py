import unittest
import tkinter as tk
from Project6611 import DataStatisticsGUI
from SupportClass import Support

class TestDataStatistics(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.app = DataStatisticsGUI(root)

    def tearDown(self):
        # Destroy the instance of DataStatisticsGUI after testing
        self.app.root.destroy()

    def test_mean_calculation(self):
       	print("Testing the mean method")
        self.app.data = [34, 481, 788, 353, 180]
        self.app.calculate_mean()
        result = float(self.app.mean_label.cget("text"))
        self.assertEqual(result, 367.2)

    def test_median_calculation(self):
        print("Testing the median method")
        self.app.data = [1, 2, 3, 4, 5]
        self.app.calculate_median()
        result = float(self.app.median_label.cget("text"))
        self.assertEqual(result, 3.0)

    def test_mode_calculation(self):
        print("Testing the mode method")
        self.app.data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        self.app.calculate_mode()
        result = self.app.mode_label.cget("text")
        self.assertEqual(result, "[4, 5]")

    def test_maximum_calculation(self):
        print("Testing the maximum method")
        self.app.data = [34, 481, 788, 353, 180]
        self.app.calculate_maximum()
        result = float(self.app.maximum_label.cget("text"))
        self.assertEqual(result, 788)

    def test_minimum_calculation(self):
        print("Testing the minimum method")
        self.app.data = [34, 481, 788, 353, 180]
        self.app.calculate_minimum()
        result = float(self.app.minimum_label.cget("text"))
        self.assertEqual(result, 34)

    def test_sd_calculation(self):
        # Test the calculate_sd method
        self.app.data = [1, 2, 3, 4, 5]
        self.app.calculate_sd()
        result = float(self.app.sd_label.cget("text"))
        expected_sd = 1.41
        self.assertEqual(result, expected_sd)

    def test_mad_calculation(self):
        print("Testing the mean absolute deviation method")
        self.app.data = [1, 2, 3, 4, 5]
        self.app.calculate_mad()
        result = float(self.app.mad_label.cget("text"))
        expected_mad = 1.2
        self.assertEqual(result, expected_mad)

    def test_quick_sort(self):
        print("Testing the quick sort method")
        input_list = [34, 481, 788, 353, 180]
        result = Support.quick_sort(input_list)
        expected_result = [34, 180, 353, 481, 788]
        self.assertEqual(result, expected_result)

    def test_absolute_positive(self):
        print("Testing the absolute method for positive input")
        result = Support.absolute(5)
        self.assertEqual(result, 5)

    def test_absolute_negative(self):
        print("Testing the absolute method for negative input")
        result = Support.absolute(-8)
        self.assertEqual(result, 8)

    def test_custom_sqrt(self):
        print("Testing the custom square root method")
        input_number = 16
        result = Support.custom_sqrt(input_number)
        expected_result = 4.0
        self.assertAlmostEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
