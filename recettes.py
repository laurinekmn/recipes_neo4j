"""
PROJET NEO4J - RECETTES DE CUISINE
Pour le 10 novembre 2022

Laurine Komendanczyk
"""

from py2neo import Graph, Node, Relationship
import pandas as pd
import os
import numpy as np

# Connection au graphe Neo4J
global graph
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))

# Setting working directory
os.chdir("D:/Documents/3A/bigdata/Recipes/recipes_neo4j/")

# Import dataset
df = pd.read_csv("./Data/recipes_data.csv", delimiter=",")

#%% --------------- SUBSET FOR TESTS -----------------

SUBSET_SIZE = 200

df2 = df.copy()[0:SUBSET_SIZE]

df2['label'] = df2['label'].str.replace("'", "")
# colnames = list(df2.columns)
# colnames = colnames[1: ]
# df2.dtypes

# for col in colnames : 
#     # print(type(col))
#     df2.iloc[: ,1: ] = df2.iloc[: ,1: ].astype('int32')
#     # df2.iloc[:,1:].astype('int32', copy = False)

# df2.dtypes

#%% --------------- ARE THERE MISSING VALUES -----------------

df.isnull().sum().sum()
df.isna().sum().sum()


#%% ---------------NODES AND RELATIONSHIPS-----------------

def create_graph():
    # Graph Cleaning before start
    graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
    
    ingredients = {}
    recipe = {}
    Contain = Relationship.type("CONTAINS")
    
    # =========================================
    # Creation of the nodes and relatioships
    # =========================================
    
    for index, row in df2.iterrows():
        recipe[row['label']] = Node("Recipe", name=str(row['label']))
        r = recipe[row['label']]
        L = [i for i in list(row.index) if row[i] == 1]
        for ingredient in L:
            if ingredient not in ingredients :
                ingredients[ingredient]= Node("Ingredient", name = str(ingredient))
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
# Interface
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
        * chaîne de caractères (noms d'ingrédients séparés par des virgules)
    """    
    
    L = str()    
    rq = f"match (r:Recipe)-[:CONTAINS]->(i:Ingredient) WHERE r.name IN [\'{my_r}\'] RETURN  i"
    data = graph.run(rq).data()
    for elem in data:
        L = L + "\n" + str(elem['i']['name'])
    return L[1:]


def get_recipes_one(my_ing):
    """
    Renvoie la liste de toutes les recettes contenant l'ingrédient my_ing donné en entrée 
    
    Input : 
        * my_ing : liste (ingrédients)
    
    Output : 
        * chaîne de caractères (noms de recettes séparés par des virgules)

    """
    L = str()
    
    rq = f"MATCH (r:Recipe)-[:CONTAINS]->(i:Ingredient) WHERE i.name IN [\'{my_ing}\'] RETURN DISTINCT r"
    data = graph.run(rq).data()
    for elem in data:
        L = L + "\n" + str(elem['r']['name'])
    return L

def get_recipes_without_one(my_ing):
    """
    Renvoie la liste de toutes les recettes ne contenant pas l'ingrédient my_ing donné en entrée 
    
    Input : 
        * my_ing : liste (ingrédients)
    
    Output : 
        * chaîne de caractères (noms de recettes séparés par des virgules)

    """
    L = str()
    rq = "MATCH (r:Recipe) WHERE NOT (r)-[:CONTAINS]->(:Ingredient {name:"+f"\'{my_ing}\'" + "}) RETURN DISTINCT r.name"
    data = graph.run(rq).data()
    for elem in data:
        L = L + "\n" + str(elem['r.name'])
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


# Fonction renvoyant le résultat d'une requête Cypher entrée par l'utilisateur
def solve_my_query(rq):
    """
    Renvoie le résultat d'une requête Cypher entrée par l'utilisateur
    
    Input : 
        * rq : chaîne de caractère, requête Cypher portant sur le jeu de données 
    
    Output : 
        * liste des résultats de la requête rq
    """
    data = graph.run(rq).data()
    L = str()
    for elem in data:
        L = L + "\n" + str(elem.values())
    return L    
    


