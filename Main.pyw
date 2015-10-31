# -*- coding: utf-8 -*-
# This file is the Main. You can run this file to play.
# Please don't change the code below !

try:
    # for Python2 (Linux)
    from Tkinter import *    
except ImportError:
    # for Python3 (Windows)
    from tkinter import *     
from Grid import *
from Hanjie_Graphics import *
from Utility import *
import Editor, sys


def pointeurB1 (event):
    """Change the white box in black and reciprocally with the left click"""
    coor=[int(event.x),int(event.y)]
    if coor[0] > ig.Decalage_droite and coor[0] < ig.Decalage_droite + grid.getLargeur()*ig.Proportion:
        if coor[1] > ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut and coor[1] < ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut+ grid.getHauteur()*ig.Proportion:
            x = int((coor[0]-ig.Decalage_droite)/ig.Proportion)
            y = int((coor[1]-(ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut))/ig.Proportion)
    
            if grid.getValeur(x, y) == 0 or grid.getValeur(x, y) == 2:
                grid.setValeur(x, y, 1)
                Swap(x, y, 1, ig)
            else:
                grid.setValeur(x, y, 0)
                Swap(x, y, 0, ig)
                            
            if testEnd(Secret_grid, grid) == True:
                End(ig, Secret_grid,fenetre)
                
def pointeurB3 (event):
    """Add or remove the cross with the right click"""
    coor=[int(event.x),int(event.y)]
    if coor[0] > ig.Decalage_droite and coor[0] < ig.Decalage_droite + grid.getLargeur()*ig.Proportion:
        if coor[1] > ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut and coor[1] < ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut+ grid.getHauteur()*ig.Proportion:
            x = int((coor[0]-ig.Decalage_droite)/ig.Proportion)
            y = int((coor[1]-(ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut))/ig.Proportion)
    
            if grid.getValeur(x, y) == 0 or grid.getValeur(x, y) == 1:
                grid.setValeur(x, y, 2)
                Swap(x, y, 2, ig)
            else:
                grid.setValeur(x, y, 0)
                Swap(x, y, 0, ig)
                
def effacer():
    """Delete all boxs"""
    grid.Reset()
    Draw(grid, ig)

def retour():
    """Back to the menu"""
    for widget in fenetre.winfo_children():
        widget.destroy()
    im = menu(fenetre)    
    im.Bouton_jouer.config(command=jouer)
    im.Bouton_editeur.config(command=editeur)    

def jouer():
    """Prints all levels"""
    for widget in fenetre.winfo_children():
        widget.destroy()
    il = Lvl(fenetre)
    global my_listbox
    my_listbox = il.Listbox_niveau
    il.Bouton_lancer.config(command=lancer_niveau)
    il.Bouton_retour.config(command=retour)
   

def editeur():
    """Open the editor to create your own painting"""
    Editor.editor()

def lancer_niveau():
    """Launch a level"""
    global ig
    global grid
    global Secret_grid
   
    Nom = my_listbox.get(my_listbox.curselection())   
    
    for widget in fenetre.winfo_children():
        widget.destroy()   
           
    Secret_grid = Grid()
    Secret_grid.Load(Nom)
    grid = Grid(Secret_grid.getLargeur(),Secret_grid.getHauteur())
    
    ig = Game(Secret_grid, fenetre)
    ig.Zone_dessin.bind("<Button-1>",pointeurB1)
    ig.Zone_dessin.bind("<Button-3>",pointeurB3)
    ig.Bouton_Effacer.config(command=effacer)
    ig.Bouton_Retour.config(command=retour)
    
    
global my_listbox 
global ig
global grid
global Secret_grid
global fenetre

#Fenetre
fenetre=Tk()
fenetre.geometry("700x800")
fenetre.title("Hanjie")
fenetre.resizable(width=False, height=False)

if sys.platform == 'win32' or sys.platform=='win64':
    fenetre.iconbitmap('./res/icon/' + os.sep + 'icon.ico')
elif sys.platform == 'linux2':
    fenetre.iconbitmap('@' + './res/icon/' + os.sep + 'icon.xbm')



im = menu(fenetre)
im.Bouton_jouer.config(command=jouer)
im.Bouton_editeur.config(command=editeur)

fenetre.mainloop()