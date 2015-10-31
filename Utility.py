# -*- coding: utf-8 -*-
# This file is the Utility. Utility contain some useful functions.
# Please don't change the code below !

try:
    # for Python2 (Linux)
    from Tkinter import *    
except ImportError:
    # for Python3 (Windows)
    from tkinter import *    
import os
from Grid import *

def searchSaves():
    """Return the list of saves"""
 
    folder = 'Save/'
    Str = '.txt'
    
    # Recherche le contenu du dosssier 
    entry = os.listdir(folder)
    
    list_grid = []
 
    # Traitement des fichiers du repertoire
    for f in entry:
        if (not os.path.isdir(os.path.join(folder, f))) and (f.find(Str) != -1):
            g = Grid()
            g.Load(f.replace(Str, ''))
            list_grid += [g]
    
    list_grid = sorted(list_grid, key = lambda grid: grid.difficulty)
    
    return list_grid     

def searchBackgrounds():
    """Return the list of saves"""
 
    folder = 'res/Background/Bg_Game/'
    Str = '.png'
    
    # Recherche le contenu du dosssier 
    entry = os.listdir(folder)
    
    list_bg = []
 
    # Traitement des fichiers du repertoire
    for f in entry:
        if (not os.path.isdir(os.path.join(folder, f))) and (f.find(Str) != -1):
            img = PhotoImage(file = './' + folder + f)            
            list_bg += [img]
            
    return list_bg     

def testEnd (Secret_grid, grid):
    """Return true if the game is ended and false if not"""
    
    Verif = True
    
    for i in range (len(grid.table)):
        for j in range (len(grid.table[0])):
            var = grid.table[i][j]
            var_s = Secret_grid.table[i][j]
            
            if (var == 1 and var_s != 1) or (var_s == 1 and var != 1):
                Verif = False
    
    return Verif  

# TEST (Don't pay attention to the code below, you can find some errors)
if __name__ == '__main__':
    print(searchSaves())