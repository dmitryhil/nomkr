import unittest
from datetime import datetime
from mkr import read_data_from_file, price_change_last_month

class TestPriceChange(unittest.TestCase):
    def setUp(self):
        # Створення тестових даних для файлу
        self.test_data = [
            ("Product A", datetime(2024, 3, 15), 25.50),
            ("Product B", datetime(2024, 3, 20), 30.00),
            ("Product A", datetime(2024, 4, 1), 28.00),
            ("Product B", datetime(2024, 4, 5), 32.00),
            ("Product A", datetime(2024, 4, 10), 30.00)
        ]

    def test_read_data_from_file(self):
        expected_data = self.test_data
        filename = "test_products.txt"
        # Запис тестових даних у файл
        with open(filename, 'w') as file:
            for item in expected_data:
                file.write(','.join(map(str, item)) + '\n')
        # Зчитування даних з файлу
        actual_data = read_data_from_file(filename)
        self.assertEqual(actual_data, expected_data)

    def test_price_change_last_month(self):
        test_data = self.test_data
        product_name = "Product A"
        expected_price_change = 2.50
        self.assertEqual(price_change_last_month(test_data, product_name), 
                         f"The price change for {product_name} in the last month is {expected_price_change:.2f}.")

    def test_not_enough_data(self):
        test_data = self.test_data[:2]  # Використання лише двох записів
        product_name = "Product B"
        expected_result = "Not enough data to calculate price change for the last month."
        self.assertEqual(price_change_last_month(test_data, product_name), expected_result)

    def tearDown(self):
        # Видалення тестового файлу після тестування
        filename = "test_products.txt"
        import os
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    unittest.main()
