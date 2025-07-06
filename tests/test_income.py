import unittest
from datetime import datetime
from real_estate_income import calculate_income


class TestRealEstateIncome(unittest.TestCase):
    def test_constant_occupancy(self):
        start = datetime(2021, 1, 1)
        end = datetime(2021, 3, 31)
        income = calculate_income(start, end, 1000, 100, 0.0, 0.1)
        self.assertAlmostEqual(income, 2430.0)

    def test_variable_occupancy(self):
        start = datetime(2021, 1, 1)
        end = datetime(2021, 3, 31)
        income = calculate_income(
            start, end, 1000, 100, 0.0, 0.1, occupancy=[1.0, 0.5, 0.0]
        )
        self.assertAlmostEqual(income, 1080.0)

    def test_vacancy_rate(self):
        start = datetime(2021, 1, 1)
        end = datetime(2021, 3, 31)
        income = calculate_income(start, end, 1000, 100, 0.2, 0.1)
        self.assertAlmostEqual(income, 1890.0)


if __name__ == "__main__":
    unittest.main()
