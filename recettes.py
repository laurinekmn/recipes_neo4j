"""
PROJET NEO4J - RECETTES DE CUISINE
Pour le 10 novembre 2022

    * Connexion à Neo4j 
    * Création du graphe 
    * Création d'un subset
    * Requêtes dans la base de données en graphe

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

#%% --------------- VALEURS MANQUANTES ? -----------------

# df.isnull().sum().sum()
# df.isna().sum().sum()

#%% ---------------NODES AND RELATIONSHIPS-----------------

def create_graph(df):
    # Nettoyage du graphe
    graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
    
    ingredients = {}
    recipe = {}
    Contain = Relationship.type("CONTAINS")
    
    # ====================================
    # Création des noeuds et des relations 
    # ====================================
    
    for index, row in df.iterrows():
        recipe[row['label']] = Node("Recipe", name=str(row['label'])) # création noeud
        r = recipe[row['label']]
        L = [i for i in list(row.index) if row[i] == 1]
        for ingredient in L:
            if ingredient not in ingredients :
                ingredients[ingredient]= Node("Ingredient", name = str(ingredient)) # création noeud
            i = ingredients[ingredient]
            if row[ingredient]==1: 
                graph.create(Contain(r, i)) # création relation
    

#%% ---------------- Requêtes -------------------

# ==============
# Listes de base
# ==============
 
# >>>> Récupérer la liste des recettes de la base de données

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

# Exemple
print("===============================================")
print ("Liste des recettes présentes dans le graphe (5 premiers éléments affichés)")
print(list_recipes()[0:5])


# >>>> Récupérer la liste des ingrédients de la base de données
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

# Exemple
print("===============================================")
print ("Liste des ingrédients présents dans le graphe (5 premiers éléments affichés)")
print(list_ingredients()[0:5])


# ===================================
# Requêtes utilisées dans l'interface
# ===================================

# >>>> Récupérer la liste des ingrédients d'une recette choisie 

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

# Exemple
print("===============================================")
print ("Liste des ingrédients de la recette 'Ranch Dipper'")
print(get_ingredients("Ranch Dipper"))


# >>>> Récupérer la liste des recettes contenant un ingrédient choisi

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

# Exemple
print("===============================================")
print ("Liste des recettes contenant l'ingrédient 'sour cream'")
print(get_recipes_one("sour cream"))


# >>>> Récupérer la liste des recettes ne contenant pas un ingrédient choisi

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

# Exemple
print("===============================================")
print ("Liste des recettes contenant ne contenant pas l'ingrédient 'sour cream'")
print(get_recipes_without_one("sour cream"))

# ================
# Requêtes en plus
# ================

# >>>> Récupérer liste des recettes contenant une liste d'ingrédients donnés
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
print(get_recipes(["olive oil", "red wine vinegar"])) 


# >>>> Récupérer liste des recettes ne contenant pas une liste d'ingrédients donnés
def get_recipes_without_many(L_ing):
    """
    Renvoie la liste de toutes les recettes ne contenant pas les ingrédients de L_ing donnés en entrée 
    
    Input : 
        * L_ing : liste (ingrédients)
    
    Output : 
        * L : liste (noms de recettes)
    """
    L = list()
    if len(L_ing) == 0 : 
        return(print("La liste doit contenir au moins un ingrédient"))
    if len(L_ing)==1 : 
        rq = "MATCH (r:Recipe)-[:CONTAINS]->(i:Ingredient) WHERE NOT (r)-[:CONTAINS]-> (:Ingredient {name:" + f"\'{L_ing[0]}\'" + "}) RETURN DISTINCT r.name"
    else : 
        rq = "MATCH (r:Recipe)-[:CONTAINS]->(i:Ingredient) WHERE NOT (r)-[:CONTAINS]-> (:Ingredient {name:" + f"\'{L_ing[0]}\'" + "})"
        for k in range(1,len(L_ing)):
            rq = rq + "AND NOT (r)-[:CONTAINS]-> (:Ingredient {name:" + f"\'{L_ing[k]}\'" + "})"
        rq = rq + "RETURN DISTINCT r.name"

    data = graph.run(rq).data()
    for elem in data:
        L.append(elem['r.name'])
    return (L)

# Exemple
print("===============================================")
print ("Recettes contenant ne contenant pas les ingrédients 'sour cream' et 'soy sauce' (Affichage des 5 premières recettes)")
print(get_recipes_without_many(["sour cream", "soy sauce"])[0:5]) 

# >>>> Fonction renvoyant le résultat d'une requête Cypher entrée par l'utilisateur

def print_my_query(rq):
    """
    Renvoie le résultat d'une requête Cypher entrée par l'utilisateur
    
    Input : 
        * rq : chaîne de caractère, requête Cypher portant sur le jeu de données 
    
    Output : 
        * /
        print des résultats 
    """
    data = graph.run(rq).data()
    for elem in data:
        print(elem.values())
    
print("===============================================")
print ("Exemple d'utilisation de la fonction print_my_query")
print_my_query("match (r:Recipe) where (r)-[:CONTAINS]->(:Ingredient {name:'sour cream'}) return distinct r.name ")
