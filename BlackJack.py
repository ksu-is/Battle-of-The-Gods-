
import time
import numpy as np
import sys

# Delay printing

def delay_print(s): # Gives the fell of playing on a oldschool gaming system like a nintendo
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class champ:
    def __init__(champ1, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        champ1.name = name
        champ1.types = types
        champ1.moves = moves
        champ1.attack = EVs['ATTACK']
        champ1.defense = EVs['DEFENSE']
        champ1.health = health
        champ1.bars = 20 # Amount of health bars


    def fight(champ1, champ2):
        # Allow two champ to fight each other

        # Print fight information
        print("-----BATTLE-----")
        print(f"\n{champ1.name}")
        print("TYPE/", champ1.types)
        print("ATTACK/", champ1.attack)
        print("DEFENSE/", champ1.defense)
        print("LVL/", 10*(1+np.mean([champ1.attack,champ1.defense])))
        print("\nVS")
        print(f"\n{champ2.name}")
        print("TYPE/", champ2.types)
        print("ATTACK/", champ2.attack)
        print("DEFENSE/", champ2.defense)
        print("LVL/", 10*(1+np.mean([champ2.attack,champ2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Earth']
        for i,k in enumerate(version): # enumerate() to get a counter and the value from the iterable at the same time!
            if champ1.types == k:
                # Both are same type example Fire vs Fire 
                if champ2.types == k:
                    string_1_attack = '\nIts not very effective...\n'
                    string_2_attack = '\nIts not very effective...\n'

                # champ2 is STRONG
                if champ2.types == version[(i+1)%3]:
                    # Ex: Water attacks fire or fire attacks earth 
                    champ2.attack *= 2
                    champ2.defense *= 2
                    champ1.attack /= 2
                    champ1.defense /= 2
                    string_1_attack = '\nIts not very effective...\n'
                    string_2_attack = '\nIts super effective!\n'

                # champ2 is WEAK
                if champ2.types == version[(i+2)%3]:
                    # fire attacks water 
                    champ1.attack *= 2
                    champ1.defense *= 2
                    champ2.attack /= 2
                    champ2.defense /= 2
                    string_1_attack = '\nIts super effective!\n'
                    string_2_attack = '\nIts not very effective...\n'


        # actual fighting...
        # Continue while champ still have health
        while (champ1.bars > 0) and (champ2.bars > 0):
            # Print the health of each champ
            print(f"\n{champ1.name}\nHLTH\t{champ1.health}")
            print(f"\n{champ2.name}\nHLTH\t{champ2.health}\n")

            print(f"You have been summoned {champ1.name}!")
            for i, x in enumerate(champ1.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{champ1.name} used {champ1.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            champ2.bars -= champ1.attack
            champ2.health = ""

            # Add back bars plus defense boost
            for j in range(int(champ2.bars+.1*champ2.defense)):
                champ2.health += "="

            time.sleep(1)
            print(f"\n{champ1.name}\nHLTH\t{champ1.health}")
            print(f"\n{champ2.name}\nHLTH\t{champ2.health}\n")
            time.sleep(.5)

            # Check to see if champ fainted
            if champ1.bars <= 0:
                delay_print("\n..." + champ1.name + ' defeated.')
                break

            # champ2s turn

            print(f"You have been summoned! {champ2.name}!")
            for i, x in enumerate(champ2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{champ2.name} used {champ2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            champ1.bars -= champ2.attack
            champ1.health = ""

            # Add back bars plus defense boost
            for j in range(int(champ1.bars+.1*champ1.defense)):
                champ1.health += "="

            time.sleep(1)
            print(f"{champ1.name}\nHLTH\t{champ1.health}")
            print(f"{champ2.name}\nHLTH\t{champ2.health}\n")
            time.sleep(.5)

            # Check to see if champ fainted
            if champ2.bars <= 0:
                delay_print("\n..." + champ2.name + ' defeated.')
                break







if __name__ == '__main__':
    #Create champ
    Helios = champ('Helios, god of the sun', 'Fire', ['Sun Strike', 'Heat Wave', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Hephaestus = champ('Hephaestus, god of blacksmiths, crafting, fire, and volcanoes.', 'Fire', ['Fire Breath', 'Axe Strike', 'Metor Strike', 'Heat Stroke'],{'ATTACK': 10, 'DEFENSE':10})
    Artemis = champ('Artemis, greek goddess of the hunt, the wilderness, wild animals, the Moon and chastity', 'Earth', ['Vine Wip', 'Arrow Strike', 'Sneak attack', 'Frenzy'],{'ATTACK':8, 'DEFENSE':12})

    Gia = champ('Gaia, titan personification of the Earth and one of the Greek primordial deities. Gaia is the ancestral mother of all life.', 'Earth', ['Earthquake', 'Tornado', 'Landslide', 'Quicksand'],{'ATTACK':10, 'DEFENSE':12})
    Poseidon= champ('Poseidon, god of the sea , earthquakes, and horses.', 'Water', ['Trident Slash', 'Earthquake', 'Headbutt', 'Tsunami'],{'ATTACK': 9, 'DEFENSE':12})
    Amhitrite = champ('Amhitrite, goddess of the sea, wife of the god Poseidon', 'Water', ['Trident Slash', 'Hurricane', 'Whale Punch', 'Shark attack'],{'ATTACK':10, 'DEFENSE':10})



    Gia.fight(Amhitrite) # Get them to fight

