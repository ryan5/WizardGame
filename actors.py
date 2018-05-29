import random


class Creature:
    def __init__(self, name, creature_level):
        self.name = name
        self.level = creature_level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_role(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(self.name, creature.name))

        my_roll = self.get_defensive_role()
        creature_roll = self.get_defensive_role()

        print("You roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("\nThe wizard has triumphed over {} \n".format(creature.name))
            return True
        else:
            print("The Wizard has been defeated!!")
            return False

    def run(self, creature):
        print("{} has run away from {}".format(self.name, creature))
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


class SmallCreature(Creature):
    def get_defensive_role(self):
        base_roll = super().get_defensive_role()
        return base_roll / 2


class MediumCreature(Creature):
    pass


class LargeCreature(Creature):
    def __init__(self, name, level, magic, fight):
        super().__init__(name, level)
        self.magic = magic
        self.fight = fight

    def get_defensive_role(self):
        base_roll = super().get_defensive_role()
        magic_modifier = 5 if self.magic else 1
        fight_modifier = self.fight / 10
        return base_roll * magic_modifier * fight_modifier