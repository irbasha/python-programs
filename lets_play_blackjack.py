# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:51:01 2020

@author: irfan
"""

from random import shuffle

class Blackjack:
    """
    Blackjack class for black jackgame.
    
    methods: 
        card_value(self, card)     -> returns the rank of a card for the player/dealer
        hand_value(self, hand)     -> claculates and returns the total score value
        init_game(self)            -> initiates the game leads through it
    """

    def __init__(self):
        self.ranks = [_ for _ in range(2,11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
        self.suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
        self.deck = [[rank,suit] for rank in self.ranks for suit in self.suits]
        shuffle(self.deck)

    def card_value(self, card):
        rank = card[0]
        if rank in self.ranks[0:-4]:
            return int(rank)
        elif rank == 'ACE':
            return 11
        else:
            return 10

    def hand_value(self, hand):
        tmp_value = sum(self.card_value(_) for _ in hand)
        num_aces = len([_ for _ in hand if _[0] == 'ACE'])
    
        while num_aces > 0:
            if tmp_value > 21 and 'ACE' in self.ranks:
                tmp_value -= 10
                num_aces -= 1
            else:
                break

        if tmp_value < 21:
            return [str(tmp_value), tmp_value]
        elif tmp_value == 21:
            return ['Blackjack!', 21]
        else:
            return ['Bust!', 100]

    def init_game(self):
        player_in = True
        player_hand = [self.deck.pop(), self.deck.pop()]
        dealer_hand = [self.deck.pop(), self.deck.pop()]

        while player_in:
            current_score_str = '''\nYou are currently at %s\nwith the hand %s\n'''
            print(current_score_str % (self.hand_value(player_hand)[0], player_hand))

            if self.hand_value(player_hand)[1] == 100:
                break
        
            if player_in:
                response = int(input('Hit or stay? (Hit = 1, Stay = 0): '))

                if response:
                    player_in = True
                    new_player_card = self.deck.pop()
                    player_hand.append(new_player_card)
                    print('You draw %s' % new_player_card)
                else:
                    player_in = False

        player_score_label, player_score = self.hand_value(player_hand)
        dealer_score_label, dealer_score = self.hand_value(dealer_hand)
        
        if player_score <= 21:
            dealer_hand_string = '''\nDealer is at %s\nwith the hand %s\n'''
            print(dealer_hand_string % (dealer_score_label, dealer_hand))
        else:
            print("Dealer wins.")
            
        while self.hand_value(dealer_hand)[1] < 17:
            new_dealer_card = self.deck.pop()
            dealer_hand.append(new_dealer_card)
            print('Dealer draws %s' % new_dealer_card)

        dealer_score_label, dealer_score = self.hand_value(dealer_hand)
        
        if player_score < 100 and dealer_score == 100:
            print('You beat the dealer!')
        elif player_score > dealer_score:
            print('You beat the dealer!')
        elif player_score == dealer_score:
            print('You tied the dealer, nobody wins.')
        elif player_score < dealer_score:
            print("Dealer wins!") 

       
if __name__ == "__main__":
    play_blackjack = Blackjack()
    play_blackjack.init_game()
    
