
import time
import numpy as np
import sys

# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class champion:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars


    def fight(self, champion2):
        # Allow twochampion to fight each other

        # Print fight information
        print("----championE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{champion2.name}")
        print("TYPE/", champion2.types)
        print("ATTACK/", champion2.attack)
        print("DEFENSE/", champion2.defense)
        print("LVL/", 3*(1+np.mean([champion2.attack,champion2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Earth']
        for i,k in enumerate(version):
            if self.types == k:
                # Both are same type
                if champion2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # champion2 is STRONG
                if champion2.types == version[(i+1)%3]:
                    champion2.attack *= 2
                    champion2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # champion2 is WEAK
                if champion2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    champion2.attack /= 2
                    champion2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        # Now for the actual fighting...
        # Continue whilechampion still have health
        while (self.bars > 0) and (champion2.bars > 0):
            # Print the health of each champion
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{champion2.name}\t\tHLTH\t{champion2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            champion2.bars -= self.attack
            champion2.health = ""

            # Add back bars plus defense boost
            for j in range(int(champion2.bars+.1*champion2.defense)):
                champion2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{champion2.name}\t\tHLTH\t{champion2.health}\n")
            time.sleep(.5)

            # Check to see if champion has been defeated
            if champion2.bars <= 0:
                delay_print("\n..." + champion2.name + ' Your champion has been DEFEATED! ')
                break

            # champion2s turn

            print(f"Go {champion2.name}!")
            for i, x in enumerate(champion2.moves):
                print(f"{i+1}.", x)
            index = int(input('Choose your attack!  '))
            delay_print(f"\n{champion2.name} used {champion2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= champion2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{champion2.name}\t\tHLTH\t{champion2.health}\n")
            time.sleep(.5)

            # Check to see ifchampion fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + 'Your Champion has been DEFEATED!')
                break







if __name__ == '__main__':
    #Available Champions 
    Heilos = champion('Helios, Titan personification of the Sun, drives his chariot across the sky.', 'Fire', ['Metorstrike', 'Heat Wave', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Hephaestus = champion('Hephaestus, god of blacksmiths, crafting, fire, and volcanoes.', 'Fire', ['Phen', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
    Artemis = champion('Artemis ', 'Earth', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})
    Gaia  = champion('Gaia', 'Earth', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':1000, 'DEFENSE':1500})
   Poseidon  = champion('P', 'Earth', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':1200, 'DEFENSE':800})



    Charizard.fight(Squirtle) # Get them to fight

list_Champions = ["Helios, Titan personification of the Sun, drives his chariot across the sky.'", "Hephaestus, god of blacksmiths, crafting, fire, and volcanoes.", 'Artemis, Greek goddess of the hunt, the wilderness, wild animals, the Moon and chastity ', "Poseidon, god of the sea (and of water generally), earthquakes, and horses. "," "]
print("Welcome to the Battle of the gods, choose your Champion ")
Champion_1 = input("please enter choose champion #1: ", )
Champion_2 = input("Choose champion #2": )

Charizard.fight(Squirtle) # Let the  fight begin