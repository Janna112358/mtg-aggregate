#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:03:12 2018

@author: jgoldstein

read in decklist and make Deck objects
"""
import os
from collections import defaultdict

class Deck:
    def __init__(self, from_dicts=None, min_main=60, max_side=15):
        self._maindeck = {}
        self._sideboard = {}
        self.min_main = min_main
        self.max_side = max_side
        
        if from_dicts is not None:
            self.set_decklist(*from_dicts)
    
    @classmethod
    def from_file(cls, filename):
        """
        Read in decklist from the given filename
        
        Parameters
        ----------
        filename: str
            path to the decklist file
        """
        # create dictionaries that set the value of any key to 0 by default
        maindeck = defaultdict(int)
        sideboard = defaultdict(int)
        
        with open(filename, 'r') as f:
            
            # start by reading maindeck, flip to sideboard
            # if we encounter a newline or the word sideboard
            read_sideboard = False
            for line in f:
                if line == '\n' or 'sideboard' in line.lower():
                    read_sideboard = True
                    continue
            
                # read number of copies and cardname
                vals = line.split(maxsplit=1)
                try:
                    if vals[0][-1] == 'x':
                        num = int(vals[0][:-1])
                    else:
                        num = int(vals[0])
                except ValueError:
                    raise IOError('Could not read number of cards in line: {!r}'.format(line))
                cardname = vals[1].strip()
            
                if read_sideboard:
                    sideboard[cardname] += num
                else:
                    maindeck[cardname] += num
                    
            return Deck(from_dicts=(maindeck, sideboard))
                        
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
        self._maindeck = maindeck
        self._sideboard = sideboard
        
    def print_decklist(self):
        """
        Print decklist to screen
        """
        print('Mainboard')
        for card in self._maindeck:
            print('{} {}'.format(self._maindeck[card], card))
        print('\nSidebaord')
        for card in self._sideboard:
            print('{} {}'.format(self._sideboard[card], card))
            
    def save_decklist(self, savefile):
        """
        Save decklist to a file
        
        Parameters
        ----------
        savefile: str
            Path to the file to save in
        """
        with open(savefile, 'w') as f:
            for card in self._maindeck:
                f.write('{} {}\n'.format(self._maindeck[card], card))
            f.write('\n')
            for card in self._sideboard:
                f.write('{} {}\n'.format(self._sideboard[card], card))
                
                
    @classmethod                
    def read_folder(cls, folder, ext='.dck'):
        """
        Read in all decklists from a folder
        
        Parameters
        ----------
        folder: str
            Path to the directory with decklist files
            
        ext: str
        default = '.dck'
        Extension of decklist files
        
        Returns
        -------
        list
            list with Decks read from folder
        """
        file_list = os.listdir(folder)
        os.chdir(folder)
        return [cls.from_file(f) for f in file_list if f.endswith(ext)]
                