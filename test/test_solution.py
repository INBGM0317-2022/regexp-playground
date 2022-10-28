import unittest
from typing import Type

from playground.solution import Solution


class TestExercises(unittest.TestCase):
    """
    Stores unit tests to test your solution.
    """
    __solution: Type[Solution] = None # TODO Solution

    def test_is_email_address(self) -> None:
        """
        Tests function `is_email_address()`.

        :return: nothing
        """
        for value in ["user@company.com", "-@-.hu"]:
            self.assertTrue(self.__solution.is_email_address(value), f"{value} should be valid")
        for value in ["where-is-the-end@", "user@nodot", "user@twodots..com", "user@short-domain.x"]:
            self.assertFalse(self.__solution.is_email_address(value), f"{value} should be invalid")

    def test_is_c_identifier(self) -> None:
        """
        Tests function `is_c_identifier()`.

        :return: nothing
        """
        for value in ["i", "long_and_mnemonic_identifier", "thisiscorrectalthoughthewordsarenotseparated", "foo_bar"]:
            self.assertTrue(self.__solution.is_c_identifier(value), f"{value} should be valid")
        for value in ["it_contains_1number", "it_contains_CapitalLetters", "dot.is_not_accepted", "", "_", "_foo",
                      "foo_", "_foo_", "foo__bar"]:
            self.assertFalse(self.__solution.is_c_identifier(value), f"{value} should be invalid")

    def test_is_home_address(self) -> None:
        """
        Tests function `is_home_address()`.

        :return: nothing
        """
        for value in ["4028 Debrecen, Kassai ut 26."]:
            self.assertTrue(self.__solution.is_home_address(value), f"{value} should be valid")
        for value in ["0000 x, y", "123 Aprajafalva, Torpapa sugarut 1.", "9999 Bivalyrocsoge,Nincsisilyen utca 10.",
                      "9999,Bivalyrocsoge, Nincsisilyen utca 10.", "9999 Bivalyrocsoge,",
                      "9999 , Nincsisilyen utca 10."]:
            self.assertFalse(self.__solution.is_home_address(value), f"{value} should be invalid")

    def test_is_separated_number(self) -> None:
        """
        Tests function `is_separated_number()`.

        :return: nothing
        """
        for value in ["0", "123", "1.234", "1.234.567.890"]:
            self.assertTrue(self.__solution.is_separated_number(value), f"{value} should be valid")
        for value in ["", "1234", "12.34", "123.", ".123", "123.", "abc"]:
            self.assertFalse(self.__solution.is_separated_number(value), f"{value} should be invalid")


if __name__ == "__main__":
    unittest.main()
