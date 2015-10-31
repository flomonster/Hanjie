# -*- coding: utf-8 -*-
# This file is the artificial intelligence (AI). The AI can solve every puzzle.
# Please don't change the code below !

try:
    # for Python2 (Linux)
    from Tkinter import *    
except ImportError:
    # for Python3 (Windows)
    from tkinter import *    
from Grid import *
from math import *
from sys import *
from Hanjie_Graphics import *
from Utility import *
from copy import *
from time import *

# FILO
class Pile:
    '''Just a classic pile. First In Last Out !'''

    def __init__(self):
        '''Constructor...'''
        self.table = []

    def getLenght(self):
        '''Return the lenght of the pile.'''
        return len(self.table)

    def add(self, var):
        '''Add an object to the pile.'''
        self.table += [var]

    def drop(self):
        '''Return the last object add.'''
        var = self.table[self.getLenght()-1]        
        del self.table[self.getLenght()-1]        
        return var

class Essay:

    def __init__(self, grid, en_cours, step):

        self.grid = grid
        self.en_cours = en_cours
        self.step = step

class Step:

    def __init__(self, x, y, grid_memory):

        self.x = x
        self.y = y     
        self.grid_memory = grid_memory   

def TreatmentCol(grid, col, indice):
    '''Analysis a column and put a maximum of black and cross boxes.'''
    h = grid.getHauteur()    
    start = 0

    end = h 
    for ind in indice[col]:
        end -= ind + 1

    col_Verif_Cross = [2] * h
    
    for num_ind, ind in enumerate(indice[col]):
        col_Verif = [1] * h
        end += 1 + ind    
        OK = False

        # Lance le test
        for i in range(start, end - ind + 1):
            can_put = True

            for j in range(i, ind + i):
                if grid.getValeur(col,j) == 2:
                    can_put = False
                                    
            if can_put == True:
                OK = True
                for j in range(h):
                    if j < i or j >= i + ind:
                        col_Verif[j] = 0  
                    else:
                        col_Verif_Cross[j] = 0
                
        # Applique les resultats du test
        start += 1 + ind
        count = 0
        if OK == True:
            for i in range(h):
                if col_Verif[i] == 1:
                    grid.setValeur(col, i, 1)
                    count += 1
                    if count == ind:                    
                        if i + 1 < h:                    
                            grid.setValeur(col, i+1, 2)
                        if i - ind >= 0:
                            grid.setValeur(col, i-ind, 2)   

                    if start < i + 2:
                        start = i + 2  
        else:
            None

    for i in range(h):
        if col_Verif_Cross[i] == 2:
            grid.setValeur(col, i, 2)  

    return grid


def TreatmentLig(grid, lig, indice):
    '''Analysis a line and put a maximum of black and cross boxes.'''
    l = grid.getLargeur()
    start = 0

    end = l
    for ind in indice[lig+l]:
        end -= ind + 1

    lig_Verif_Cross = [2] * l
    
    for num_ind, ind in enumerate(indice[lig+l]):
        lig_Verif = [1] * l
        end += 1 + ind
        OK = False

        # Test
        for i in range(start, end - ind + 1):
            can_put = True

            for j in range(i, ind + i):
                if grid.getValeur(j,lig) == 2:
                    can_put = False
            
            if can_put == True:   
                OK = True      
                for j in range(l):
                    if j < i or j >= i + ind:
                        lig_Verif[j] = 0  
                    else:
                        lig_Verif_Cross[j] = 0 
                     
        # Applique les resultats du test   
        start += 1 + ind
        count = 0
        if OK == True:
            for i in range(l):
                if lig_Verif[i] == 1:
                    grid.setValeur(i, lig, 1)
                    count += 1
                    if count == ind:
                        if i + 1 < l:                    
                            grid.setValeur(i+1, lig, 2)
                        if i - ind >= 0:
                            grid.setValeur(i-ind, lig, 2)   

                    if start < i + 2:
                        start = i + 2
        else:
            return None

    for i in range(l):
        if lig_Verif_Cross[i] == 2:
            grid.setValeur(i, lig, 2)  

    return grid


def Treatment(grid, indice):
    '''Complete the grid intelligently and return it.'''
    width = grid.getLargeur()
    height = grid.getHauteur()

    Last_Grid = copy(grid)
    loop = False

    Already_Treat = set()
    
    while (Last_Grid.table != grid.table or loop == False) and Analysis(grid, indice) == True:
        loop = True
        Last_Grid = deepcopy(grid)

        # Complete black boxes
        for i in range(len(indice)):

            if not i in Already_Treat:

                if i < width:         
                    for j in range(height):
                        if grid.getValeur(i,j) == 0:
                            grid = TreatmentCol(grid, i, indice)
                            break 
                    else:
                        Already_Treat.add(i)                              

                else:
                    for j in range(width):
                        if grid.getValeur(j, i - width) == 0:
                            grid = TreatmentLig(grid, i - width, indice)
                            break 
                    else:
                        Already_Treat.add(i)                

                if grid == None:
                    return None

        
    
        # Complete cross
        indice_potentiel = grid.getIndice()

        for i in range(len(indice)):
            if indice[i] == indice_potentiel[i]:
                if i < grid.getLargeur():
                    for j in range(grid.getHauteur()):
                        if grid.getValeur(i,j) == 0:
                            grid.setValeur(i,j,2)

                else:
                    for j in range(grid.getLargeur()):
                        if grid.getValeur(j,i-grid.getLargeur()) == 0:
                            grid.setValeur(j,i-grid.getLargeur(),2)

    return grid


def Analysis(grid, indice):
    '''Analysis all lines and columns and puts crosses everywhere it can. Return False if there are errors.'''
    width = grid.getLargeur()
    height = grid.getHauteur()
    Valid = True

    indice_potentiel = grid.getIndice()

    for i in range(len(indice)):
        
        # TEST I
        sum_indice = 0
        sum_indice_potentiel = 0

        for ind in indice[i]:
            sum_indice += ind

        for ind in indice_potentiel[i]:
            sum_indice_potentiel += ind

        if sum_indice_potentiel > sum_indice:
            Valid = False         
            break

        # TEST II
        if indice_potentiel[i] != indice[i]:
            if i < width:
                for j in range(height):
                    if grid.getValeur(i,j) == 0:
                        break
                else:
                    Valid = False                    
                    break

            else:
                for j in range(width):
                    if grid.getValeur(j,i-width) == 0:
                        break
                else:
                    Valid = False
                    break

    # TEST III
    break_ = False
    for i in range(grid.getLargeur()):
        for j in range(grid.getHauteur()):
            if grid.getValeur(i,j) == 0:  
                break_ = True              
                break            
        if break_ == True:
            break
    else:
        Valid = False
    return Valid

        
def New(essay):
    
    grid = essay.grid
    grid_memory = deepcopy(grid)

    for i in range(grid.getLargeur()):
        for j in range(grid.getHauteur()):

            if grid.getValeur(i, j) == 0:
                                
                grid.setValeur(i, j, 1)

                step = Step(i,j, grid_memory)

                new_essay = Essay(grid, False, step)

                return new_essay

    return None


def Next(essay):
    
    grid = essay.step.grid_memory
    i = essay.step.x
    j = essay.step.y
    grid.setValeur(i, j, 2)
    
    new_essay = Essay(grid, False, None)

    return New(new_essay)


def SolveAI(Solution):
    '''Main function of the AI, call it to solve a puzzle.'''
    # Start chrono
    time_start = time()

    # Solve
    indice = Solution.getIndice()

    p = Pile()
    grid = Grid(Solution.getLargeur(), Solution.getHauteur())
    grid = Treatment(grid, indice)
    essay = Essay(grid, False, None)
    p.add(essay)   

    while p.getLenght() != 0:

        essay_actual = p.drop()        

        if testEnd(essay_actual.grid, Solution) == True:            
            # End chrono
            print(time()-time_start)
            return essay_actual.grid

        elif essay_actual.en_cours == False:
            essay_actual.en_cours = True
            p.add(essay_actual)
            new_essay = New(essay_actual)
            if new_essay != None:
                p.add(new_essay)

        else:
            next_essay = Next(essay_actual)
            if next_essay != None:
                p.add(next_essay)    


# TEST (Don't pay attention to the code below, you can find some errors)
if __name__ == '__main__':
    
    grid = Grid()
    grid.Load('Boat')

    #Fenetre
    fenetre=Tk()
    fenetre.geometry("700x800")
    fenetre.title("AI Test")
    fenetre.resizable(width=False, height=False)
    
    ig = Game(grid, fenetre)   
    Draw(SolveAI(grid), ig)
        
    fenetre.mainloop()
    