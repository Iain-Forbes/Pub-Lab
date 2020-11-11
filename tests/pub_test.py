import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub('Mos Eisley Cantina', 100, ["Jabba Juice", "Spotchka", "Blackroot"])

    def test_pub_name(self):
        self.assertEqual('Mos Eisley Cantina', self.pub.name)

    def test_till_amount(self):
        self.assertEqual(100, self.pub.till)

    def test_drink(self):
        self.assertEqual(["Jabba Juice", "Spotchka", "Blackroot"], self.pub.drink)

    def test_increase_till(self):
        self.pub.increase_till(5)
        self.assertEqual(105, self.pub.till)

        
        
