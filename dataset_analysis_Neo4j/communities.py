"""
3810 - Principles of Database Systems
Fall 2019
DB Assignment 04
Author: John Shapiro

This Python script takes nodes exported in json format from Neo4j and builds
a cypher that can be run in Neo4j in order to group communities of similar
diseases into a graph.
"""

import json
fin = open('nodes.json', 'rt', encoding = 'utf-8-sig')
data = json.load(fin)
fin.close()
communities = {}
for d in data:
    if d['community'] not in communities:
        communities[d['community']] = 1
    else:
        communities[d['community']] += 1
# print(communities)

fout = open('labelling.cypher', 'wt')
for d in data:
    nodeId = d['code']
    community = d['community']
    fout.write("MATCH( node { code: '" + str(nodeId) + "'} ) ")
    if communities[community] >= 10:
        fout.write("SET node:c" + str(community) + "\n")
    else:
        fout.write("DETACH DELETE node\n")
    fout.write("WITH 1 as dummy\n")
fout.write("MATCH(n) RETURN(n)")
fout.close()
