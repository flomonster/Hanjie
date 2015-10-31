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
from Hanjie_Graphics import *
from copy import *
from time import *

# FILO
class Pile:
    '''Just a classic pile. First In Last Out !'''

    def __init__(self):
        '''Constructor...'''
        self.table = []

    def getLength(self):
        '''Return the length of the pile.'''
        return len(self.table)

    def add(self, var):
        '''Add an object to the pile.'''
        self.table += [var]

    def drop(self):
        '''Return the last object add.'''
        var = self.table[self.getLength()-1]        
        del self.table[self.getLength()-1]        
        return var


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

def Merge(column1, column2):
    '''Return the merge of both column'''
    column = [0] * len(column1)

    for i in range(len(column1)):
        
        if (column1[i] == 1 and column2[i] != 0) or (column2[i] == 1 and column1[i] != 0):
            break

        elif  column1[i] == 2 or column2[i] == 2:
            column[i] = 2

        elif column1[i] == 1 or column2[i] == 1:
            column[i] = 1

    else:
        return column

    return None

def Possibilities(grid, indice):
    '''Yield all available possibilities grid. Change only one column.'''
    width = grid.getLargeur()
    height = grid.getHauteur()

    # -------------------------------
    # Reperer la position d'un litige
    # -------------------------------

    best_i = 0      
    less_indice = float('inf')

    for i in range(width):        
        for j in range(height):
            if grid.getValeur(i,j) == 0:                        
                if len(indice[i]) < less_indice:
                      less_indice = len(indice[i]) 
                      best_i = i         
                break

    i = best_i
    
                
    # -------------------------------
    # Propose toutes les possibilites
    # -------------------------------

    # Sauvegarde la colonne d'origine
    memoire_possibilities = []
    
    # Lance un test des possibilites pour chaque indice separement
    positions_probables_par_indice = []
    start = 0

    end = height 
    for ind in indice[i]:
        end -= ind + 1
    for num_ind, ind in enumerate(indice[i]):        
        end += 1 + ind    
        positions_probables = []

        # Lance le test
        for k in range(start, end - ind + 1):
            can_put = True  
            col_Test = [0] * height

            for j in range(k, ind + k):
                if grid.getValeur(i,j) == 2:
                    can_put = False                
                    
            if can_put == True:
                for j in range(height):
                    if j >= k and j < k + ind:
                        col_Test[j] = 1
                    if j == k - 1 or j == k + ind:
                        col_Test[j] = 2
                positions_probables += [col_Test]

            elif len(positions_probables) == 0:
                start += 1

        positions_probables_par_indice += [positions_probables]        
        start += 1 + ind

    # Fusionne les possibilites et renvoi seulement les probables
    p = Pile()
    p.add((-1, [0]*height))

    col_origin = []
    for j in range(height):
        col_origin += [grid.getValeur(i,j)] 
          
    while p.getLength() != 0:
        var = p.drop()
        
        if var[0]+1 < len(indice[i]):
            
            for col in positions_probables_par_indice[var[0]+1]:

                merge_col = Merge(col, var[1])                
                if merge_col != None:
                    for j in range(height):
                        if col_origin[j] != 0 and merge_col[j] != 0 and col_origin[j] != merge_col[j]:
                            break
                    else:
                        p.add((var[0]+1, merge_col))
                

        else:
            
            if not var[1] in memoire_possibilities:
                copy_grid = deepcopy(grid)
                for j in range(height):
                    if var[1][j] == 0:
                        copy_grid.setValeur(i,j,2)
                    else:
                        copy_grid.setValeur(i,j,var[1][j])

                
                yield copy_grid
                memoire_possibilities += [var[1]]

                      
 
def SolveAI(Solution):
    '''Main function of the AI, call it to solve a puzzle.'''
    #Start chrono
    time_start = time()

    width = Solution.getLargeur()
    height = Solution.getHauteur()
    indice = Solution.getIndice()    

    grid = Grid(width, height)
    p = Pile()
    p.add(grid)
    Stop = False

    while Stop == False and p.getLength() > 0:
        grid = p.drop()
        
        grid = Treatment(grid, indice)
       
        if grid != None:
            if testEnd(grid, Solution) == False:
                if Analysis(grid, indice) == True:  
                
                    for possibility in Possibilities(grid, indice):  

                        if Analysis(possibility, indice) == True:                  
                            p.add(possibility)       
                                       
            else:
                Stop = True

    #End chrono
    print(time()-time_start)
    return grid
    

# TEST (Don't pay attention to the code below, you can find some errors)
if __name__ == '__main__':
    
    grid = Grid()
    grid.Load('Forty_Two')

    #Fenetre
    fenetre=Tk()
    fenetre.geometry("700x800")
    fenetre.title("AI Test")
    fenetre.resizable(width=False, height=False)
    
    ig = Game(grid, fenetre)   
    Draw(SolveAI(grid), ig)
        
    fenetre.mainloop()
    