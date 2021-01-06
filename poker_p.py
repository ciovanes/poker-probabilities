""" 
Created on Wed Jan 6 22:47:36 2021
@author: spanishkukli
@summary: The probabilities that you get the following poker plays in x attemps and x number of cards in the deck (max. 52 cards).
"""

import random 
from collections import Counter


#--Plays--
#Two cards of the same rank.
def pair(vals):
    for val in vals:
        if val == 2:
            return 1
            
    return 0

#Two different pairs.
def two_pair(vals):
    x = 0
    for val in vals:
        if val == 2:
            x += 1
    if x == 2:
        return 1
    else:
        return 0

#Three cards of the same rank.
def three_of_a_kind(vals):
    for val in vals:
        if val == 3:
            return 1

    return 0 

#Five cards in a sequence, but not of the same suit.
def straight(vals):
    x = []
    for val in vals:
        try:
            x.append(int(val))  

        except ValueError:
            if val == "J":
                x.append(11)
            elif val == "Q":
                x.append(12)
            elif val == "K":
                x.append(13)
            elif val == "AS":
                x.append(1)
                x.append(14) 

    x.sort()

    for i in range(len(x) - 1):
        if x[i] != x[i + 1] - 1:
            if x[i] != 1:
                return 0
        i +=1
    return 1

#Any five cards of the same suit, but not in a sequence.
def flush(suits):
    x = suits[0]
    for suit in suits:
        if x != suit:
            return 0 

    return 1

#Three of a kind with a pair.
def full_house(vals):
    a_pair = pair(vals)
    a_three_of_a_kind = three_of_a_kind(vals)

    if a_pair == 1 and a_three_of_a_kind == 1:
        return 1
    else:
        return 0 

#All four cards of the same rank.
def four_of_a_kind(vals):
    for val in vals:
        if val == 4:
            return 1

    return 0

#Five cards in a sequence, all in the same suit.
def straight_flush(vals, suits):
    a_straight = straight(vals)
    a_flush = flush(suits)
    if a_straight == 1 and a_flush == 1:
        return 1
    else:
        return 0

#A, K, Q, J, 10, all the same suit.
def royal_flush(vals, suits):
    a_straight = straight_flush(vals, suits)

    if a_straight == 1:
        if "10" in vals and "AS" in vals:
            return 1
        else:
            return 0
            
    return 0

#Make a deck with 52 cards.
def make_deck():
    SUITS = ["spades", "hearts", "diamonds", "clubs"]
    VALUES = ["AS", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))

    return deck 

#Get a random hand.
def get_hand(deck, deck_size):
    hand = random.sample(deck, deck_size)
    return hand

#Calculate P
def plays_p(hands):
    plays = {
        'pair': 0,              
        'two pair': 0,          
        'three of a kind': 0,   
        'straight': 0,          
        'flush': 0,             
        'full house': 0,        
        'four of a kind': 0,    
        'straight flush': 0,    
        'royal flush': 0        
    }

    for hand in hands:
        values = []
        suits = []
        for card in hand:
            values.append(card[1])
            suits.append(card[0])

        counter = dict(Counter(values))
       
        plays["pair"] += pair(counter.values())
        plays["two pair"] += two_pair(counter.values())
        plays["three of a kind"] += three_of_a_kind(counter.values())
        plays["straight"] += straight(values)
        plays["flush"] += flush(suits)
        plays["full house"] += full_house(counter.values())
        plays["four of a kind"] += four_of_a_kind(counter.values())
        plays["straight flush"] += straight_flush(values, suits)
        plays["royal flush"] += royal_flush(values, suits)
    #Print P
    for play in plays.keys():
        P = plays[play] / attempts
        print(f"P: {P}, to get {play} in {attempts} attempts.")


#Main
def main(deck_size, attempts):
    deck = make_deck()
    hands = []
    
    for _ in range(attempts):
        hand = get_hand(deck, deck_size)
        hands.append(hand)
        print(hand)

    plays_p(hands)



if __name__ == "__main__":
    deck_size = int(input("Deck size?: "))
    attempts = int(input("Attempts?: "))
    #print(deck_size, attempts)
    
    main(deck_size, attempts)
