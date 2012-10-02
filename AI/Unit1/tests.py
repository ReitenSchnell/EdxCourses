from unittest import TestCase
from buyLotsOfFruit import buyLotsOfFruit


class Tests(TestCase):
    def test_should_return_None_if_list_contains_unknown_fruit(self):
        result = buyLotsOfFruit([('apples', 2.0), ('some fruits', 3.0), ('limes', 4.0)])
        self.assertEqual(None, result)

    def test_should_return_price_of_list(self):
        result = buyLotsOfFruit([('apples', 2.0), ('pears', 3.0), ('limes', 4.0)])
        self.assertEqual(12.25, result)



