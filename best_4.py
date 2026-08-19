import heapq

def best_first_search(graph, heuristic, start, goal):
    pq = [(heuristic[start], start)]
    visited = set()

    while pq:
        _, node = heapq.heappop(pq)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    return False


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Heuristic values (smaller = closer to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}

best_first_search(graph, heuristic, 'A', 'G')