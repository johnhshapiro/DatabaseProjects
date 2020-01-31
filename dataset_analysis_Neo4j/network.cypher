CALL apoc.load.json('file:///network.json') YIELD value AS pair
MERGE (a:Disease {code: pair.a.id, name: pair.a.name})
MERGE (b:Disease {code: pair.b.id, name: pair.b.name})
MERGE (a)-[:shares {weight: pair.weight}]->(b)

CALL algo.louvain.stream('Disease', 'shares')
YIELD nodeId, community
RETURN algo.asNode(nodeId).code AS code, community
ORDER BY community;