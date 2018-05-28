import random
import time

from actors import Wizard, Creature


def main():
    header()
    game_loop()


def header():
    print('---------------------------------')
    print('           Wizard Game')
    print('---------------------------------')
    print()


def game_loop():

    print("Welcome to the wonderful game of wizards and beasts.")
    hero_name = input('Please give your wizard a name? ')
    print("Welcome old wise and merciful " + hero_name)
    print()

    creatures = [
        Creature('Beast youngling', 1),
        Creature('Feeble Elmer', 2),
        Creature('Petty Goat', 4),
        Creature('King Goat', 6),
        Creature('Basic Demon', 10),
    ]

    hero = Wizard(hero_name, 1)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forrest...'
              .format(active_creature.name, active_creature.level))
        print()
        cmd = input('Do you [a]ttack, [r]un, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                time.sleep(5)
                print('The hero is revitalized!')
        elif cmd == 'r':
            hero.run(active_creature)
            print()
        elif cmd == 'l':
            print('The wizard {} takes a look around surroundings and sees: '
                  .format(hero.name))
            for c in creatures:
                print(' * a {} of level {}'.format( c.name, c.level))
        else:
            print("Ok, exiting....bye!".format(cmd))
            break

        if not creatures:
            print("You defeated all the creatures. All Hail {}".format(hero.name))
            break


if __name__ == '__main__':
    main()