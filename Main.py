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
from AI import *


def pointerB1 (event):
    """Change the white box in black and reciprocally with the left click"""

    global Origin
    global Sens
    global Mark

    coor=(int(event.x),int(event.y))
    if coor[0] > ig.Decalage_droite and coor[0] < ig.Decalage_droite + grid.getLargeur()*ig.Proportion:
        if coor[1] > ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut and coor[1] < ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut+ grid.getHauteur()*ig.Proportion:
            x = int((coor[0]-ig.Decalage_droite)/ig.Proportion)
            y = int((coor[1]-(ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut))/ig.Proportion)
    
            if grid.getValeur(x, y) == 0 or grid.getValeur(x, y) == 2:
                grid.setValeur(x, y, 1)
                Swap(x, y, 1, ig)
            else:
                grid.setValeur(x, y, 0)
                Draw(grid, ig)
                            
            if testEnd(Secret_grid, grid) == True:
                End(ig, Secret_grid,fenetre)
                ig.Zone_dessin.unbind("<Button-1>")
                ig.Zone_dessin.unbind("<Button-3>")
                ig.Zone_dessin.unbind("<B1-Motion>")
                ig.Zone_dessin.unbind("<B3-Motion>")

            Origin = (x,y,grid.getValeur(x,y))    
            Sens = ""
            Mark = [(x, y)]
                
def pointerB3 (event):
    """Add or remove the cross with the right click"""

    global Origin
    global Sens
    global Mark

    coor=(int(event.x),int(event.y))
    if coor[0] > ig.Decalage_droite and coor[0] < ig.Decalage_droite + grid.getLargeur()*ig.Proportion:
        if coor[1] > ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut and coor[1] < ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut+ grid.getHauteur()*ig.Proportion:
            x = int((coor[0]-ig.Decalage_droite)/ig.Proportion)
            y = int((coor[1]-(ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut))/ig.Proportion)
    
            if grid.getValeur(x, y) == 0 :
                grid.setValeur(x, y, 2)
                Swap(x, y, 2, ig)

            elif grid.getValeur(x, y) == 1:
                grid.setValeur(x, y, 2)
                Draw(grid, ig)

            else:
                grid.setValeur(x, y, 0)
                Draw(grid, ig)
            print(grid.getValeur(x,y))
            Origin = (x,y,grid.getValeur(x,y))    
            Sens = ""
            Mark = [(x, y)]

            

def slideB1(event):
    """Change the white box in black and reciprocally with the left click being held down"""

    global Origin
    global Sens
    global Mark
    
    coor=[int(event.x),int(event.y)]
    if coor[0] > ig.Decalage_droite and coor[0] < ig.Decalage_droite + grid.getLargeur()*ig.Proportion:
        if coor[1] > ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut and coor[1] < ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut+ grid.getHauteur()*ig.Proportion:
            x = int((coor[0]-ig.Decalage_droite)/ig.Proportion)
            y = int((coor[1]-(ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut))/ig.Proportion)

            if Sens == "" and x != Origin[0]:
                Sens = "h"
            elif Sens == "" and y != Origin[1]:
                Sens = "v"


            if not (x, Origin[1]) in Mark:

                if Sens == "h" and Origin[2] == 0:
                    grid.setValeur(x, Origin[1], 0)
                    Draw(grid, ig)
                    Mark = Mark + [(x, Origin[1])]
                    
                elif Sens == "h" and Origin[2] == 1:
                    grid.setValeur(x, Origin[1], 1)
                    Swap(x, Origin[1], 1, ig)
                    Mark = Mark + [(x, Origin[1])]
                    if testEnd(Secret_grid, grid) == True:
                        End(ig, Secret_grid,fenetre)
                        ig.Zone_dessin.unbind("<Button-1>")
                        ig.Zone_dessin.unbind("<Button-3>")
                        ig.Zone_dessin.unbind("<B1-Motion>")
                        ig.Zone_dessin.unbind("<B3-Motion>")

            if not (Origin[0], y) in Mark:

                if Sens == "v" and Origin[2] == 0:
                    grid.setValeur(Origin[0], y, 0)
                    Draw(grid, ig)
                    Mark = Mark + [(Origin[0], y)]

                elif Sens == "v" and Origin[2] == 1:
                    grid.setValeur(Origin[0], y, 1)
                    Swap(Origin[0], y, 1, ig)
                    Mark = Mark + [(Origin[0], y)]
                    if testEnd(Secret_grid, grid) == True:
                        End(ig, Secret_grid,fenetre)
                        ig.Zone_dessin.unbind("<Button-1>")
                        ig.Zone_dessin.unbind("<Button-3>")
                        ig.Zone_dessin.unbind("<B1-Motion>")
                        ig.Zone_dessin.unbind("<B3-Motion>")

    
def slideB3(event):
    """Add or remove the cross with the right click being held down"""

    global Origin
    global Sens
    global Mark
    
    coor=[int(event.x),int(event.y)]
    if coor[0] > ig.Decalage_droite and coor[0] < ig.Decalage_droite + grid.getLargeur()*ig.Proportion:
        if coor[1] > ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut and coor[1] < ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut+ grid.getHauteur()*ig.Proportion:
            x = int((coor[0]-ig.Decalage_droite)/ig.Proportion)
            y = int((coor[1]-(ig.NbMaxIndiceH*ig.Proportion+ig.Decalage_haut))/ig.Proportion)

            if Sens == "" and x != Origin[0]:
                Sens = "h"
            elif Sens == "" and y != Origin[1]:
                Sens = "v"

            
            if not (x, Origin[1]) in Mark:

                if Sens == "h" and Origin[2] == 2:
                                  
                    grid.setValeur(x, Origin[1], 2)
                    Draw(grid, ig)
                    Mark = Mark + [(x, Origin[1])]
                    
                elif Sens == "h" and Origin[2] != 2:
                                  
                    grid.setValeur(x, Origin[1], 0)
                    Draw(grid, ig)
                    Mark = Mark + [(x, Origin[1])]
                        

            if not (Origin[0], y) in Mark:

                if Sens == "v" and Origin[2] == 2:
                    grid.setValeur(Origin[0], y, 2)
                    Draw(grid, ig)
                    Mark = Mark + [(Origin[0], y)]
                    
                elif Sens == "v" and Origin[2] != 2:
                                  
                    grid.setValeur(Origin[0], y, 0)
                    Draw(grid, ig)
                    Mark = Mark + [(x, Origin[1])]


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

    global my_listbox

    for widget in fenetre.winfo_children():
        widget.destroy()
    il = Lvl(fenetre)
    
    my_listbox = il.Listbox_niveau
    il.Bouton_lancer.config(command=lancer_niveau)
    il.Bouton_retour.config(command=retour)
    il.Bouton_AI.config(command=ia)

def editeur():
    """Open the editor to create your own painting"""

    Editor.editor()

def ia():
    """It's the computer who plays"""

    global ig
    global grid
    global Secret_grid

    Nom = my_listbox.get(my_listbox.curselection())

    for widget in fenetre.winfo_children():
        widget.destroy()

    Secret_grid = Grid()
    Secret_grid.Load(Nom)
    grid = SolveAI(Secret_grid)
    ig = Game(Secret_grid, fenetre)

    ig.Bouton_Retour.config(command=retour)

    Draw(grid,ig)

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
    ig.Zone_dessin.bind("<Button-1>",pointerB1)
    ig.Zone_dessin.bind("<Button-3>",pointerB3)
    ig.Zone_dessin.bind("<B1-Motion>",slideB1)
    ig.Zone_dessin.bind("<B3-Motion>",slideB3)
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