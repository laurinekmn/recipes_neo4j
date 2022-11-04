# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:04:15 2022

@author: lauri
"""

from tkinter import *
from tkinter import ttk
from onglets import create_VIZ, create_ING, create_REC
from recettes.py import list_ingredients, list_recipes, get_ingredients
#%%

COLOR_BG = "#c1bebe"
COLOR_ACCENT1 = "#3d915f"
COLOR_ACCENT2 = "#855f53"
COLOR_ACCENT3 = "#608e85"

#%%

def create_VIZ():
    
    win = Toplevel(window)
    win.geometry("780x600")
    win.config(background = COLOR_BG)
    
    Spacetop = Label(win, text = "", height = 3, bg = COLOR_BG)

    Main_title = Label(win, text = "Visualization of the dataset", 
                       font = ("Arial", 28, "bold"), 
                       bg = COLOR_BG, 
                       fg = COLOR_ACCENT1)
    Spacetop.pack()
    Main_title.pack() 


def create_ING():
    win = Toplevel(window)
    win.geometry("780x600")
    win.config(background = COLOR_BG)

    Spacetop = Label(win, text = "", height = 3, bg = COLOR_BG)
    Space0 = Label(win, text = "", height = 3, bg = COLOR_BG)

    Main_title = Label(win, text = "List of ingredients", 
                       font = ("Arial", 28, "bold"), 
                       bg = COLOR_BG, 
                       fg = COLOR_ACCENT2)
    
    
    # ===========================
    # Menu déroulant des recettes     
    # ===========================

    OptionList = list_recipes()

    variable = StringVar(win)
    variable.set(OptionList[0])


    opt = OptionMenu(win, variable, *OptionList)
    opt.config(width=90, font=('Helvetica', 12))
    
    L_ing = get_ingredients(variable.get())
    
    ListIng = Label(win, text = L_ing)
    
    Spacetop.pack()
    Main_title.pack()  
    Space0.pack()
    opt.pack()
    ListIng.pack()
    
def create_REC():
    win = Toplevel(window)
    win.geometry("780x600")
    win.config(background = COLOR_BG)

    Spacetop = Label(win, text = "", height = 3, bg = COLOR_BG)
    
    Main_title = Label(win, text = "Selection of ingredients", 
                       font = ("Arial", 28, "bold"), 
                       bg = COLOR_BG, 
                       fg = COLOR_ACCENT3)
    Spacetop.pack()
    Main_title.pack() 


#%% ----------- FENETRE D'ACCUEIL ---------------

global window
window = Tk()
window.title("Neo4j project - Recipes finder")
window.geometry("780x600")
window.config(background = COLOR_BG)
frame = Frame (window, bg = COLOR_BG)

Sub_title = Label(frame, text = "FIND A RECIPE WITH", 
                  font = ("Arial", 12), 
                  bg = COLOR_BG, 
                  fg = COLOR_ACCENT2)

Main_title = Label(frame, text = "Recipe Finder", 
                   font = ("Arial", 28, "bold"), 
                   bg = COLOR_BG, 
                   fg = "black")


Intro = Label(frame, text = "Welcome on Recipe Finder! To start, click on one of the three buttons below.",
              font = ("Arial", 12), 
              bg = COLOR_BG,
              fg = "black")

Spacetop = Label(frame, text = "", height = 3, bg = COLOR_BG)
Space0 = Label(frame, text = "", height = 2, bg = COLOR_BG)
Space1 = Label(frame, text = "", height = 3, bg = COLOR_BG)
Space2 = Label(frame, text = "", height = 2, bg = COLOR_BG)
Space3 = Label(frame, text = "", height = 2, bg = COLOR_BG)

# Bouton redirigeant vers fenêtre de visualisation des données 
Bouton0 = Button(frame, text = "Visualize the structure of the dataset", 
                 font = ("Arial", 15), 
                 bg = COLOR_ACCENT1, 
                 fg = "white", 
                 command = create_VIZ
                 )

# Bouton redirigeant vers fenêtre pour connaître les ingrédients d'une recette
Bouton1 = Button(frame, text = "Get a list of ingredients for a chosen recipe", 
                 font = ("Arial", 15), 
                 bg = COLOR_ACCENT2, 
                 fg = "white", 
                 command = create_ING
                 )

# Bouton redirigeant ver fenêtre pour trouver des recettes avec des conditions sur les ingrédients
Bouton2 = Button(frame, text = "Find a recipe by selecting ingredients", 
                 font = ("Arial", 15), 
                 bg = COLOR_ACCENT3, 
                 fg = "white", 
                 command = create_REC
                 )



# ====
# Menu 
# ====
menup = Menu(window)

menu1 = Menu(window, tearoff = 0)
# menu1.add_command(label="Nouveau Fichier", command = <fonction>)
# menu1.add_separator()
menu1.add_command(label = "Quit", command = window.destroy)
menup.add_cascade(label = "File", menu = menu1)

# menu2 = Menu(window, tearoff = 0)
# menu2.add_command(label = "Nouveau Fichier", command = <fonction>)
# menup.add_cascade(label = "Edition", menu = menu2)





# ==================
# BUILD THE VIEWPORT
# ==================

Spacetop.pack()
Sub_title.pack()
Main_title.pack()
frame.pack() 
Space0.pack()
# Name.pack()
Intro.pack()
Space1.pack()
Bouton0.pack()
Space2.pack()
Bouton1.pack()
Space3.pack()
Bouton2.pack()

window.config(menu=menup)
window.mainloop()






# Lancer un fichier par un autre 
# os.system(nomdefichier.py)