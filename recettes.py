"""
PROJET NEO4J - RECETTES DE CUISINE
Pour le 10 novembre 2022

Laurine Komendanczyk
"""

from py2neo import Graph, Node, Relationship
import pandas as pd
# from pandas import DataFrame
import os

# Connection au graphe Neo4J
graph = Graph("bolt://localhost:7687", 
              auth=("neo4j", "123"))

# Setting working directory
os.chdir("D:/Documents/3A/bigdata/Recipes/recipes_neo4j/")

# Import dataset
df = pd.read_csv("./Data/recipes_data.csv", delimiter=",")

#%% --------------- SUBSET FOR TESTS -----------------

df2 = df.copy()[1:6]
colnames = list(df2.columns)
colnames = colnames[1: ]
df2.dtypes

for col in colnames : 
    # print(type(col))
    df2.iloc[: ,1: ] = df2.iloc[: ,1: ].astype('int32')
    # df2.iloc[:,1:].astype('int32', copy = False)

df2.dtypes

#%% --------------- ARE THERE MISSING VALUES -----------------

df.isnull().sum().sum()
df.isna().sum().sum()


#%% ---------------NODES AND RELATIONSHIPS-----------------

# Graph Cleaning before starting 
graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")


# =================================
# Creation of nodes for each recipe
# =================================

recipe = {}

for index, row in df.iterrows(): #index est un entier, rows est pd.Series
    # print(index, type(index))
    # print(row, type(row))
    recipe[row['label']] = Node("Recipe",
                                name = str(row['label'])
                                )


# =====================================
# Creation of nodes for each ingredient 
# =====================================

ingredients = {}

for name, col in df.iteritems():
    ingredients[name] = Node("Ingredient", 
                             name = str(name))

# ============
# Relationship 
# ============
 
Contain = Relationship.type("CONTAINS")

for index, row in df.iterrows():
    r = recipe[row['label']]
    
    for ingredient in list(row.index):
        i = ingredients[ingredient]
        if row[ingredient] == 1: 
            graph.create(Contain(r, i))


#%% ---------------- Optimisation ---------------

# Graph Cleaning before start
graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")


# =========
# Creation of nodes for each ingredient 
# =========

ingredients = {}

for name, col in df.iteritems():
    ingredients[name] = Node("Ingredient", 
                             name = str(name))

# =========================================
# Creation of relationship with each recipe
# =========================================

Contain = Relationship.type("CONTAINS")

recipe = {}

for index, row in df.iterrows():
    recipe[row['label']] = Node("Recipe",
                                name=str(row['label']))
    r = recipe[row['label']]
    L = [i for i in list(row.index) if row[i] == 1]
    
    for ingredient in L:
        i = ingredients[ingredient]
        if row[ingredient]==1: 
            graph.create(Contain(r, i))


#%% ---------------- Requêtes -------------------

# ==============
# Listes de base
# ==============
 
def list_recipes ():
    """
    Renvoie la liste de tous les noms de recettes de la base de données
    
    Input : /
    
    Output : 
        * liste
    """
    
    L = []    
    rq = "match (r:Recipe)-[:CONTAINS]->(i:Ingredient) RETURN DISTINCT r"
    data = graph.run(rq).data()
    for elem in data:
        L.append(elem['r']['name'])
    return (L)


def list_ingredients ():
    """
    Renvoie la liste de tous les noms d'ingrédients de la base de données
    
    Input : /
    
    Output : 
        * liste
    """    
    
    L = []
    rq = "match (r:Recipe)-[:CONTAINS]->(i:Ingredient) RETURN DISTINCT i"
    data = graph.run(rq).data()
    for elem in data:
        L.append(elem['i']['name'])
    return (L)

# =============
# Visualisation
# =============

rq = "MATCH (r:Recipe)-[:CONTAINS]->(i:Ingredient) RETURN list(r, count(DISTINCT i)"



# Récupérer liste des ingrédients d'une recette choisie 

my_r = "Hazelnut Chicken"


def get_ingredients (my_r):
    """
    Renvoie la liste de tous les noms d'ingrédients de la recette donnée en entrée 
    
    Input : 
        * my_r : chaîne de caractères (nom de recette)
    
    Output : 
        * liste (noms d'ingrédients)
    """    
    
    L = list()    
    rq = f"match (r:Recipe)-[:CONTAINS]->(i:Ingredient) WHERE r.name IN [\'{my_r}\'] RETURN  i"
    data = graph.run(rq).data()
    for elem in data:
        L.append(elem['i']['name'])
    return L



# Récupérer liste des recettes contenant un ingrédient donné
def get_recipes():
    """
    Renvoie la liste de toutes les recettes contenant au moins les ingrédients de my_i_yes et ne contenant pas ceux de my_i_no donnés en entrée 
    
    Input : 
        * my_i_yes : liste (ingrédients)
        * my_i_no : liste (ingrédients)
    
    Output : liste (noms de recettes)
    """
    L = list()
    my_i_yes = list()
    my_i_no = list()
    
    rq = f"match (r:Recipe)-[:CONTAINS]->(i:Ingredient) WHERE i.name IN {my_i_yes} AND WHERE i.name NOT IN {my_i_no} RETURN r"
    data = graph.run(rq).data()
    for elem in data:
        L.append(elem['r']['name'])
    return L


