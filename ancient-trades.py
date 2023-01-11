'''
ANCIENT TRADES, an exam example/problem set from Programming II (specifications are written in Java).
Reference File: ./exam-example.pdf
Goal: to practice classes and python basics.
'''
import random

RESOURCE_NAMES = ["Gold", "Silver", "Copper", "Iron", "Aluminum", "Lead", "Zinc", "Tin", "Nickel", "Uranium", "Oil", "Natural Gas", "Coal", "Water", "Timber", "Sand", "Gravel", "Lime", "Salt", "Phosphates", "Clay", "Diamonds", "Bauxite", "Manganese", "Uranium", "Platinum", "Titanium"]
CITY_NAMES = ["Rome", "Athens", "Babylon", "Memphis", "Thebes", "Ur", "Uruk", "Hattusa", "Knossos", "Mycenae", "Troy", "Byzantium", "Carthage", "Jerusalem", "Lisbon", "Alexandria", "Antioch", "Constantinople", "Damascus", "Jerusalem", "Baghdad", "Cairo", "Medina", "Cusco", "Tenochtitlan", "Teotihuacan"]
CIVILIZATION_NAMES = ["Sumer", "Akkad", "Egypt", "Indus Valley", "Chinese", "Greek", "Roman", "Mayan", "Inca", "Aztec", "Persian Empire", "Gupta Empire", "Maurya Empire", "Han Empire", "Roman Empire", "Byzantine Empire", "Holy Roman Empire", "Islamic Caliphate", "Mongol Empire", "Inca Empire", "Aztec Empire", "British Empire", "French Empire", "Spanish Empire", "Russian Empire", "United States", "Japanese"]

# UTILS
def generate_random_resource():
    '''
    @return type=Resource A Resource object with random arguments
    '''
    return Resource(random.choice(RESOURCE_NAMES), random.randint(10, 500))

def generate_random_city_name():
    '''
    @return type=string A randomly chosen name from CITY_NAMES
    '''
    return random.choice(CITY_NAMES)
     
def generate_random_civilization(num_foundings=1):
    '''
    @return type=Civilization A Civilization with random name, random cities (one of each subclass)
    @param num_foundings type=int Number of city foundings. If None, have at least one founding
    '''
    c = Civilization(random.choice(CIVILIZATION_NAMES))
    for i in range(num_foundings):
        c.found_city(generate_random_city_name(), 'e')
        c.found_city(generate_random_city_name(), 'i')
    c.make()
    return c


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
        @notice Checks if self is greater than other
        @param other type=Resource A Resource to compare to self
        '''
        if self != other:
            if self.get_price() > other.get_price() or self.get_name() > other.get_name():
                return True
        return False

    def __repr__(self):
        return self.get_name() + ": " + str(self.get_price())

    def __str__(self):
        return self.get_name() + ": " + str(self.get_price())

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


# City SUBCLASSES
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


# Civilization Class
class Civilization(object):
    def __init__(self, name):
        '''
        @param cities type=list List of City or its subclasses EconomyCity, IndustrialCity
        @param name type=string Name of the Civilization
        @param treasury type=int Wealth of the Civilization
        @param stock type=list List of Resource
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
        @param other type=Civilization A Civilization to compare to self
        @return has_traded type=bool True if the exchange happened, False otherwise
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
                    print(other.get_name() + 'has not enough funds to close the trade.')
                    new_stock.append(resource)
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
        @param civilizations type=list List of Civilization
        '''
        self.civilizations = civilizations

    def get_civilizations(self):
        return self.civilizations

    def trade(self, iterations):
        richest = self.civilizations[0]
        for n in range(iterations):
            for c in self.civilizations:
                c.make()
            for c in self.civilizations:
                for k in self.civilizations:
                    has_traded = c.sell_resource_to(k)
                    if has_traded:
                        print(c.get_name() + 'has traded with ' + k.get_name())
                        break
                if c.get_treasury() > richest.get_treasury():
                    richest = c
        return richest

    # TODO: write the simulation of the entire program
    def play_simulation(self):
        pass

    def __str__(self):
        result = ''
        for civilization in self.get_civilizations():
            result += str(civilization) + '\n'
        return result


# TEST FUNCTIONS
def test_civilization_trades(num_foundings):
    '''
    @notice Tests the Civilization.sell_resource_to(self, other) method
    @param num_foundings type=int Number of city foundings
    '''
    c1 = generate_random_civilization(num_foundings)
    c2 = generate_random_civilization(num_foundings)
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

def test_history_trade(num_civilizations, num_foundings, iterations):
    '''
    @notice Tests the History.trade(self, iterations) method
    @param num_civilizations type=int Number of civilizations of the simulation
    @param num_foundings type=int Number of city foundings
    @param iterations type=int Number of iterations
    '''
    civilizations = []
    for n in range(num_civilizations):
        civilizations.append(generate_random_civilization(num_foundings))
    
    h = History(civilizations)
    print("Here's the list of civilizations in this simulation:\n" + str(h))
    print("---------------------------------")
    print("During the trading period...")
    richest = h.trade(iterations)
    print("---------------------------------")
    print("List of civilization's treasuries:")
    for c in h.get_civilizations():
        print(c.get_name() + ' has ' + str(c.get_treasury()))
    print("---------------------------------")
    return 'The richest civilization of the simulation is:\n' + str(richest)


# MAIN PROGRAM
if __name__ == '__main__':
    # Testing variables
    num_civilizations = 10
    num_foundings = 2
    iterations = 5

    # Civilization class testing
    test_civilization_trades(num_foundings)

    # History class testing 
    print(test_history_trade(num_civilizations, num_foundings, iterations))
