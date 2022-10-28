from abc import ABC, abstractmethod


class Exercises(ABC):
    """
    Defines static methods that should be implemented using regular expressions.
    """

    @staticmethod
    @abstractmethod
    def is_c_identifier(value: str) -> bool:
        """
        Ellenőrzi, hogy a megkapott sztring a C nyelv egy szabályos azonosítója vagy sem.

        Egy karaktersorozat akkor C azonosító, ha:

        * egy vagy több szóból áll
        * minden szó betűvel kezdődik és betűvel vagy számjeggyel folytatódhat
        * két szomszédos szót pontosan egy aláhúzás karakter választ el egymástól

        :param value: az ellenőrizendő érték
        :return: az ellenőrzés eredménye
        """

    @staticmethod
    @abstractmethod
    def is_email_address(value: str) -> bool:
        """
        Ellenőrzi, hogy a megkapott sztring egy szabályos email-cím vagy sem.

        Egy karaktersorozat akkor email-cím, ha:

        * pontosan egy kukac (`@`) szerepel benne
        * a kukac előtti rész legalább egy kisbetűt vagy kötőjelet tartalmaz
        * a kukac után pontosan pont (`.`) karakter szerepel benne
        * a kukac és a pont között legalább egy kisbetűt vagy kötőjelet tartalmaz
        * a pont után legalább két darab kisbetűt tartalmaz

        :param value: az ellenőrizendő érték
        :return: az ellenőrzés eredménye
        """

    @staticmethod
    @abstractmethod
    def is_home_address(value: str) -> bool:
        """
        Ellenőrzi, hogy a megkapott sztring egy szabályos lakcím vagy sem.

        Egy karaktersorozat akkor lakcím, ha:

        * négy darab decimális számjeggyel kezdődik
        * egy szóközzel folytatódik
        * egy legalább egy betűből álló, nagybetűvel kezdődő helységnévvel folytatódik
        * egy vesszővel folytatódik
        * legalább egy nagybetűvel kezdődő szóval folytatódik, melyek első betűje mindig nagy, előtte pedig egy szóköz található
        * egy szóközzel folytatódik
        * legalább egy decimális számjeggyel folytatódik
        * egy pont (`.`) karakterrel végződik

        :param value: az ellenőrizendő érték
        :return: az ellenőrzés eredménye
        """

    @staticmethod
    @abstractmethod
    def is_separated_number(value: str) -> bool:
        """
        Ellenőrzi, hogy a megkapott sztring egy ezresenként csoportosított számjegy-sorozatot tartalmaz vagy sem.

        Egy karaktersorozat akkor ír le egy ezresenként csoportosított számot, ha

        * csak pont (`.`) és decimális számjegyek szerepelnek benne
        * minden pont jobb oldalán három darab decimális számjegy szerepel
        * a legelső pont előtt legalább egy decimális számjegy szerepel
        * legfeljebb három számjegy követi egymást

        :param value: az ellenőrizendő érték
        :return: az ellenőrzés eredménye
        """
