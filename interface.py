# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:04:15 2022

@author: lauri
"""

from tkinter import *


#%%

window = Tk()
window.title("Neo4j project - Recipes finder")
window.geometry("780x600")
window.config(background = "#CBAE93")
frame = Frame (window, bg = "#CBAE93", width = 200, height = 200)


Main_title = Label(frame, text = "Find your recipe", font = ("Georgia", 20), bg = "#CBAE93" , fg = "#5b3f45")
Main_title.pack()
Name = Entry(frame, font = ("Arial", 14), fg = "black")
Space = Label(frame, text = "", height = 2, bg = "#CBAE93")
Bouton1 = Button(frame, text = "Get a list of ingredients for a chosen recipe")
Bouton2 = Button(frame, text = "Find a recipe by selecting ingredients")

# menu= Menu(window)
# menu.pack()

frame.pack() 
Space.pack()
Name.pack()
Space.pack()
Bouton1.pack()
Bouton2.pack()

window.mainloop()

#%% Menu 
menup = Menu(window)

menu1 = Menu(window)
# menu1.add_command(label="Nouveau Fichier", command = <fonction>)
menu1.add_separator()
menu1.add_command(label = "Quitter", command = fenetre.quit)
menup.add_cascade(label = "Fichier", menu=menu1)

menu2 = Menu(fenetre, tearoff = 0)
# menu2.add_command(label = "Nouveau Fichier", command = <fonction>)
menup.add_cascade(label = "Edition", menu = menu2)