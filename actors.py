import random


class Wizard:
    def __init__(self, name, wizard_level):
        self.name = name
        self.level = wizard_level

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(self.name, creature.name))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint (1, 12) * creature.level

        print("You roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has triumphed over {} \n".format(creature.name))
            return True
        else:
            print("The Wizard has been defeated!!")
            return False

    def run(self, creature):
        print("{} decided to run from {}".format(self.name, creature))
        my_run = random.randint(1,6) * self.level
        creature_run = random.randint(1,6) * self.level

        print("Your decided to run and rolled a {}....".format(my_run))
        print("{} chased you and rolls {}....".format(creature.name, creature_run))

        if my_run >= creature_run:
            print("{}, the Wizard has out run {}...".format(self.name, creature.name))
            return True
        else:
            print("{}, caught you and Defeated {}, you lose.". format(creature.name, self.name))
            return False


class Creature:
    def __init__(self, name, creature_level):
        self.name = name
        self.level = creature_level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )