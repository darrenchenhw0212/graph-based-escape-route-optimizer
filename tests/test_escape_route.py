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