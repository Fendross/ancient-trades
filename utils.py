import random

# CONSTANTS
RESOURCE_NAMES = ["Gold", "Silver", "Copper", "Iron", "Aluminum", "Lead", "Zinc", "Tin", "Nickel", "Uranium", "Oil", "Natural Gas", "Coal", "Water", "Timber", "Sand", "Gravel", "Lime", "Salt", "Phosphates", "Clay", "Diamonds", "Bauxite", "Manganese", "Uranium", "Platinum", "Titanium"]
CITY_NAMES = ["Rome", "Athens", "Babylon", "Memphis", "Thebes", "Ur", "Uruk", "Hattusa", "Knossos", "Mycenae", "Troy", "Byzantium", "Carthage", "Jerusalem", "Lisbon", "Alexandria", "Antioch", "Constantinople", "Damascus", "Jerusalem", "Baghdad", "Cairo", "Medina", "Cusco", "Tenochtitlan", "Teotihuacan"]
CIVILIZATION_NAMES = ["Sumer", "Akkad", "Egypt", "Indus Valley", "Chinese", "Greek", "Roman", "Mayan", "Inca", "Aztec", "Persian Empire", "Gupta Empire", "Maurya Empire", "Han Empire", "Roman Empire", "Byzantine Empire", "Holy Roman Empire", "Islamic Caliphate", "Mongol Empire", "Inca Empire", "Aztec Empire", "British Empire", "French Empire", "Spanish Empire", "Russian Empire", "United States", "Japanese"]


def generate_random_city_name():
    '''
    @return type=string A randomly chosen name from CITY_NAMES
    '''
    return random.choice(CITY_NAMES)
