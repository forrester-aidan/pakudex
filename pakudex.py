from pakuri import Pakuri  # Imports the pakuri module


class Pakudex:  # Initializes the Pakudex class
    def __init__(self):  # Constructor
        self.pakudex = []

    def get_species_list(self):  # Returns a list of the names of species in the Pakudex
        names = []

        if len(self.pakudex) == 0:
            return None
        else:
            x = 0
            while x < len(self.pakudex):
                critter = self.pakudex[x]
                names.append(critter.get_species())
                x += 1

        return names

    def get_stats(self, species: str):  # Returns the level, cp, and hp of a given Pakuri
        if len(self.pakudex) == 0:
            return None
        else:
            for value in self.pakudex:
                if value.get_species() == species:
                    level = int(value.level)
                    stats = [level, value.cp, value.hp]
                    return stats

            return None

    def sort_pakuri(self):  # Sort the Pakuri by name alphabetically
        index = 0
        while index < len(self.pakudex):
            if index + 1 == len(self.pakudex):
                x = 0
                while x < len(self.pakudex):
                    if self.pakudex[x].get_species() < self.pakudex[x + 1].get_species() and x + 2 == len(self.pakudex):
                        return self.pakudex
                    elif self.pakudex[x].get_species() < self.pakudex[x + 1].get_species() and x + 2 != len(
                            self.pakudex):
                        x += 1
                    else:
                        index = 0
                        break
            else:
                pakuri = self.pakudex[index]
                nextPakuri = self.pakudex[index + 1]

                if pakuri.get_species() > nextPakuri.get_species():
                    y = self.pakudex[index + 1]
                    self.pakudex[index + 1] = self.pakudex[index]
                    self.pakudex[index] = y
                    index += 1

                else:
                    index += 1

    def add_pakuri(self, species: str, level: str):  # Create a new Pakuri object and adds it to the Pakudex
        self.pakudex.append(Pakuri(species, int(level)))
        return True

    def remove_pakuri(self, species: str):  # Removes a previously instated Pakuri from Pakudex
        for value in self.pakudex:
            if value.get_species() == species:
                self.pakudex.remove(value)
                return True

        return False

    def evolve_species(self, species):  # Evolves the given Pakuri
        for value in self.pakudex:
            if value.get_species() == species:
                value.double_level()
                value.set_attack(value.get_attack() + 1)
                return True
        return False


def print_menu():  # Prints the main menu
    print("\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Remove Pakuri"
          "\n5. Evolve Pakuri\n6. Sort Pakuri\n7. Exit\n")


def main():  # Main method that runs the menu
    p = Pakudex()
    x = 0

    print("Welcome to Pakudex: Tracker Extraordinaire!")  # Introduction
    while x < 1:
        print_menu()
        option = input("What would you like to do? ")
        print("")

        if not option.isnumeric():  # Checks for alphabetic characters
            print("Unrecognized menu selection!")

        elif int(option) == 1:  # List Pakuri
            if len(p.pakudex) == 0:
                print("No Pakuri currently in the Pakudex!")
            else:
                listNumber = 1
                index = 0

                print("Pakuri in Pakudex: ")
                while index < len(p.pakudex):
                    print(str(listNumber) + ". " + p.get_species_list()[index])
                    listNumber += 1
                    index += 1

        elif int(option) == 2:  # Show Pakuri
            speciesName = input("Enter the name of the species to display: ")

            if len(p.pakudex) == 0:
                print("Error: No such Pakuri!")
            elif speciesName in p.get_species_list():
                stats = p.get_stats(speciesName)
                print("\nSpecies: " + speciesName)
                print("Level: " + str(stats[0]))
                print("CP: " + str(stats[1]))
                print("HP: " + str(stats[2]))
            else:
                print("Error: No such Pakuri!")

        elif int(option) == 3:  # Add Pakuri
            y = 0

            addSpecies = input("Species: ")

            if len(p.pakudex) == 0:
                while y < 1:
                    addLevel = input("Level: ")
                    if not addLevel.isnumeric() and not addLevel.startswith("-"):
                        print("Invalid input!")
                    elif addLevel.startswith("-"):
                        print("Level cannot be negative.")
                    else:
                        p.add_pakuri(addSpecies, addLevel)
                        print("Pakuri species " + addSpecies + " (level " + addLevel + ") added!")
                        y += 1

            elif addSpecies in p.get_species_list():
                print("Error: Pakudex already contains this species!")

            else:
                while y < 1:
                    addLevel = input("Level: ")
                    if not addLevel.isnumeric() and not addLevel.startswith("-"):
                        print("Invalid input!")
                    elif addLevel.startswith("-"):
                        print("Level cannot be negative.")
                    else:
                        p.add_pakuri(addSpecies, addLevel)
                        print("Pakuri species " + addSpecies + " (level " + addLevel + ") added!")
                        y += 1
        elif int(option) == 4:  # Remove Pakuri
            removeSpecies = input("Enter the name of the Pakuri to remove: ")

            if len(p.pakudex) == 0:
                print("Error: No such Pakuri!")
            elif removeSpecies in p.get_species_list():
                p.remove_pakuri(removeSpecies)
                print("Pakuri " + removeSpecies + " removed.")
            else:
                print("Error: No such Pakuri!")

        elif int(option) == 5:  # Evolve Pakuri
            evolveSpecies = input("Enter the name of the species to evolve: ")

            if len(p.pakudex) == 0:
                print("Error: No such Pakuri!")
            elif evolveSpecies in p.get_species_list():
                p.evolve_species(evolveSpecies)
                print(evolveSpecies + " has evolved!")
            else:
                print("Error: No such Pakuri!")

        elif int(option) == 6:  # Sort Pakuri
            if len(p.pakudex) != 0:
                p.sort_pakuri()
                print("Pakuri have been sorted!")
            else:
                print("Pakuri have been sorted!")

        elif int(option) == 7:  # Exit
            print("Thanks for using Pakudex! Bye!")
            quit()

        else:
            print("Unrecognized menu selection!")


if __name__ == '__main__':  # Begins the program
    main()
