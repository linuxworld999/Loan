import unittest
from loan_calculator import calculate_monthly_payment

class TestCalculateMonthlyPayment(unittest.TestCase):

    def test_typical_loan_scenario(self):
        # Principal=10000, Rate=5%, Term=5 years
        # Expected: 188.712 BHD (from online calculator)
        principal = 10000
        annual_rate = 5
        term_years = 5
        expected_payment = 188.712302 
        # Using more precision for expected from calculator:
        # M = 10000 * [0.004166666666666667 * (1 + 0.004166666666666667)^60] / [(1 + 0.004166666666666667)^60 - 1]
        # Monthly rate i = 0.05 / 12 = 0.004166666666666667
        # N = 5 * 12 = 60
        # M = 10000 * [0.004166666666666667 * (1.0041666666666667)^60] / [(1.0041666666666667)^60 - 1]
        # (1.0041666666666667)^60 = 1.28335865
        # Numerator = 10000 * 0.004166666666666667 * 1.28335865 = 10000 * 0.0053473277 = 53.473277
        # Denominator = 1.28335865 - 1 = 0.28335865
        # M = 53.473277 / 0.28335865 = 188.712302
        self.assertAlmostEqual(calculate_monthly_payment(principal, annual_rate, term_years), expected_payment, places=3)

    def test_zero_interest_rate(self):
        # Principal=5000, Rate=0%, Term=10 years
        principal = 5000
        annual_rate = 0
        term_years = 10
        expected_payment = 5000 / (10 * 12) # 41.666666...
        self.assertAlmostEqual(calculate_monthly_payment(principal, annual_rate, term_years), expected_payment, places=3)

    def test_short_loan_term(self):
        # Principal=20000, Rate=7.5%, Term=1 year
        # Expected: 1735.939 BHD (from online calculator)
        principal = 20000
        annual_rate = 7.5
        term_years = 1
        expected_payment = 1735.93900
        # Monthly rate i = 0.075 / 12 = 0.00625
        # N = 1 * 12 = 12
        # M = 20000 * [0.00625 * (1.00625)^12] / [(1.00625)^12 - 1]
        # (1.00625)^12 = 1.07763297
        # Numerator = 20000 * 0.00625 * 1.07763297 = 20000 * 0.006735206 = 134.70412
        # Denominator = 1.07763297 - 1 = 0.07763297
        # M = 134.70412 / 0.07763297 = 1735.93900
        self.assertAlmostEqual(calculate_monthly_payment(principal, annual_rate, term_years), expected_payment, places=3)

    def test_long_loan_term(self):
        # Principal=250000, Rate=4%, Term=30 years
        # Expected: 1193.539 BHD (from online calculator)
        principal = 250000
        annual_rate = 4
        term_years = 30
        expected_payment = 1193.53906
        # Monthly rate i = 0.04 / 12 = 0.0033333333333333335
        # N = 30 * 12 = 360
        # M = 250000 * [0.0033333333333333335 * (1.00333333333333335)^360] / [(1.00333333333333335)^360 - 1]
        # (1.00333333333333335)^360 = 3.31349783
        # Numerator = 250000 * 0.0033333333333333335 * 3.31349783 = 250000 * 0.0110449927 = 2761.248175
        # Denominator = 3.31349783 - 1 = 2.31349783
        # M = 2761.248175 / 2.31349783 = 1193.53906
        self.assertAlmostEqual(calculate_monthly_payment(principal, annual_rate, term_years), expected_payment, places=3)

    def test_negative_principal(self):
        with self.assertRaises(ValueError):
            calculate_monthly_payment(-10000, 5, 5)

    def test_negative_interest_rate(self):
        with self.assertRaises(ValueError):
            calculate_monthly_payment(10000, -5, 5)

    def test_zero_loan_term(self):
        with self.assertRaises(ValueError):
            calculate_monthly_payment(10000, 5, 0)
            
    def test_negative_loan_term(self):
        with self.assertRaises(ValueError):
            calculate_monthly_payment(10000, 5, -5)

if __name__ == '__main__':
    unittest.main()
