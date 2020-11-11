class Customer:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def buy_drink(self, drink, wallet):
        wallet = wallet =- drink
        return wallet

        


        