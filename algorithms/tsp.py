from algorithms.dijkstra import dijkstra, get_path
def tsp(graph, start, destinations):
    if start not in graph:
        raise ValueError("Starting location not found")
    remaining = set(destinations)
    remaining.discard(start)
    route = [start]
    total_distance = 0
    current = start
    while remaining:
        distances, previous = dijkstra(graph, current)
        nearest = min(
            remaining,
            key=lambda node: distances[node]
        )
        if distances[nearest] == float("inf"):
            raise ValueError("Destination is unreachable")
        path = get_path(previous, current, nearest)
        route.extend(path[1:])
        total_distance += distances[nearest]
        current = nearest
        remaining.remove(nearest)
    if current != start:
        distances, previous = dijkstra(graph, current)
        if distances[start] == float("inf"):
            raise ValueError("Depot is unreachable")
        return_path = get_path(previous, current, start)
        route.extend(return_path[1:])
        total_distance += distances[start]
    return route, total_distance
