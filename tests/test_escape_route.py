from src import EscapeRouteOptimizer


def test_readme_example_escape_route():
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
        (2, 2, 4),
    ]

    optimizer = EscapeRouteOptimizer(roads, teleportation_nodes)

    assert optimizer.escape(start=0, exits=[5]) == (10, [0, 1, 2, 4, 5])


def test_direct_exit_invalid_without_teleportation():
    roads = [
        (0, 5, 1),
        (0, 1, 4),
        (1, 2, 2),
        (2, 4, 2),
        (4, 5, 2),
    ]

    teleportation_nodes = [
        (2, 2, 4),
    ]

    optimizer = EscapeRouteOptimizer(roads, teleportation_nodes)

    # 0 -> 5 is faster, but invalid because no teleportation node is activated.
    assert optimizer.escape(start=0, exits=[5]) == (10, [0, 1, 2, 4, 5])


def test_no_valid_escape_route_when_teleportation_unreachable():
    roads = [
        (0, 1, 3),
        (1, 2, 3),
        (3, 4, 2),
    ]

    teleportation_nodes = [
        (4, 2, 4),
    ]

    optimizer = EscapeRouteOptimizer(roads, teleportation_nodes)

    assert optimizer.escape(start=0, exits=[2]) is None

def test_teleport_directly_to_exit():
    roads = [
        (0, 1, 2),
        (1, 2, 2),
    ]

    teleportation_nodes = [
        (2, 1, 5),
    ]

    roads.extend([
        (5, 5, 0),
    ])

    optimizer = EscapeRouteOptimizer(roads, teleportation_nodes)

    assert optimizer.escape(0, [5]) == (5, [0, 1, 2, 5])    

def test_multiple_teleportation_nodes_choose_optimal_route():
    roads = [
        (0, 1, 2),
        (1, 2, 2),
        (0, 3, 1),
        (3, 4, 1),
        (5, 6, 1),
        (6, 7, 1),
        (8, 7, 1),
    ]

    teleportation_nodes = [
        (2, 10, 5),  # total: 2 + 2 + 10 + 1 + 1 = 16
        (4, 2, 8),   # total: 1 + 1 + 2 + 1 = 5
    ]

    optimizer = EscapeRouteOptimizer(roads, teleportation_nodes)

    assert optimizer.escape(start=0, exits=[7]) == (5, [0, 3, 4, 8, 7])


def test_escape_can_be_called_multiple_times():
    roads = [
        (0, 1, 4),
        (0, 5, 12),
        (1, 2, 2),
        (2, 3, 2),
        (3, 5, 2),
        (2, 4, 2),
        (4, 5, 2),
    ]

    teleportation_nodes = [
        (2, 2, 4),
        (3, 1, 3),
    ]

    optimizer = EscapeRouteOptimizer(roads, teleportation_nodes)

    assert optimizer.escape(start=0, exits=[5]) == (10, [0, 1, 2, 4, 5])
    assert optimizer.escape(start=1, exits=[5]) == (6, [1, 2, 4, 5])