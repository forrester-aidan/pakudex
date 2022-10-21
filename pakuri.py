import math


class Pakuri():
    def __init__(self, species: str, level: int):
        self.__species = species
        self.__level = level
        self.__attack = int(len(species) * 7 + 11) % 16
        self.__defense = int(len(species) * 5 + 17) % 16
        self.__stamina = int(len(species) * 6 + 13) % 16
        self._cp = int(math.floor(self.__attack * math.sqrt(self.__defense) * math.sqrt(self.__stamina) * self.__level * 0.08))
        self._hp = int(math.floor(self.__stamina * self.__level / 6))

    @property
    def cp(self):
        return self._cp

    @property
    def hp(self):
        return self._hp

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, newLevel: int):
        self.__level = newLevel

    def get_species(self):
        return self.__species

    def get_attack(self):
        return self.__attack

    def get_defense(self):
        return self.__defense

    def get_stamina(self):
        return self.__stamina

    def double_level(self):
        self.__level = self.__level * 2
        self._hp = int(math.floor(self.__stamina * self.__level / 6))

    def set_attack(self, new_attack: int):
        self.__attack = new_attack
        self._cp = int(
            math.floor(self.__attack * math.sqrt(self.__defense) * math.sqrt(self.__stamina) * self.__level * 0.08))




