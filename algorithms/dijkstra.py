import heapq
def dijkstra(graph, start):
    distances = {
        node: float("inf") for node in graph
    }
    previous = {
        node: None for node in graph
    }
    if start not in graph:
        raise ValueError(f"Location {start} not found")
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(
            priority_queue
        )
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )
    return distances, previous
def get_path(previous, start, destination):
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    if not path or path[0] != start:
        return []
    return path
