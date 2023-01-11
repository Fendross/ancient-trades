'''
ANCIENT TRADES, an exam example/problem set from Programming II (specifications are written in Java).
Reference File: ./exam-example.pdf
Goal: to practice classes and python basics.
'''
import random

RESOURCE_NAMES = ['Petrol', 'Gold', 'Silver', 'Bronze', 'Weapons', 'Canned Food', 'Milk', 'Corn', 'Uranium']
CITY_NAMES = ['Pretoria', 'Agrigento', 'Roma', 'Cartagine', 'Milano', 'Venezia', 'Napoli', 'Genova', 'Livorno', 'Termoli']
CIVILIZATION_NAMES = [
    "Sumer",
    "Akkad",
    "Egypt",
    "Indus Valley",
    "Chinese",
    "Greek",
    "Roman",
    "Mayan",
    "Inca",
    "Aztec",
    "Persian Empire",
    "Gupta Empire",
    "Maurya Empire",
    "Han Empire",
    "Roman Empire",
    "Byzantine Empire",
    "Holy Roman Empire",
    "Islamic Caliphate",
    "Mongol Empire",
    "Inca Empire",
    "Aztec Empire",
    "British Empire",
    "French Empire",
    "Spanish Empire",
    "Russian Empire",
    "United States",
    "Japanese"
]


def generate_random_resource():
    '''
    TEMP FUNCTION (UTIL)
    @return: Resource with random arguments
    '''
    name = random.choice(RESOURCE_NAMES)
    return Resource(name, random.randint(10, 20))

def generate_random_city_name():
    '''
    TEMP FUNCTION (UTIL)
    @return: string name, random name
    '''
    name = random.choice(CITY_NAMES)
    return name

def generate_random_civilization_name():
    name = random.choice(CIVILIZATION_NAMES)
    return name

# Resource Class
class Resource(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def greater_than(self, other):
        '''
        @notice: checks if self is greater than other
        @param other: Resource
        '''
        if self != other:
            if self.get_price() > other.get_price() or self.get_name() > other.get_name():
                return True
        return False

    def __repr__(self):
        return self.get_name() + " of price per unit: " + str(self.get_price())

    def __str__(self):
        return self.get_name() + ", " + str(self.get_price())

    def __eq__(self, other):
        if self.get_price() != other.get_price() or self.get_name() != other.get_name():
            return False
        return True


# Abstract Base Class City
class City(object):
    def __init__(self, name):
        self.name = name
    
    def produce(c):
        pass


class IndustrialCity(City):
    def __init__(self, name, resource):
        super().__init__(name)
        self.resource = resource
    
    def get_name(self):
        return self.name

    def get_resource(self):
        return self.resource

    def produce(self, c):
        c.add_resource(self.resource)

    def __repr__(self):
        return 'Industrial City of ' + self.get_name() + ' which produces ' + str(self.get_resource())

    def __str__(self):
        return 'Industrial City of ' + self.get_name() + ' which produces ' + str(self.get_resource())


class EconomyCity(City):
    def __init__(self, name):
        super().__init__(name)

    def get_name(self):
        return self.name

    def produce(self, c):
        c.treasury += 1000

    def __repr__(self):
        return 'Economy City of ' + self.get_name()

    def __str__(self):
        return 'Economy City of ' + self.get_name()


class Civilization(object):
    def __init__(self, name):
        '''
        @param cities: list of City
        @param name: string, the name of the Civilization
        @param treasury: int, the money possessed by the instance
        @param stock: list of Resource
        '''
        self.name = name
        self.cities = []
        self.treasury = 0
        self.stock = []

    def get_name(self):
        return self.name

    def get_cities(self):
        return self.cities

    def get_treasury(self):
        return self.treasury
    
    def get_stock(self):
        return self.stock

    def found_city(self, name, city_type):
        if city_type.lower() == 'i':
            resource = generate_random_resource()
            self.cities.append(IndustrialCity(name, resource))
        elif city_type.lower() == 'e':
            self.cities.append(EconomyCity(name))

    def add_resource(self, resource):
        self.stock.append(resource)

    def add_money(self, amount):
        self.treasury += amount

    def make(self):
        for city in self.cities:
            city.produce(self)
        
    def has(self, r):
        if r in self.get_stock():
            return True
        return False

    def has_double(self, r):
        if self.get_stock().count(r) > 1:
            return True
        return False

    def sell_resource_to(self, other):
        '''
        @param other: Civilization
        @return: bool, True if the exchange happened or False otherwise
        '''
        new_stock = []
        has_traded = False
        for resource in self.get_stock():
            if self.has_double(resource) and not other.has(resource):
                if other.get_treasury() >= resource.get_price():
                    other.add_resource(resource)
                    other.treasury -= resource.get_price()
                    self.treasury += resource.get_price()
                    has_traded = True
                else:
                    raise ValueError("Buyer treasury has not enough funds")
            else:
                new_stock.append(resource)
        self.stock = new_stock
        return has_traded

    def __repr__(self):
        return self.get_name() + ' civilization:\nCities: ' + str(self.get_cities()) \
               + '\nValue of treasury: ' + str(self.get_treasury()) + '\nResources: ' + str(self.get_stock())

    def __str__(self):
        return self.get_name() + ' civilization:\nCities: ' + str(self.get_cities()) \
               + '\nValue of treasury: ' + str(self.get_treasury()) + '\nResources: ' + str(self.get_stock())


class History(object):
    def __init__(self, civilizations):
        '''
        @param civilizations: list of Civilization
        '''
        self.civilizations = civilizations


def test_civilization_trades(name_1, name_2):
    '''
    @notice: tests the sell_resource_to method of the Civilization class
    '''
    c1 = Civilization(name_1)
    c2 = Civilization(name_2)
    for i in range(5):
        c1.found_city(generate_random_city_name(), 'e')
        c1.found_city(generate_random_city_name(), 'i')
        c1.add_resource(generate_random_resource())
        c2.found_city(generate_random_city_name(), 'e')
        c2.found_city(generate_random_city_name(), 'i')
        c2.add_resource(generate_random_resource())
    c2.make()
    print("Let's see if a trade can happen here...")
    print(c1)
    print("---------------------------------")
    print(c2)
    has_traded = c1.sell_resource_to(c2)
    print("---------------------------------")
    if has_traded:
        print("The trade has happened! Let's check the balances of the two Civilizations:")
        print(c1)
        print("---------------------------------")
        print(c2)    
    else:
        print("The trade didn't happen.")


if __name__ == '__main__':
    print("---------------------------------")

    # Civilization test
    # test_civilization('Romans')

    # Trading method test
    test_civilization_trades(generate_random_civilization_name(), generate_random_civilization_name())
    print("---------------------------------")
