#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:03:12 2018

@author: jgoldstein

read in decklist and make Deck objects
"""

class Deck:
    def __init__(self, read_deckfile=None, min_main=60, max_side=15):
        self.maindeck = {}
        self.sideboard = {}
        self.min_main = min_main
        self.max_side = max_side
        
        if read_deckfile is not None:
            self.read_from_file(read_deckfile)
        pass
    
    def read_from_file(self, filename):
        """
        Read in decklist from the given filename
        
        Parameters
        ----------
        filename: path to decklist file
        """
        with open(filename, 'r') as f:
            sideboard = False
            for line in f:
                if line == '\n' or 'sideboard' in line.lower():
                    sideboard = True
                    continue
                
                # read number of copies and cardname
                vals = line.split(maxsplit=1)
                try:
                    num = int(vals[0])
                except:
                    if vals[0][-1] == 'x':
                        try:
                            num = int(vals[0][:-1])
                        except:
                            raise
                    else:
                        raise IOError('Could not read number of cards in line: {}'.format(line))
                cardname = vals[1].strip()
                
                if sideboard:
                    if cardname in self.sideboard:
                        self.sideboard[cardname] += num
                    else:
                        self.sideboard[cardname] = num
                else:
                    if cardname in self.maindeck:
                        self.maindeck[cardname] += num
                    else:
                        self.maindeck[cardname] = num
                        
    def set_decklist(self, maindeck, sideboard):
        """
        Set decklist directly with dictionaries
        
        Paramters
        ---------
        maindeck: dict
            dictionary with maindeck cards
        sideboard: dict
            dictionary with sideboard cards
        """
        num_main = sum(maindeck.values())
        num_side = sum(sideboard.values())
        if num_main < self.min_main:
            raise ValueError('Maindeck of {} cards does not make minimum of {}'.format(num_main, self.min_main))
        if num_side > self.max_side:
            raise ValueError('Sideboard of {} cards exceeds maximum of {}'.format(num_side, self.max_side))
        self.maindeck = maindeck
        self.sideboard = sideboard
