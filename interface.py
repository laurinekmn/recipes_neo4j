# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:04:15 2022

@author: lauri
"""

from tkinter import *
from tkinter import ttk
# from onglets import create_VIZ, create_ING, create_REC
# from recettes import list_ingredients, list_recipes, get_ingredients, get_recipes

#%% --------------- COULEURS DE L'INTERFACE ------------------

COLOR_BG = "#c1bebe"
COLOR_ACCENT1 = "#3d915f"
COLOR_ACCENT2 = "#855f53"
COLOR_ACCENT3 = "#608e85"

#%% ------------ SOUS-FENÊTRES DE L'INTERFACE-----------------


def create_LIST():
    win = Toplevel(window)
    win.geometry("780x600")
    win.config(background = COLOR_BG)
    
    # Espaces entre les différents éléments 
    Spacetop = Label(win, text = "", height = 3, bg = COLOR_BG)
    Space0 = Label(win, text = "", height = 1, bg = COLOR_BG)
    Space1 = Label(win, text = "", height = 3, bg = COLOR_BG)
    Space2 = Label(win, text = "", height = 3, bg = COLOR_BG)
    Space3 = Label(win, text = "", height = 3, bg = COLOR_BG)

    # Titre de la fenêtre
    Main_title = Label(win, text = "List of ingredients", 
                       font = ("Arial", 28, "bold"), 
                       bg = COLOR_BG, 
                       fg = COLOR_ACCENT1)
    
    # Explication du fonctionnement de la fenêtre
    Explication = Label(win, text = "1) Choose a recipe from the list \n \n 2) Click the \"Update the list\" button to see the list of the ingredient!",
                        font = ("Arial", 13, "italic"), 
                        bg = COLOR_BG, 
                        fg = "black")
    
    # Menu déroulant des recettes     
    OptionList = list_recipes()

    var = StringVar(win)
    L_ing = StringVar(win)
    var.set(OptionList[0])
    L_ing.set(get_ingredients(var.get()))

    # Menu 
    opt = OptionMenu(win, var, *OptionList)
    opt.config(width=90, 
               font=('Arial', 14, "bold"), 
               bg = COLOR_BG, 
               fg = "black")
    
    # Bouton pour mettre à jour la liste des ingrédients 
    def update_L_ing ():
        v = var.get()
        L_ing.set(get_ingredients(v))
    
    update = Button(win, 
                    text = "Update the list", 
                    font = ("Arial", 16, "bold"), 
                    bg = COLOR_ACCENT3, 
                    fg = "white",
                    command = update_L_ing)
    
    
    # Liste des ingrédients de la recette sélectionnée
    ListIng = Label(win, 
                    font = ("Arial", 13), 
                    bg = COLOR_BG, 
                    fg = "black",
                    textvariable = L_ing)
    
    
    # "Construction" de la fenêtre avec pack 
    Spacetop.pack()
    Main_title.pack()  
    Space0.pack()
    Explication.pack()
    Space1.pack()
    opt.pack()
    Space2.pack()
    update.pack()
    Space3.pack()
    ListIng.pack()


def create_ONE():
    
    win = Toplevel(window)
    win.geometry("780x600")
    win.config(background = COLOR_BG)
    
    Spacetop = Label(win, text = "", height = 3, bg = COLOR_BG)
    Space0 = Label(win, text = "", height = 1, bg = COLOR_BG)
    Space1 = Label(win, text = "", height = 3, bg = COLOR_BG)
    Space2 = Label(win, text = "", height = 3, bg = COLOR_BG)
    Space3 = Label(win, text = "", height = 3, bg = COLOR_BG)

    Main_title = Label(win, text = "Recipes with one ingredient", 
                       font = ("Arial", 28, "bold"), 
                       bg = COLOR_BG, 
                       fg = COLOR_ACCENT2)
    
    # Explication du fonctionnement de la fenêtre
    Explication = Label(win, text = "1) Choose an ingredient from the list \n \n 2) Click the \"Update the list\" button to see the list of the recipes which contain it!",
                        font = ("Arial", 13, "italic"), 
                        bg = COLOR_BG, 
                        fg = "black")
    
    # Menu déroulant des ingrédients     
    OptionList = list_ingredients()

    var = StringVar(win)
    L_rec = StringVar(win)
    var.set(OptionList[0])
    L_rec.set(get_recipes_one(var.get()))

    # Menu 
    opt = OptionMenu(win, var, *OptionList)
    opt.config(width=90, 
               font=('Arial', 14, "bold"), 
               bg = COLOR_BG, 
               fg = "black")
    
    # Bouton pour mettre à jour la liste des ingrédients 
    def update_L_rec ():
        v = var.get()
        L_rec.set(get_recipes_one(v))
    
    update = Button(win, 
                    text = "Update the list", 
                    font = ("Arial", 16, "bold"), 
                    bg = COLOR_ACCENT1, 
                    fg = "white",
                    command = update_L_rec)
    
    
    # Liste des ingrédients de la recette sélectionnée
    ListRec = Label(win, 
                    font = ("Arial", 13), 
                    bg = COLOR_BG, 
                    fg = "black",
                    textvariable = L_rec)
    
    
    Spacetop.pack()
    Main_title.pack() 
    Space0.pack()
    Explication.pack()
    Space1.pack()
    opt.pack()
    Space2.pack()
    update.pack()
    Space3.pack()
    ListRec.pack()

    

def create_WITHOUT_ONE():
    
    win = Toplevel(window)
    win.geometry("780x600")
    win.config(background = COLOR_BG)
    
    Spacetop = Label(win, text = "", height = 3, bg = COLOR_BG)
    Space0 = Label(win, text = "", height = 1, bg = COLOR_BG)
    Space1 = Label(win, text = "", height = 3, bg = COLOR_BG)
    Space2 = Label(win, text = "", height = 3, bg = COLOR_BG)
    Space3 = Label(win, text = "", height = 3, bg = COLOR_BG)

    Main_title = Label(win, text = "Recipes without one ingredient", 
                       font = ("Arial", 28, "bold"), 
                       bg = COLOR_BG, 
                       fg = COLOR_ACCENT2)
    
    # Explication du fonctionnement de la fenêtre
    Explication = Label(win, text = "1) Choose an ingredient from the list \n \n 2) Click the \"Update the list\" button to see the list of the recipes which contain it!",
                        font = ("Arial", 13, "italic"), 
                        bg = COLOR_BG, 
                        fg = "black")
    
    # Menu déroulant des ingrédients     
    OptionList = list_ingredients()

    var = StringVar(win)
    L_rec = StringVar(win)
    var.set(OptionList[0])
    L_rec.set(get_recipes_without_one(var.get()))

    # Menu 
    opt = OptionMenu(win, var, *OptionList)
    opt.config(width=90, 
               font=('Arial', 14, "bold"), 
               bg = COLOR_BG, 
               fg = "black")
    
    # Bouton pour mettre à jour la liste des ingrédients 
    def update_L_rec ():
        v = var.get()
        L_rec.set(get_recipes_without_one(v))
    
    update = Button(win, 
                    text = "Update the list", 
                    font = ("Arial", 16, "bold"), 
                    bg = COLOR_ACCENT1, 
                    fg = "white",
                    command = update_L_rec)
    
    
    # Liste des ingrédients de la recette sélectionnée
    ListRec = Label(win, 
                    font = ("Arial", 13), 
                    bg = COLOR_BG, 
                    fg = "black",
                    textvariable = L_rec)
    
    
    Spacetop.pack()
    Main_title.pack() 
    Space0.pack()
    Explication.pack()
    Space1.pack()
    opt.pack()
    Space2.pack()
    update.pack()
    Space3.pack()
    ListRec.pack()


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


#%% ------------------ FENETRE D'ACCUEIL ---------------------

global window

# ================================
# ELEMENTS DE LA FENETRE D'ACCUEIL
# ================================

# Création d'une fenêtre 
window = Tk()
window.title("Neo4j project - Recipes finder")
window.geometry("780x600")
window.config(background = COLOR_BG)
frame = Frame (window, bg = COLOR_BG)

# Sous-titre - fenêtre d'accueil
Sub_title = Label(frame, text = "FIND A RECIPE WITH", 
                  font = ("Arial", 12), 
                  bg = COLOR_BG, 
                  fg = COLOR_ACCENT2)

# Titre - fenêtre d'accueil
Main_title = Label(frame, text = "Recipe Finder", 
                   font = ("Arial", 28, "bold"), 
                   bg = COLOR_BG, 
                   fg = "black")

# Explication du fonctionnement de l'interface
Intro = Label(frame, text = "Welcome on Recipe Finder! To start, click on one of the three buttons below.",
              font = ("Arial", 12), 
              bg = COLOR_BG,
              fg = "black")

# Espaces entre les éléments
Spacetop = Label(frame, text = "", height = 3, bg = COLOR_BG)
Space0 = Label(frame, text = "", height = 2, bg = COLOR_BG)
Space1 = Label(frame, text = "", height = 3, bg = COLOR_BG)
Space2 = Label(frame, text = "", height = 2, bg = COLOR_BG)
Space3 = Label(frame, text = "", height = 2, bg = COLOR_BG)
Space4 = Label(frame, text = "", height = 2, bg = COLOR_BG)


# Bouton redirigeant vers fenêtre pour connaître les ingrédients d'une recette
Bouton0 = Button(frame, text = "Get a list of ingredients for a chosen recipe", 
                 font = ("Arial", 15), 
                 bg = COLOR_ACCENT1, 
                 fg = "white", 
                 command = create_LIST
                 )

# Bouton redirigeant vers fenêtre pour obtenir recettes contenant un ingrédient choisi
Bouton1 = Button(frame, text = "Choose an ingredient you want in the recipe", 
                 font = ("Arial", 15), 
                 bg = COLOR_ACCENT2, 
                 fg = "white", 
                 command = create_ONE
                 )

# Bouton redirigeant ver fenêtre pour trouver des recettes avec des conditions sur les ingrédients
Bouton2 = Button(frame, text = "Choose an ingredient you don't want in the recipe", 
                 font = ("Arial", 15), 
                 bg = COLOR_ACCENT2, 
                 fg = "white", 
                 command = create_WITHOUT_ONE
                 )


# Bouton redirigeant ver fenêtre pour trouver des recettes avec des conditions sur les ingrédients
Bouton3 = Button(frame, text = "Find a recipe by selecting ingredients", 
                 font = ("Arial", 15), 
                 bg = COLOR_ACCENT3, 
                 fg = "white", 
                 command = create_REC
                 )



# ====
# Menu 
# ====

# Création d'un menu en haut de la fenêtre d'accueil permettant de quitter l'interface
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
Space4.pack()
Bouton3.pack()

window.config(menu=menup)



window.mainloop()



# Lancer un fichier par un autre 
# os.system(nomdefichier.py)