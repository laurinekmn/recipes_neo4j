"""
PROJET NEO4J - RECETTES DE CUISINE
Pour le 10 novembre 2022

Laurine Komendanczyk
"""

from py2neo import *
import pandas as pd
from pandas import DataFrame
import os



graph = Graph("bolt://localhost:7687",auth=("neo4j", "123"))



# Recipes dataset import

os.chdir("D:/Documents/3A/bigdata/Recettes_Neo4J/")

df = pd.read_csv("./Data/recipes_data.csv", delimiter=",")



#%%
df2 = df.copy()[1:6]
colnames = list(df2.columns)
colnames = colnames[1:]
df2.dtypes

for col in colnames : 
    # print(type(col))
    df2.iloc[:,1:] = df2.iloc[:,1:].astype('int32')
    # df2.iloc[:,1:].astype('int32', copy = False)

df2.dtypes



#%%

# Check for missing values

df.isnull().sum().sum()
df.isna().sum().sum()


#%%

# Graph Cleaning

graph.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")

# Creation of nodes for each recipe

recipe = {}
for index, row in df.iterrows(): #index est un entier, rows est pd.Series
    # print(index, type(index))
    # print(row, type(row))
    recipe[row['label']] = Node("Recipe",
                                name=str(row['label']))


# Creation of nodes for each ingredient 

ingredients = {}
for name, col in df.iteritems():
    ingredients[name] = Node("Ingredient", 
                             name = str(name))


# Relationship 
 
Contain = Relationship.type("CONTAINS")

for index, row in df.iterrows():
    r = recipe[row['label']]
    # print(r)
    for ingredient in list(row.index) :
        i = ingredients[ingredient]
        if row[ingredient]==1 : 
            graph.create(Contain(r, i))


#%%

for r in recipe : 
    graph.create(r)
