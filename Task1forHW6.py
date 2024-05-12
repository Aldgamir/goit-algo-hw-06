import networkx as nx
import matplotlib.pyplot as plt
import sys

# Створюємо пустий граф
metro_graph = nx.Graph()

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

metro_graph.add_nodes_from(metro_stations)

def metro_connections_with_weights(edges, weights):
    for edge, weight in zip(edges, weights):
        metro_graph.add_edge(*edge, weight=weight)

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

# Значення для метро Dubai взяті навмання
weights = [
    2, 3, 4, 2, 5, 3, 4, 3, 2, 4, 3, 2, 5, 4, 3, 2, 4, 3, 4, 3, 2, 3, 4, 3, 2, 3, 2, 3, 4, 3, 4, 3, 2, 3, 2, 3, 4,
    3, 4, 3, 2, 3, 2, 3, 4, 3, 4, 3
]

metro_connections_with_weights(edges, weights)

# Тепер ствоимо сам графік
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(metro_graph)
nx.draw(
    metro_graph, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10,
    font_weight='bold', edge_color='gray', width=1
)
plt.title('Станції метро Dubai')
plt.show()

# Проаналізуємо граф
print("Кількість вкршин:", metro_graph.number_of_nodes())
print("Кількість ребер:", metro_graph.number_of_edges())
print("Ступінь ребер:", dict(metro_graph.degree()))

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

def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next_node in set(graph.adj[node]) - set(path):
            if next_node == end:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

# Використаемо алгоритми DFS і BFS для знаходження шляхів у графі
start_station = "Centrepoint"
end_station = "Creek"

dfs_paths = dfs(metro_graph, start_station, end_station)
bfs_paths = list(bfs(metro_graph, start_station, end_station))

# Виводимо результати
print("Шляхи, знайдені за допомогою DFS:")
for path in dfs_paths:
    print(path)

print("\nШляхи, знайдені за допомогою BFS:")
for path in bfs_paths:
    print(path)

def dijkstra(graph, start):
    # Ініціалізуємо довжину шляху до всіх вершин як нескінченність
    distances = {node: sys.maxsize for node in graph.nodes()}
    distances[start] = 0

    # Створюємо множину відвіданих вершин
    visited = set()

    # Починаємо обхід з початкової вершини
    current = start

    while len(visited) < len(graph.nodes()):
        visited.add(current)

        # Оновлюємо відстані до сусідніх вершин
        for neighbor in graph.neighbors(current):
            weight = graph[current][neighbor]['weight']
            distance = distances[current] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Перевіряємо, чи залишилися невідвідані вершини
        if len(visited) < len(graph.nodes()):
            # Вибираємо вершину з найменшою відстанню яку ще не відвідували
            candidates = {node: distances[node] for node in graph.nodes() if node not in visited}
            current = min(candidates, key=candidates.get)

    return distances

# Обираемо початкову станцію та викликаемо алгоритм Дейкстри
start_station = "Centrepoint"
dijkstra_distances = dijkstra(metro_graph, start_station)
print("Найкоротші відстані до кожної вершини від початкової станції:")
print(dijkstra_distances)
