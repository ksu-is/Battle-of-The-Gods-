#This is Eric's Blackjack Python casion game 

""" 
The goal of the game is to get as close to 21 as possible without going over.
It is players (up to 4) vs dealer. The players are dealt two cards face up,
and the dealer gets 1 card face up and 1 face down. Each player chooses "hit"
or "stay" to get another card or stop receiving car

"""
import random
import inspect
from time import sleep

class Chips:

    def __init__(self, bankroll=100):
        self.bankroll = bankroll
        self.bet = 0
        self.insurance_bet = 0

    def __str__(self):
        """when chips is printed, this will show"""
        return "PLAYER has: " + str(self.bankroll) + " chips."

    def lose_bet(self):
        """removes the bet from the bankroll if the player loses"""
        self.bankroll -= self.bet

    def win_bet(self):
        """adds the bet to the bankroll if the player wins"""
        self.bankroll += self.bet

    def lose_insurance_bet(self):
        """removes the insurance bet from the bankroll if the dealer does not have 21"""
        self.bankroll -= self.insurance_bet

    def win_insurance_bet(self):
        """adds twice the insurance bet to the bankroll if the dealer does have 21"""
        self.bankroll += self.insurance_bet * 2

    def win_blackjack(self):
        """adds 1.5x the bet to the bankroll if the player gets a natural blackjack,
        must use int() on self.bet here or else it will be turned into float"""
        self.bankroll += int(self.bet * 1.5)

#creates an instance of player for each player BEFORE the loop,
#so their chips do not get reset

GAME_CHIPS = Chips()