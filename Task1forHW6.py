import networkx as nx
import matplotlib.pyplot as plt
import sys
import time

# Визначення функції вимірювання часу виконання функції
def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Створення порожнього графа
metro_graph = nx.Graph()

# Визначення станцій метро та їх координат
metro_stations = {
    "Centrepoint": (1, 1), "Airport Terminal 3": (1, 2), "Airport Terminal 1": (1, 3), "GGICO": (1, 4),
    "Deira City Centre": (1, 5), "Al Rigga": (1, 6), "Union": (1, 7), "Bur Juman": (1, 8), "max": (1, 9),
    "World Trade Centre": (1, 10), "Burj Khalifa / Dubai Mall": (1, 11), "Business Bay": (1, 12),
    "Onpassive": (1, 13), "Equiti": (1, 14), "Mall of the Emirates": (1, 15), "Mashreq": (1, 16),
    "Dubai Internet City": (1, 17), "Al Khail": (1, 18), "Sobha Realty": (1, 19), "DMCC": (1, 20),
    "Jabal Ali": (1, 21), "Ibn Battuta": (1, 22), "Energy": (1, 23), "Danube": (1, 24), "UAE Exchange": (1, 25),
    "Etisalat": (2, 3), "Al Qusais": (2, 4), "Dubai Airport Free Zone": (2, 5), "Al Nahda": (2, 6),
    "Stadium": (2, 7), "Al Quiadah": (2, 8), "Abu Baker Al Siddique": (2, 9), "Union": (1, 7),
    "Baniyas Square": (2, 10), "Palm Deira": (2, 11), "Al Ras": (2, 12), "Al Ghubaiba": (2, 13),
    "Al Fahidi": (2, 14), "Bur Juman": (1, 8), "Oud Metha": (2, 16), "Dubai Healthcare City": (2, 17),
    "Al Jadaf": (2, 18), "Creek": (2, 19)
}

# Додавання вершин до графа
metro_graph.add_nodes_from(metro_stations)

# Визначення функції для додавання ребер із вагами
def metro_connections_with_weights(edges, weights):
    for edge, weight in zip(edges, weights):
        metro_graph.add_edge(*edge, weight=weight)

# Визначення ребер та їх ваг
edges = [
    ("Centrepoint", "Airport Terminal 3"), ("Airport Terminal 3", "Airport Terminal 1"),
    ("Airport Terminal 1", "GGICO"), ("GGICO", "Deira City Centre"), ("Deira City Centre", "Al Rigga"),
    ("Al Rigga", "Union"), ("Union", "Bur Juman"), ("Bur Juman", "max"), ("max", "World Trade Centre"),
    ("World Trade Centre", "Burj Khalifa / Dubai Mall"), ("Burj Khalifa / Dubai Mall", "Business Bay"),
    ("Business Bay", "Onpassive"), ("Onpassive", "Equiti"), ("Equiti", "Mall of the Emirates"),
    ("Mall of the Emirates", "Mashreq"), ("Mashreq", "Dubai Internet City"), ("Dubai Internet City", "Al Khail"),
    ("Al Khail", "Sobha Realty"), ("Sobha Realty", "DMCC"), ("DMCC", "Jabal Ali"), ("Jabal Ali", "Ibn Battuta"),
    ("Ibn Battuta", "Energy"), ("Energy", "Danube"), ("Danube", "UAE Exchange"),
    ("Etisalat", "Al Qusais"), ("Al Qusais", "Dubai Airport Free Zone"), ("Dubai Airport Free Zone", "Al Nahda"),
    ("Al Nahda", "Stadium"), ("Stadium", "Al Quiadah"), ("Al Quiadah", "Abu Baker Al Siddique"),
    ("Abu Baker Al Siddique", "Union"), ("Union", "Baniyas Square"), ("Baniyas Square", "Palm Deira"),
    ("Palm Deira", "Al Ras"), ("Al Ras", "Al Ghubaiba"), ("Al Ghubaiba", "Al Fahidi"), ("Al Fahidi", "Bur Juman"),
    ("Bur Juman", "Oud Metha"), ("Oud Metha", "Dubai Healthcare City"), ("Dubai Healthcare City", "Al Jadaf"),
    ("Al Jadaf", "Creek")
]

# Значення ваги взяті довільно
weights = [
    2, 3, 4, 2, 5, 3, 4, 3, 2, 4, 3, 2, 5, 4, 3, 2, 4, 3, 4, 3, 2, 3, 4, 3, 2, 3, 2, 3, 4, 3, 4, 3, 2, 3, 2, 3, 4,
    3, 4, 3, 2, 3, 2, 3, 4, 3, 4, 3
]

# Додавання ребер з вагами до графа
metro_connections_with_weights(edges, weights)

# Створення графіка
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(metro_graph)
nx.draw(
    metro_graph, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10,
    font_weight='bold', edge_color='gray', width=1
)
plt.title('Станції метро Dubai')
plt.show()

# Аналіз графа
print("Кількість вершин:", metro_graph.number_of_nodes())
print("Кількість ребер:", metro_graph.number_of_edges())
print("Ступінь вершин:", dict(metro_graph.degree()))

# Визначення функції DFS
def dfs(graph, start, end, path=[], visited=set()):
    visited.add(start)
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in visited:
            new_paths = dfs(graph, node, end, path, visited)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Визначення функції BFS
def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next_node in set(graph.adj[node]) - set(path):
            if next_node == end:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

# Виконання алгоритмів DFS та BFS для пошуку шляхів у графі
start_station = "Centrepoint"
end_station = "Creek"

# Вимірюємо час виконання DFS
dfs_result, dfs_time = measure_time(dfs, metro_graph, start_station, end_station)

# Вимірюємо час виконання BFS
bfs_result, bfs_time = measure_time(list, bfs(metro_graph, start_station, end_station))

# Вывод результатов
print("Шляхи, знайдені за допомогою DFS:")
for path in dfs_result:
    print(path)
print("Час виконання DFS:", dfs_time)

print("\nШляхи, знайдені за допомогою BFS:")
for path in bfs_result:
    print(path)
print("Час виконання BFS:", bfs_time)

# Визначення функції алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {node: sys.maxsize for node in graph.nodes()}
    distances[start] = 0
    visited = set()
    current = start
    while len(visited) < len(graph.nodes()):
        visited.add(current)
        for neighbor in graph.neighbors(current):
            weight = graph[current][neighbor]['weight']
            distance = distances[current] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        if len(visited) < len(graph.nodes()):
            candidates = {node: distances[node] for node in graph.nodes() if node not in visited}
            current = min(candidates, key=candidates.get)
    return distances

# Вибираємо початкову станцію та викликаємо алгоритм Дейкстри
start_station = "Centrepoint"
dijkstra_distances = dijkstra(metro_graph, start_station)
print("Найкоротші відстані до кожної станції від початкової станції:")
print(dijkstra_distances)
