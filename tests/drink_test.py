import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestDrink(unittest.TestCase):
    def setUp(self):
       self.drink = Drink('Jabba Juice', 3, 56)

    def test_drink_has_name(self):
        self.assertEqual("Jabba Juice", self.drink.name)

    def test_price(self):
        self.assertEqual(3, self.drink.price)
    
    # def 
