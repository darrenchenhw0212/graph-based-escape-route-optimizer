from src import TreeMap

roads = [
    (0, 1, 4),
    (1, 2, 3),
    (2, 3, 5),
    (0, 3, 15),
]

solulus = [
    (1, 2, 2),
]

tree_map = TreeMap(roads, solulus)
result = tree_map.escape(start=0, exits=[3])

print(result)