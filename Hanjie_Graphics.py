# -*- coding: utf-8 -*-
# This file is the Graphics. Right here the widgets are created and more.
# Please don't change the code below !


try:
    # for Python2 (Linux)
    from Tkinter import *    
except ImportError:
    # for Python3 (Windows)
    from tkinter import *    
from Grid import *
from math import *
from Utility import * 
from random import *
from sys import *

# Useless
dic = {}

class Info_lvl:
    '''Class for levels selection window'''

    def __init__(self,bouton_lancer,bouton_retour,bouton_ai,listbox_niveau):
        '''The constructor'''
        self.Bouton_lancer = bouton_lancer
        self.Bouton_retour = bouton_retour
        self.Bouton_AI = bouton_ai
        self.Listbox_niveau = listbox_niveau
        
 
class Info_menu:
    '''Class for the menu'''    

    def __init__(self,bouton_jouer,bouton_editeur):
        '''The constructor'''
        self.Bouton_jouer = bouton_jouer
        self.Bouton_editeur = bouton_editeur
        
        
class Info_game:
    '''Class for the Game window'''
    
    def __init__(self,proportion,decalage_droite,decalage_haut,zone_dessin,nbmaxindiceh,nbmaxindicel,bouton_effacer,bouton_retour,indices,down_canvas):
        '''The constructor'''
        self.Proportion = proportion
        self.Decalage_droite = decalage_droite
        self.Decalage_haut = decalage_haut
        self.Zone_dessin = zone_dessin
        self.NbMaxIndiceH = nbmaxindiceh
        self.NbMaxIndiceL = nbmaxindicel
        self.Bouton_Effacer = bouton_effacer
        self.Bouton_Retour = bouton_retour
        self.Indices = indices
        self.Down_Canvas = down_canvas 

    
def Game(grid, fenetre) :
    """Print the game window"""

    #Zone de dessin
    zone_dessin = Canvas(fenetre, width=700, height=620, bg=None)
    zone_dessin.place(x=0,y=0)

    img = searchBackgrounds()
    img = choice(img)

    dic["Bg"] = img
    
    #Zone de dessin du bas
    Down_canvas = Canvas(fenetre, width=700, height=200, bg='navajo white' )
    Down_canvas.place(x=0,y=610)

    img = PhotoImage(file = "./res/Background/Down_Background.png")
    dic["down_canvas"] = img
    Down_canvas.create_image(0, 0, anchor = NW, image = img )
    
    #Bouttons
    img = PhotoImage(file='./res/Buttons/Button_clear.png')
    dic["button_clear"] = img 
    bouton_effacer=Button(fenetre, image = img, width=172, height=38, bg='navajo white')
    bouton_effacer.place(x=250,y=660)
    
    img = PhotoImage(file='./res/Buttons/Button_back.png')
    dic["button_back"] = img
    bouton_retour=Button(fenetre, image = img, width=140, height=38, bg='navajo white')
    bouton_retour.place(x=267,y=710)
      
    #Grid
    Indices = grid.getIndice()
    Hauteur = grid.getHauteur()
    Largeur = grid.getLargeur()

    NbMaxIndiceH = 0
    NbMaxIndiceL = 0
    
    #Definir Nb max d'indices pour la hauteur et la largeur
    for i in range(Largeur):
        if len(Indices[i]) > NbMaxIndiceH:
            NbMaxIndiceH = len(Indices[i])
            
    for i in range(Largeur,len(Indices)):
        if len(Indices[i]) > NbMaxIndiceL:
            NbMaxIndiceL = len(Indices[i])

        
    #Dessin de la grille
    Proportion = 0
    if float(Hauteur + NbMaxIndiceH)/620 > float(Largeur + NbMaxIndiceL)/700:
        x = Hauteur + NbMaxIndiceH
        Proportion = int(-0.8138*x + 41.613)
           
    else:
        x = Largeur + NbMaxIndiceL
        Proportion = int(-1.1434*x + 54.476)     
            
    Decalage_droite = (700 - (Largeur + NbMaxIndiceL)*Proportion)/2
    Decalage_haut = (620 - (Hauteur + NbMaxIndiceH)*Proportion)/2
              
       
    Ig = Info_game(Proportion, Decalage_droite, Decalage_haut, zone_dessin, NbMaxIndiceH, NbMaxIndiceL, bouton_effacer, bouton_retour, grid.getIndice(), Down_canvas)

    
    Draw(Grid(Largeur, Hauteur), Ig)

    return Ig

def menu(fenetre):
    """Print the menu window"""
    #Fond
    img = PhotoImage(file = "./res/Background/bg_menu.png")
    dic["fond"] = img
    Fond = Canvas(fenetre, width=701, height=801)
    Fond.create_image(0, 0, anchor = NW, image=img)
    Fond.pack()

    #Bouttons
    img = PhotoImage(file='./res/Buttons/Button_play.png')
    dic["button_play"] = img
    bouton_jouer=Button(fenetre, image = img, width=124, height=38, bg='navajo white')
    bouton_jouer.place(x=276,y=390)
    
    img = PhotoImage(file='./res/Buttons/Button_editor.png')
    dic["button_editor"] = img
    bouton_editeur=Button(fenetre, image = img, width=154, height=38, bg='navajo white')
    bouton_editeur.place(x=260,y=440)
      
    
    Im = Info_menu(bouton_jouer, bouton_editeur)
    return Im
    

def Lvl(fenetre):
    '''Print the level window'''
    
    #Background
    img = PhotoImage(file = "./res/Background/bg_level.png")
    dic["fond"] = img
    Fond = Canvas(fenetre, width=700, height=800)
    Fond.create_image(0,0,anchor = NW, image=img)
    Fond.place(x=0,y=0)
        
    #Listbox
    
    listbox_niveau = Listbox(fenetre)
    Niveau = searchSaves()
    for i in range(len(Niveau)):
        listbox_niveau.insert(i, Niveau[i].Name)
                
    listbox_niveau.place(x=276,y=70)
            
    #Butons 
    img = PhotoImage(file = "./res/Buttons/Button_start.png")
    dic["bouton_lancer"] = img   
    bouton_lancer=Button(fenetre, image = img, width=314, height=38, bg='navajo white')     
    bouton_lancer.place(x=180,y=390)

    img = PhotoImage(file = "./res/Buttons/Button_back.png")
    dic["bouton_retour"] = img
    bouton_retour=Button(fenetre, image = img, width=140, height=38, bg='navajo white')  
    bouton_retour.place(x=267,y=440)

    img = PhotoImage(file = "./res/Buttons/Button_AI.png")
    dic["bouton_ai"] = img
    bouton_ai=Button(fenetre, image = img, width=60, height=38, bg='navajo white') 
    bouton_ai.place(x=305,y=490)
    
    Il = Info_lvl(bouton_lancer, bouton_retour, bouton_ai, listbox_niveau)
    return Il


def Swap(x,y,color,Ig,reduc = 3):
    '''Swap the color of the box (x, y) to white(0), black(1) or cross(other) color.'''
        
    x = x*Ig.Proportion + Ig.Decalage_droite 
    y = y*Ig.Proportion + Ig.Decalage_haut + Ig.NbMaxIndiceH*Ig.Proportion
    if color == 1:
        Ig.Zone_dessin.create_rectangle(x + reduc, y + reduc, x + Ig.Proportion - reduc, y + Ig.Proportion - reduc, fill='black')
    elif color == 2:        
        Ig.Zone_dessin.create_line(x + reduc, y+reduc, x + Ig.Proportion - reduc, y + Ig.Proportion - reduc, fill='black',width=1.5)
        Ig.Zone_dessin.create_line(x + reduc, y + Ig.Proportion - reduc, x + Ig.Proportion - reduc, y + reduc, fill='black',width=1.5)
            

def Draw(grid, IG, boolean_grid = True, reduc = 3):
    '''Print the color of boxs thank the grid'''

    IG.Zone_dessin.create_image(0, 0, anchor = NW, image = dic["Bg"] )


    #Grid
    Indices = IG.Indices
    Hauteur = grid.getHauteur()
    Largeur = grid.getLargeur()

    if boolean_grid == True :
        #traits Horizontaux        
        for i in range(IG.NbMaxIndiceH*IG.Proportion, Hauteur*IG.Proportion + IG.NbMaxIndiceH*IG.Proportion + 1 , IG.Proportion):
            if ((i/IG.Proportion)-IG.NbMaxIndiceH)%5 == 0 :      
                IG.Zone_dessin.create_line(0 + IG.Decalage_droite, i + IG.Decalage_haut, Largeur*IG.Proportion + IG.Decalage_droite, i + IG.Decalage_haut, fill = "black",width=2)
            else:
                 IG.Zone_dessin.create_line(0 + IG.Decalage_droite, i + IG.Decalage_haut, Largeur*IG.Proportion + IG.Decalage_droite, i + IG.Decalage_haut, fill = "black",width=1)
        #traits Verticaux
        for i in range(0 ,Largeur*IG.Proportion +1 , IG.Proportion):        
            if (i/IG.Proportion)%5 == 0 :            
                IG.Zone_dessin.create_line(i + IG.Decalage_droite, IG.NbMaxIndiceH*IG.Proportion + IG.Decalage_haut, i + IG.Decalage_droite, IG.Proportion*(Hauteur + IG.NbMaxIndiceH) + IG.Decalage_haut, fill = "black",width=2)
        
            else :
                IG.Zone_dessin.create_line(i + IG.Decalage_droite, IG.NbMaxIndiceH*IG.Proportion + IG.Decalage_haut, i + IG.Decalage_droite, IG.Proportion*(Hauteur + IG.NbMaxIndiceH) + IG.Decalage_haut, fill = "black")
        #Indices en Haut
        for i in range(0,Largeur):
            for j in range(len(Indices[i])-1,-1,-1):
                IG.Zone_dessin.create_text(IG.Decalage_droite + IG.Proportion*(i + 0.5), IG.Decalage_haut + IG.Proportion*(IG.NbMaxIndiceH - (len(Indices[i])- j - 1) - 0.5) - 1, text=Indices[i][j], fill = 'red')                       
        
        #Indices a Droite
        for i in range(Largeur,len(Indices)):
            for j in range(len(Indices[i])):
                IG.Zone_dessin.create_text(IG.Decalage_droite + IG.Proportion*(Largeur + j + 0.5) + 3, IG.Decalage_haut + IG.Proportion*( i - Largeur + IG.NbMaxIndiceH + 0.5), text=Indices[i][j], fill = 'red')
        
    #Dessine les cases en fonction de la grille       
    for i in range(grid.getLargeur()):
        for j in range(grid.getHauteur()):
            Swap(i,j,grid.getValeur(i,j),IG,reduc)
           

def End(Ig, grid, fenetre):
    """Print the end of the game"""
    Ig.Bouton_Effacer.destroy()
    img = PhotoImage(file='./res/Bravo.png')
    dic["bravo"] = img
    Ig.Down_Canvas.create_image(270, 50, anchor = NW, image = img)
    
    
    Ig.Decalage_droite = (700 - grid.getLargeur()*Ig.Proportion)/2
    Ig.Decalage_haut = (620 - grid.getHauteur()*Ig.Proportion)/2 - Ig.NbMaxIndiceH*Ig.Proportion
    
    Draw(grid, Ig, False, 0)
                
    
# TEST (Don't pay attention to the code below, you can find some errors)
if __name__ == "__main__":
    ma_grid = Grid()
    ma_grid.Load("Ying Yang")
    fenetre=Tk()
    fenetre.geometry("700x800")
    fenetre.title("Hanjie")
    Ig = Game(ma_grid, fenetre)
    End(Ig, ma_grid, fenetre)
    fenetre.mainloop()