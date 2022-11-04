# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:04:15 2022

@author: lauri
"""

from tkinter import *
from tkinter import ttk

#%%

COLOR_BG = "#c1bebe"
COLOR_ACCENT1 = "#3d915f"
COLOR_ACCENT2 = "#855f53"
COLOR_ACCENT3 = "#608e85"



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


# Name = Entry(frame, font = ("Arial", 14), fg = "black")

Intro = Label(frame, text = "Welcome on Recipe Finder! To start, click on one of the three buttons below.",
              font = ("Arial", 12), 
              bg = COLOR_BG,
              fg = "black")

Spacetop = Label(frame, text = "", height = 3, bg = COLOR_BG)
Space0 = Label(frame, text = "", height = 2, bg = COLOR_BG)
Space1 = Label(frame, text = "", height = 3, bg = COLOR_BG)
Space2 = Label(frame, text = "", height = 2, bg = COLOR_BG)
Space3 = Label(frame, text = "", height = 2, bg = COLOR_BG)

Bouton0 = Button(frame, text = "Visualize the structure of the dataset", 
                 font = ("Arial", 15), 
                 bg = COLOR_ACCENT1, 
                 fg = "white"
                 )

Bouton1 = Button(frame, text = "Get a list of ingredients for a chosen recipe", 
                 font = ("Arial", 15), 
                 bg = COLOR_ACCENT2, 
                 fg = "white" 
                 )

Bouton2 = Button(frame, text = "Find a recipe by selecting ingredients", 
                 font = ("Arial", 15), 
                 bg = COLOR_ACCENT3, 
                 fg = "white"
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
