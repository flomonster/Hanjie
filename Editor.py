# -*- coding: utf-8 -*-
# This file is the editor. You can run this file to create a new puzzle.
# Please don't change the code below !

try:
    # for Python2 (Linux)
    from Tkinter import *
    from ttk import Combobox
except ImportError:
    # for Python3 (Windows)
    from tkinter import * 
    from tkinter.ttk import Combobox
    
from Grid import *

 
def But_Save():
    """Save the actual draw"""    
    global grid 
    Name = entry_retour.get()
    
    grid.Reduce()
    dif = combobox_difficulty.get()
    dif = dif.replace('LVL ', '', 1)
    grid.Save(Name, dif)
    
    grid = Grid()
    rePaint()
    
    
def But_Load():
    """Load a draw"""
        
    Name = entry_retour.get()
    
    grid.Load(Name)
    grid.Enlarge()
    
    combobox_difficulty.set(lvlList[grid.difficulty-1])
    
    rePaint()
    
def But_Reset():
    '''Reset the draw'''
    grid.Reset()    
    rePaint()
    combobox_difficulty.set(lvlList[0])
    
def Swap(event):
    """Swap the color box"""
    x = int(event.x)
    y = int(event.y)
    
    i = int(x / 10)
    j = int(y / 10)
            
    if (grid.getValeur(i, j) == 0):
        grid.setValeur(i, j, 1)  
        zone_dessin.create_rectangle(i * 10 + 1, j* 10 + 1, i * 10 + 9, j * 10 + 9, outline='black', fill='black')     

    else:
        grid.setValeur(i, j, 0)    
        zone_dessin.create_rectangle(i * 10 + 1, j* 10 + 1, i * 10 + 9, j * 10 + 9, outline='white', fill='white')    
    
def rePaint():
    """Repaint the grid with a new table"""
    for j, Ligne in enumerate(grid.table):
        for i, var in enumerate(Ligne):
            if (var == 0):
                zone_dessin.create_rectangle(i * 10 + 1, j* 10 + 1, i * 10 + 9, j * 10 + 9, outline='white', fill='white')     
            else:
                zone_dessin.create_rectangle(i * 10 + 1, j* 10 + 1, i * 10 + 9, j * 10 + 9, outline='black', fill='black')

def Initialisation(): 
    """Draw the lines of the grid"""          
    for i in range(0, 500, 10):
        zone_dessin.create_line(i, 0, i, 500, fill = "black")
        zone_dessin.create_line(0, i, 500, i, fill = "black")
        
def editor(): 
    """Run editor"""
    global zone_dessin     
    global grid 
    global entry_retour
    global combobox_difficulty
    global lvlList
    
    grid = Grid()
    
    # Windows
    fenetre = Tk()

    fenetre.geometry("500x525")
    fenetre.title("Editeur Hanjie")
    fenetre.resizable(width=False, height=False)

    # Canvas
    zone_dessin = Canvas(fenetre,width=500,height=500, bg="white")
    zone_dessin.place(x=0,y=0) 
    Initialisation()
    zone_dessin.bind("<Button-1>", Swap)

    # Entry
    default_text = StringVar()
    entry_retour = Entry(fenetre,width=20,textvariable=default_text)
    default_text.set("Level name...")
    entry_retour.place(x=2,y=503)

    # Save Button
    button_save = Button(fenetre,text="Save", width=8,height=1, command = But_Save)
    button_save.place(x=130,y=500)

    # Load Button
    button_load = Button(fenetre,text="Load", width=8,height=1, command = But_Load)
    button_load.place(x=200,y=500)

    # Reset Button
    button_load = Button(fenetre,text="Reset", width=8,height=1, command = But_Reset)
    button_load.place(x=270,y=500)

    # Difficulty Combobox
    lvlSelect = StringVar()
    lvlList = ('LVL 1', 'LVL 2', 'LVL 3', 'LVL 4', 'LVL 5')
    combobox_difficulty = Combobox(fenetre, values = lvlList, state = 'readonly')    
    combobox_difficulty.set(lvlList[0])
    combobox_difficulty.place(x=340,y=502)

    fenetre.mainloop()

# TEST (Don't pay attention to the code below, you can find some errors)
if __name__ == "__main__":
    editor()
