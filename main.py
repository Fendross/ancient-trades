'''
ANCIENT TRADES, an exam example/problem set from Programming II (specifications are written in Java).
Reference File: ./exam-example.pdf
Goal: to practice classes and python basics.
'''
import random

RESOURCE_NAMES = ['Petrol', 'Gold', 'Silver', 'Bronze', 'Weapons', 'Canned Food', 'Milk', 'Corn', 'Uranium']
CITY_NAMES = ['Pretoria', 'Agrigento', 'Roma', 'Cartagine', 'Milano', 'Venezia', 'Napoli', 'Genova', 'Livorno', 'Termoli']

def generate_random_resource():
    '''
    TEMP FUNCTION (UTIL)
    @return: Resource with random arguments
    '''
    name = random.choice(RESOURCE_NAMES)
    del(RESOURCE_NAMES[RESOURCE_NAMES.index(name)])
    return Resource(name, random.randint(10, 101))

def generate_random_city_name():
    '''
    TEMP FUNCTION (UTIL)
    @return: string name, random name
    '''
    name = random.choice(CITY_NAMES)
    del(CITY_NAMES[CITY_NAMES.index(name)])
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
        return 'Industrial City of ' + self.get_name() + ' that produces ' + str(self.get_resource())

    def __str__(self):
        return 'Industrial City of ' + self.get_name() + ' that produces ' + str(self.get_resource())


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

    def sell_resource_to(self, other):
        '''
        @param other: Civilization
        @return: bool, True if the exchange happened or False otherwise
        '''
        pass

    def __str__(self):
        return self.get_name() + ' civilization:\nCities: ' + str(self.get_cities()) \
               + '\nValue of treasury: ' + str(self.get_treasury()) + '\nResources: ' + str(self.get_stock())


def test_civilization_class(name):
    c = Civilization(name)
    for i in range(5):
        c.found_city(generate_random_city_name(), 'e')
        c.found_city(generate_random_city_name(), 'i')
    print("Status of the civilization " + name + " after initialisation:\n" + str(c))
    print()
    c.make()
    print("Status of the civilization " + name + " after producing:\n" + str(c))


if __name__ == '__main__':
    print("---------------------------------")

    # Civilization test
    test_civilization_class('Romans')
    print("---------------------------------")
