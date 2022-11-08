"""
PROJET NEO4J - RECETTES DE CUISINE
Pour le 10 novembre 2022

Laurine Komendanczyk
"""

from py2neo import Graph, Node, Relationship
import pandas as pd
import os

# Connection au graphe Neo4J
global graph
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))

# Setting working directory
os.chdir("D:/Documents/3A/bigdata/Recipes/recipes_neo4j/")

# Import dataset
df = pd.read_csv("./Data/recipes_data.csv", delimiter=",")

#%% --------------- SUBSET FOR TESTS -----------------

SUBSET_SIZE = 200

def create_subset(SUBSET_SIZE):
    df2 = df.copy()[0:SUBSET_SIZE]
    return df2

create_subset(SUBSET_SIZE)

#%% --------------- ARE THERE MISSING VALUES -----------------

df.isnull().sum().sum()
df.isna().sum().sum()


#%% ---------------NODES AND RELATIONSHIPS-----------------

def create_graph(df):
    # Graph Cleaning before start
    graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
    
    ingredients = {}
    recipe = {}
    Contain = Relationship.type("CONTAINS")
    
    # =========================================
    # Creation of the nodes and relatioships
    # =========================================
    
    for index, row in df.iterrows():
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

# ===================================
# Requêtes utilisées dans l'interface
# ===================================

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

# ================
# Requêtes en plus
# ================

# >>>> Récupérer liste des recettes contenant un ingrédient donné
def get_recipes(L_ing):
    """
    Renvoie la liste de toutes les recettes contenant les ingrédients de L_ing donnés en entrée 
    
    Input : 
        * L_ing : liste (ingrédients)
    
    Output : 
        * L : liste (noms de recettes)
    """
    L = list()
    if len(L_ing) == 0 : 
        return(print("La liste doit contenir au moins un ingrédient"))
    if len(L_ing)==1 : 
        rq = "MATCH (r:Recipe)-[:CONTAINS]->(i:Ingredient) WHERE (r)-[:CONTAINS]-> (:Ingredient {name:" + f"\'{L_ing[0]}\'" + "}) RETURN DISTINCT r.name"
    else : 
        rq = "MATCH (r:Recipe)-[:CONTAINS]->(i:Ingredient) WHERE (r)-[:CONTAINS]-> (:Ingredient {name:" + f"\'{L_ing[0]}\'" + "})"
        for k in range(1,len(L_ing)):
            rq = rq + "AND (r)-[:CONTAINS]-> (:Ingredient {name:" + f"\'{L_ing[k]}\'" + "})"
        rq = rq + "RETURN DISTINCT r.name"

    data = graph.run(rq).data()
    for elem in data:
        L.append(elem['r.name'])
    return (L)

# Exemple
print("===============================================")
print ("Recettes contenant les ingrédients 'olive oil' et 'red wine vinegar'")
get_recipes(["olive oil", "red wine vinegar"]) # Beet Salad

# >>>> Fonction renvoyant le résultat d'une requête Cypher entrée par l'utilisateur
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
    


