#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:00:35 2018

@author: jgoldstein

mtg aggreate deck creator
"""
from random import shuffle

def create_aggregate(decks, save=None, num_main=60, num_side=15, symbol='#'):
    """
    Create the aggregate deck from a list of decks
    
    Parameters
    ----------
    decks: list of Decks
    save: None or filename
    if not None, save aggregate list using the given file name
    
    Returns
    -------
    Deck: the aggregate decklist
    """
    count_all_cards_main = count_aggregate_cards(decks, main=True, symbol=symbol)
    count_all_cards_side = count_aggregate_cards(decks, main=False, symbol=symbol)
    max_occurence = len(decks)
    agg_main = make_deck_from_count(count_all_cards_main, max_occurence, num_main)
    agg_side = make_deck_from_count(count_all_cards_side, max_occurence, num_side)

    main = {}
    for agg_card in agg_main:
        card = agg_card.split(symbol)[0].strip()
        if card in main:
            main[card] += 1
        else:
            main[card] = 1                              
                            
    side = {}
    for agg_card in agg_side:
        card = agg_card.split(symbol)[0].strip()
        if card in side:
            side[card] += 1
        else:
            side[card] = 1
    
    return main, side  

def count_aggregate_cards(decks, main=True, symbol='#'):
    count_cards = {}
    for deck in decks:
        if main:
            decklist = deck._maindeck
        else:
            decklist = deck._sideboard
            
        for card in decklist:
            for i in range(decklist[card]):
                agg_card = card + ' {}{}'.format(symbol, i+1)
                if agg_card not in count_cards:
                    count_cards[agg_card] = 1
                else:
                    count_cards[agg_card] += 1
    return count_cards

def make_deck_from_count(count_cards, max_occurence, len_decklist):
    agg_deck = []
    while len(agg_deck) < len_decklist:
        space_in_deck = len_decklist - len(agg_deck)
        
        best_cards = [agg_card for agg_card in count_cards if count_cards[agg_card] == max_occurence]
        if len(best_cards) <= space_in_deck:
            agg_deck += best_cards
            max_occurence -= 1
        else:
            print('choose {} cards randomly from {}'.format(space_in_deck, best_cards))
            shuffle(best_cards)
            agg_deck += best_cards[:space_in_deck]
    
    return agg_deck