from src import EscapeRouteOptimizer


# ------------------------------------------------------------------
# Test 1:
# Verify the README example produces the expected minimum-cost
# escape route and reconstructed path.
# ------------------------------------------------------------------
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


# ------------------------------------------------------------------
# Test 2:
# Ensure the algorithm does not return the direct exit if no
# teleportation node has been activated, even when the direct path
# has a lower travel cost.
# ------------------------------------------------------------------
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

    assert optimizer.escape(start=0, exits=[5]) == (10, [0, 1, 2, 4, 5])


# ------------------------------------------------------------------
# Test 3:
# Verify that the algorithm returns None when no valid escape route
# exists because every teleportation node is unreachable.
# ------------------------------------------------------------------
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


# ------------------------------------------------------------------
# Test 4:
# Verify that teleporting directly to the exit produces the correct
# minimum-cost route.
# ------------------------------------------------------------------
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


# ------------------------------------------------------------------
# Test 5:
# Verify that when multiple teleportation nodes are available,
# the algorithm selects the globally optimal escape route rather
# than the first teleportation node encountered.
# ------------------------------------------------------------------
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
        (2, 10, 5),  # More expensive overall
        (4, 2, 8),   # Optimal teleportation node
    ]

    optimizer = EscapeRouteOptimizer(roads, teleportation_nodes)

    assert optimizer.escape(start=0, exits=[7]) == (5, [0, 3, 4, 8, 7])


# ------------------------------------------------------------------
# Test 6:
# Verify that the optimizer can be reused for multiple escape
# queries without retaining state from previous computations.
# ------------------------------------------------------------------
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