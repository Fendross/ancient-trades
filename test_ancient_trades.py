'''
@notice History was not test-driven implemented
'''

from ancient_trades import *
from utils import *

def build_resource_stock(num_resources):
    n = 0
    while n < num_resources:
        generate_random_resource()
        n += 1
    print("Generated " + str(n) + " random resources!")


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

    print("Trading simulation started...\n")
    richest = h.commerce(iterations)
    print("---------------------------------")
    print("List of civilization's treasuries:")
    for c in h.get_civilizations():
        print(c.get_name() + ' has ' + str(c.get_treasury()))
    print("---------------------------------")
    return 'The richest civilization of the simulation is:\n' + str(richest)


if __name__ == '__main__':
    print("!!! TESTING SUITE FOR THE ANCIENT TRADES SIMULATION !!!\n")
    # Testing variables
    num_civilizations = 5
    num_foundings = 2
    iterations = 3
    num_resources = 10

    # Initialise the resources stock to pick from
    build_resource_stock(num_resources)
    print("---------------------------------")

    # Civilization class testing
    print("TESTING test_civilization_trades...\n")
    test_civilization_trades(num_foundings)
    print("---------------------------------")

    # History class testing 
    print("TESTING test_history_trade...\n")
    print(test_history_trade(num_civilizations, num_foundings, iterations))