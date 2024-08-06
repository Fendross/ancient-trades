'''
ANCIENT TRADES, a practice problem set for the OOP paradigm.
Goal: to practice classes and python basics.
'''
import random
from utils import *

# UTILS
def generate_random_resource():
    '''
    @return type=Resource A Resource object with random arguments
    '''
    return Resource(random.choice(RESOURCE_NAMES), random.randint(10, 500))
     
def generate_random_civilization(num_foundings=1):
    '''
    @param num_foundings type=int Number of city foundings. If None, have at least one founding
    @return type=Civilization A Civilization with random name, random cities (one of each subclass)
    '''
    c = Civilization(random.choice(CIVILIZATION_NAMES))
    for i in range(num_foundings):
        c.found_city(generate_random_city_name(), 'e')
        c.found_city(generate_random_city_name(), 'i')
    c.make()
    return c


# Resource Class
class Resource(object):
    created_resources = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Resource.created_resources.append(self)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_random_created_resource():
        if Resource.created_resources == []:
            raise ValueError("Cannot get a random resource from an empty list")
        else:
            return random.choice(Resource.created_resources)

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


# Resource Subclass
class DerivedResource(Resource):
    def __init__(self, name, price, original):
        '''
        @param original type=Resource The original Resource that this instance is derived from
        '''
        super().__init__(name, price)
        self.original = original

    def get_original(self):
        return self.original

    def __repr__(self):
        return self.get_name() + " price " + str(self.get_price()) + " derived from " + str(self.get_original())

    def __str__(self):
        return self.get_name() + " price " + str(self.get_price()) + " derived from " + str(self.get_original())


# Abstract Base Class City
class City(object):
    def __init__(self, name):
        self.name = name
    
    def produce(c):
        pass


# City Subclasses
class IndustrialCity(City):
    def __init__(self, name, resource):
        super().__init__(name)
        self.resource = resource
    
    def get_name(self):
        return self.name

    def get_resource(self):
        return self.resource

    def produce(self, c):
        if type(self.resource) == DerivedResource:
            if not self.resource.get_original() in c.get_stock():
                raise Exception("Original resource not in the Civilization stock")
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

    def found_city(self, city_name, city_type):
        if city_type.lower() == 'i':
            resource = Resource.get_random_created_resource()
            self.cities.append(IndustrialCity(city_name, resource))
        elif city_type.lower() == 'e':
            self.cities.append(EconomyCity(city_name))

    def add_resource(self, resource):
        self.stock.append(resource)

    def add_money(self, amount):
        self.treasury += amount

    def make(self):
        for city in self.cities:
            # If city is trying to produce a DerivedResource without having the original in the stock, catch the exception and print an error message
            try:
                city.produce(self)
            except Exception:
                print("City " + city.get_name() + " is trying to produce " + str(city.get_resource()) + ", a derived resource without having the original one.")
        
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
                    print(other.get_name() + ' has not enough funds to close the trade.')
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
    def __init__(self, civilizations=[]):
        '''
        @param civilizations type=list List of Civilization
        '''
        self.civilizations = civilizations

    def get_civilizations(self):
        return self.civilizations

    def commerce(self, iterations):
        '''
        @notice Takes the Civilization of the History instance and for each iteration:
                - calls the make() method on each of them
                - for each Civilization, checks if it can trade with the others, and it can do it only once per iteration
                - if the current Civilization has more money than the one saved in the richest variable, it becomes the richest
        @param iterations type=int the number of loop iterations
        @return richest type=Civilization The richest Civilization
        '''
        richest = self.civilizations[0]
        for n in range(iterations):
            print("Trade cicle #" + str(n) + " ongoing...")
            if len(self.civilizations) <= 1:
                print("One or less civilization in the history, thus commerce cannot be initiated. Add more the next time!")
                return
            for c in self.civilizations:
                c.make()
            for c in self.civilizations:
                for k in self.civilizations:
                    has_traded = c.sell_resource_to(k)
                    if has_traded:
                        print(c.get_name() + ' has traded with ' + k.get_name())
                        break
                if c.get_treasury() > richest.get_treasury():
                    richest = c
            print("---------------------------------")
        return richest

    def play_simulation(self):
        '''
        @notice Runs the Civilization Builder CLI, which creates a Civilization and can add to it as many cities as the user wishes.
        '''
        # Starting treasury of each civilization
        initial_balance = 10000

        print("*** ANCIENT TRADES ***\nWhich civilization will be the richest?\n")
        print("---------------------------------\n")
        # Resource Creation Loop
        while True:
            resource_name = input("Enter the name of a new Resource, or type 'stop' to move forward:\n")
            if resource_name.lower() == 'stop':
                break
            else:
                resource_price = int(input("What is its price?: "))
                r = Resource(resource_name, resource_price)
                Resource.created_resources.append(r)
                response = input("Do you wish to also create a Derived Resource from " + resource_name + "? [y/n]\n")
                if response.lower() == 'y':
                    derived_name = input("Which name?\n")
                    derived_price = int(input("Which price?\n"))
                    Resource.created_resources.append(DerivedResource(derived_name, derived_price, r))
        
        # Civilization Builder
        while True:
            civilization_name = input("Enter the name of the new Civilization (blank if you want to stop):\n")
            if civilization_name == '':
                break
            else:
                cities_index = 0
                c = Civilization(civilization_name)
                # City Creation Loop
                while True:
                    city_name = input("Enter the name of a new City, or type 'stop' to move forward:\n")
                    city_type = ''
                    if city_name.lower() == 'stop':
                        break
                    else:
                        city_char = input("Of which type? 'i' for Industrial, 'e' cor Economy:\n")
                        if city_char == 'i':
                            city_type += 'Industrial'
                        elif city_char == 'e':
                            city_type += 'Economy'
                        else:
                            raise ValueError("City type not recognized")
                    c.found_city(city_name, city_char)
                    if city_char == 'i':
                        r = c.get_cities()[cities_index].get_resource()
                        print(c.get_name() + " founded " + city_name + ", a city of type " + city_type + ", which produces the resource " + r.get_name() + " (price " + str(r.get_price()) + ").")
                    elif city_char == 'e':
                        print(c.get_name() + " founded " + city_name + ", a city of type " + city_type + ".")
                    cities_index += 1
            c.add_money(initial_balance)
            self.civilizations.append(c)

        # Then, ask for how many iterations does the user want to make civilizations trade with each other
        n = int(input("Enter a number of iterations for the commerce:\n"))
        print("\nHistory of the commerce:\n")
        richest = self.commerce(n)
        print("The richest civilization of them all is...***" + richest.get_name() + "***\n")

    def __str__(self):
        result = ''
        for civilization in self.get_civilizations():
            result += str(civilization) + '\n'
        return result


# MAIN PROGRAM
if __name__ == '__main__':
    # TODO list of inputs?
    h = History()
    h.play_simulation()
