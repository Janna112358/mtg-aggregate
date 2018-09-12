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
    main: dict
        dictionary of aggregate maindeck
    side: dict
        dictionary of aggregate sideboard
    """
    count_all_cards_main = _count_aggregate_cards(decks, main=True, symbol=symbol)
    count_all_cards_side = _count_aggregate_cards(decks, main=False, symbol=symbol)
    max_occurence = len(decks)
    agg_main = _make_deck_from_count(count_all_cards_main, max_occurence, num_main)
    agg_side = _make_deck_from_count(count_all_cards_side, max_occurence, num_side)

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

def _count_aggregate_cards(decks, main=True, symbol='#'):
    """
    Count aggregate occurence of cards in a list of decks
    
    Helper function for create_aggregate. Can also be used to get a ranking of
     the most played cards in the given list of decks
    
    Parameters
    ---------
    decks: list
        list of Deck objects
    main: bool
        default = True
        if True, count maindeck aggregate
        if False, count sideboard aggregate
    symbol: str
        default = '#'
        symbol to use in numbering of aggregate cards (i.e. the difference between
        'Negate #1' and 'Negate #2'). Use something that does not occur in card names!
        
    Returns
    -------
    dict:
        counts of all aggregate cards (i.e. making the distinction between 
        'Negate #1' and 'Negate #2')
    """
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

def _make_deck_from_count(count_cards, max_occurence, len_decklist):
    """
    Get the normal-named decklist from the aggregate count
    
    Helper function for create_aggregate. Used the ranking from the aggregate count
    to select the best len_decklist number of cards (picking at random where neseccary).
    
    Parameters
    ----------
    count_cards: dict
        aggregate card count as returned by _count_aggregate_cards
    max_occurence: int
        maximum occurence of any card to assume, should be the number of decks
        used to make the aggregate count
    len_decklist: int
        lenght of the required list (usually 60 for maindeck, 15 for sideboard)
        
    Returns
    -------
    list
        list of len_decklist selected aggregate cards (i.e. making the 
        distinction between 'Negate #1' and 'Negate #2')
    """
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