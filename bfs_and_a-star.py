# Md. Sabbir Ahamed
# Bfs and A* algorithms
from queue import PriorityQueue

heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vileea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

graph = {
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vileea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Rimnicu Vileea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Pitesti': {'Rimnicu Vileea': 97, 'Bucharest': 101, 'Craiova': 138},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vileea': 146, 'Pitesti': 138},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

def best_first_search(start, goal):
    my_queue = PriorityQueue()
    my_queue.put((heuristic[start], start, [start]))  # my_queue=[[366,'Arad',['Arad']]
    visited = set()

    while not my_queue.empty():
        _, current, path = my_queue.get()

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor, _ in graph[current].items(): # neighbour, _ ={'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118}
                if neighbor not in visited:
                    my_queue.put((heuristic[neighbor], neighbor, path + [neighbor])) # (374,'Zerind',['Arad','Zerind'])

    return None  

def a_star_search(start, goal):
    my_queue = PriorityQueue()
    my_queue.put((0 + heuristic[start], start, [start], 0))  # my_queue=[[0+366,'Arad',['Arad'],0]
    visited = set()

    while not my_queue.empty():
        _, current, path, edge_cost = my_queue.get() #current='Arad' path=['Arad'], edge_cost=0

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor, distance in graph[current].items(): # neighbour,distance={'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118}
                if neighbor not in visited:
                    new_cost = edge_cost + distance # 0 + 75
                    priority = new_cost + heuristic[neighbor] # 75+374
                    my_queue.put((priority, neighbor, path + [neighbor], new_cost)) # (449,'Zerind',['Arad','Zerind'],75)

    return None  

source = 'Arad'
destination = 'Bucharest'

print("Path Using BFS:")
best_first_path = best_first_search(source, destination)
print("Path:", best_first_path)

print("\nPath Using A* Search:")
a_star_path = a_star_search(source, destination)
print("Path:", a_star_path)