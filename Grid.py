# -*- coding: utf-8 -*-
# This file is the grid's class.
# Please don't change the code below !

class Grid:  
    
    def __init__(self, width=50, height=50, difficulty = None, name = ''):
        '''Constructor'''

        tab = [[0 for i in range(width)] for j in range(height)]         
        self.table = tab
        self.difficulty = difficulty
        self.Name = name
                

    def Reset(self):
        '''This method put all boxs to 0'''

        for i, ligne in enumerate(self.table):
            for j in range(len(ligne)):            
                  
                self.table[i][j] = 0

    def setValeur(self, x,y, val):
        '''Change the value of the box (x, y) to (val)'''

        self.table[y][x] = val        

    def getValeur(self, x, y):
        '''Return the value of the box (x, y)'''

        return self.table[y][x]
    
    def getLargeur(self):
        '''Return the width of the grid'''

        return len(self.table[0])
    
    def getHauteur(self):
        '''Return the height of the grid'''

        return len(self.table)
    
    def Save(self, Name, Difficulty):
        """This method save the grid""" 
        
        self.Name = Name     
        
        f = open('Save/' + Name + ".txt" , "w")        
        f.write(str(Difficulty))
        f.write('\n')
        
        for i, ligne in enumerate(self.table):
            for num in ligne:
                f.write(str(num))
            if i != len(self.table) -1:
                f.write("\n")                    

        f.close()
    
    def Load(self, Name):
        """This method load a grid"""
        
        self.Name = Name     
        
        f = open('Save/' + Name + ".txt", "r")
        
        Dessin = []
    
        for i, line in enumerate(f):
            if i == 0:
                self.difficulty = int(line[0])
            else:
                tab = []
                for case in line:
                    if (case == "0" or case == "1"):
                        tab += [int(case)]
                Dessin += [tab]
    
        f.close()
    
        self.table = Dessin
        
    def getIndice(self):
        """Return the index list of the grid"""

        ind = []
        compteur = 0
        
        #Indices verticaux
        for i in range (len(self.table[0])):
            colone_ind = []
            
            for j in range (len(self.table)):
                var = self.table[j][i]
                if var == 1:
                    compteur = compteur+1
                elif compteur != 0 and var != 1:
                    colone_ind = colone_ind+[compteur]
                    compteur = 0
                    
            if compteur != 0:
                colone_ind = colone_ind+[compteur]
                compteur = 0
            ind = ind + [colone_ind]
        compteur = 0
         
        #Indices horizontaux   
        for i in range (len(self.table)):
            ligne_ind = []
            
            for j in range (len(self.table[0])):
                var = self.table[i][j]
                if var == 1:
                    compteur = compteur+1
                elif compteur != 0 and var != 1:
                    ligne_ind = ligne_ind+[compteur]
                    compteur = 0
                    
            if compteur != 0:
                ligne_ind = ligne_ind+[compteur]
                compteur = 0
            ind = ind + [ligne_ind]
                    
        return ind
    
    def Reduce(self):
        '''This method reduce the grid without loose the painting'''

        min_i = 50
        min_j = 50
        max_i = 0
        max_j = 0
    
        for i, ligne in enumerate(self.table):
            for j, case in enumerate(ligne):
                if case == 1:
                    if i < min_i:
                        min_i = i
                    if i > max_i:
                        max_i =i 
                    if j < min_j:
                        min_j = j
                    if j > max_j:
                        max_j = j
                    
        new_Grid = []
        
        for i in range(min_i, max_i+1):
            ligne = []
            for j in range(min_j, max_j+1):
                ligne += [self.table[i][j]]
            new_Grid += [ligne]
    
        self.table = new_Grid
        
    def Enlarge(self, size=50):
        '''Enlarge the grid'''
        
        new_tab = []
        
        if size > len(self.table[0]):
        
            manque = [0] * (size-len(self.table[0]))
            for ligne in self.table:
                new_tab += [ligne+manque]
        if size > len(self.table):
            for i in range(size - len(self.table)):
                new_tab += [[0] * size]
                
        if new_tab != []:
            self.table = new_tab

# TEST (Don't pay attention to the code below, you can find some errors)
if __name__ == '__main__':
    g = Grid()
    g.getIndice()
    g.Load('Skull')
    print(g.getIndice())
