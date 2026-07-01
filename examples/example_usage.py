from src import EscapeRouteOptimizer


roads = [
    (0, 1, 4),
    (0, 5, 12),
    (1, 2, 2),
    (2, 3, 2),
    (3, 4, 10),
    (3, 5, 2),
    (4, 5, 2),
]

teleportation_nodes = [
    (2, 2, 4),  # node, activation_cost, teleport_destination
]

optimizer = EscapeRouteOptimizer(roads, teleportation_nodes)

time_required, path = optimizer.escape(
    start=0,
    exits=[5],
)

print("Time required:", time_required)
print("Path:", path)