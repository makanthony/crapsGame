# -*- coding: utf-8 -*-
"""
Dec 1 2022

Anthony Mak

Craps Table Final

After running the test 20 times, wins averaged at 12.35
highest was 24, lowest was 8
247 total wins out of 3000 total games
0.0823% win rate
"""

import random as rand

def roll():
    roll = rand.randint(1, 6)
    return roll

cash = 150
winnings = 0
losses = 0
while cash > 0:

    bet = input("What are you betting on? ")
    bet = int(bet)
    #bet = 7
    
    #bet = rand.randint(2, 12)
    print(bet)
    
    dice1 = roll()
    dice2 = roll()

    result = dice1 + dice2
    #result = 7
    print(result, '\n')
    if result == bet:
        winnings += 1
    else:
        losses +=1
        
    cash -= 1
    
print("After playing 150 times, you've won {} times, and lost {} times".format(winnings, losses))
if winnings > losses:
    print("Congratulations, you've won $", winnings)
elif losses > winnings:
    print("Sorry! You lost $", losses)
else:
    print("Wow! You broke even")