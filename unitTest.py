import unittest
from  mainCode import date_time_calc
from mainCode import *
from unittest.mock import Mock, MagicMock, patch
import pytest


# define the unit tests
class my_unit_tests(unittest.TestCase):


# ---------------------------------------------------------------------
# TESTING: date_time_calc()
# ---------------------------------------------------------------------

    # Tests to see if function takes correct values and calculates correctly
    # in format YYYY-MM-DD
    def test_valid_date_ymd(self):
        with patch("builtins.input", return_value="2025-10-10"):
            result = date_time_calc()
            assert result == 50

    # Tests to see if function takes correct values and calculates correctly
    # in format YYYY-MM
    def test_valid_date_ym(self):
        with patch("builtins.input", return_value="2025-10"):
            result = date_time_calc()
            assert result == 59

    # Tests to see if users can pass in strings
    def test_string_date(self):
        with patch("builtins.input", return_value="abc"):
            with pytest.raises(ValueError, match = error_message):
                date_time_calc()

    # Tests to see if users can pass in numbers
    def test_number_date(self):
        with patch("builtins.input", return_value="2050"):
            with pytest.raises(ValueError, match = error_message):
                date_time_calc()


    # run the tests
if __name__ == "__main__":
    unittest.main()

