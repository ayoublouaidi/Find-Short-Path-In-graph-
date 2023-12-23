from collections import deque
import time
import matplotlib.pyplot as plt
import networkx as nx

# Définition du graphe sous forme d'adjacency list avec des poids
graph_data = {
    "Saulx": {"Villejuste": 4, "Longjumeau": 2 ,"Champlin" :3},
    "Villejuste": {"Saulx": 4, "Villebon": 7, "Ulis": 7},
    "Longjumeau": {"Saulx": 2, "Champlin": 3},
    "Villebon": {"Saulx": 6, "Villejuste": 7, "Champlin": 5, "Ulis": 7, "Palaiseau": 7},
    "Champlin": {"Longjumeau": 4, "Villebon": 5, "Ulis": 7, "Chilly": 6, "Massy": 4},
    "Ulis": {"Villejuste": 7, "Villebon": 7, "Champlin": 7, "Orsay": 7},
    "Chilly": {"Champlin": 6, "Gif": 5, "Wissous": 6, "Bures": 5},
    "Gif": {"Chilly": 5, "Orsay": 7, "Palaiseau": 5, "Saclay": 7},
    "Orsay": {"Ulis": 7, "Gif": 7, "Palaiseau": 10, "Massy": 2},
    "Palaiseau": {"Villebon": 7, "Gif": 5, "Orsay": 10, "Massy": 7, "Vauhallan": 5, "Igny": 4},
    "Massy": {"Champlin": 4, "Orsay": 2, "Palaiseau": 7, "Wissous": 5, "Saclay": 5, "Vauhallan": 4, "Igny": 5, "Antony": 5, "Biévres": 4},
    "Wissous": {"Chilly": 6, "Bures": 5, "Massy": 5},
    "Bures": {"Chilly": 5, "Orsay": 3, "Igny": 4},
    "Saclay": {"Gif": 7, "Palaiseau": 5, "Massy": 3, "Vauhallan": 7},
    "Vauhallan": {"Palaiseau": 5, "Massy": 4, "Saclay": 7, "Igny": 2, "Biévres": 4},
    "Igny": {"Palaiseau": 4, "Massy": 5, "Bures": 4, "Vauhallan": 2},
    "Antony": {"Massy": 5},
    "Biévres": {"Massy": 4, "Vauhallan": 4, "Verriéres": 6},
    "Verriéres": {"Biévres": 6}
}

# Création d'un graphe dirigé avec NetworkX
G = nx.DiGraph()

for source, targets in graph_data.items():
    for target, weight in targets.items():
        G.add_edge(source, target, weight=weight)

# Trouver le plus court chemin
shortest_path = nx.shortest_path(G, source="Saulx", target="Verriéres", weight="weight")


pos = nx.spring_layout(G , scale = 10)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=690, node_color='skyblue', font_size=8, arrowsize=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Dessiner le plus court chemin en rouge
edge_colors = ['red' if (shortest_path[i], shortest_path[i + 1]) in G.edges else 'black' for i in range(len(shortest_path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)], edge_color=edge_colors, width=2)

plt.show()

# Implémentation de BFS avec poids
def bfs_with_weights(graph, start, target):
    queue = deque([(start, [start], 0)])
    visited = set()

    while queue:
        node, path, weight = queue.popleft()

        if node not in visited:
            neighbors = graph[node]

            for neighbor, edge_weight in neighbors.items():
                if neighbor == target:
                    return path + [neighbor], weight + edge_weight

                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], weight + edge_weight))

            visited.add(node)

# Implémentation de DFS avec poids
def dfs_with_weights(graph, start, target):
    stack = [(start, [start], 0)]
    visited = set()

    while stack:
        node, path, weight = stack.pop()

        if node not in visited:
            neighbors = graph[node]

            for neighbor, edge_weight in neighbors.items():
                if neighbor == target:
                    return path + [neighbor], weight + edge_weight

                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], weight + edge_weight))

            visited.add(node)


# Recherche de chemin avec BFS avec poids
bfs_path, bfs_weight = bfs_with_weights(graph_data, "Saulx", "Verriéres")
print("Chemin trouvé par BFS:", bfs_path)
print("Poids total:", bfs_weight)

# Recherche de chemin avec DFS avec poids
dfs_path, dfs_weight = dfs_with_weights(graph_data, "Saulx", "Verriéres")
print("Chemin trouvé par DFS:", dfs_path)
print("Poids total:", dfs_weight)


