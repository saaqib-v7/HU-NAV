import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *


def dijkstra_shortest_path(graph, source, target):
    dist = {node: float('inf') for node in graph.nodes()}
    dist[source] = 0

    
    visited = set()
    unvisited = set(graph.nodes())

    while unvisited:
        
        current_node = min(unvisited, key=dist.get)

        
        if current_node == target:
            break

        
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                distance_to_neighbor = dist[current_node] + graph.get_edge_data(current_node, neighbor)['weight']
                if distance_to_neighbor < dist[neighbor]:
                    dist[neighbor] = distance_to_neighbor

        
        visited.add(current_node)
        unvisited.remove(current_node)

    
    path = [target]
    while path[-1] != source:
        for neighbor in graph.neighbors(path[-1]):
            if dist[path[-1]] == dist[neighbor] + graph.get_edge_data(path[-1], neighbor)['weight']:
                path.append(neighbor)
                break

    return path[::-1]


def draw_map_with_shortest_path(graph, shortest_path, positions):
    nx.draw(graph, positions, with_labels=True, node_color='lightblue', edge_color='cyan')
    edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
    nx.draw_networkx_edges(graph, positions, edgelist=edges, edge_color='r', width=2)
    plt.show()


G = nx.Graph()
edges=[("C-001","C-004",1),("C-001","C-007",2),("C-001","E-002",2),("C-001","E-003",3),("C-001","E-010",5),("C-001","E-011",6),("C-001","E-012",7),("C-001","E-013",3),("C-001","Amphitheatre",5),("C-001","E-017",4),("C-001","C-015",6),("C-001","C-017",8),("C-001","C-023",7),("C-001","C-022",8),("C-001","Learn courtyard",1),("C-001","C-025",5),("C-001","W-004",5),("C-001","W-007",6),("C-001","Swimming pool",9),("C-001","Courts",10),("C-004","C-001",1),("C-004","C-007",1),("C-004","E-002",2),("C-004","E-003",3),("C-004","E-010",5),("C-004","E-011",6),("C-004","E-012",7),("C-004","E-013",3),("C-004","Amphitheatre",4),("C-004","E-017",4),("C-004","C-015",5),("C-004","C-017",6),("C-004","C-023",6),("C-004","C-022",7),("C-004","Learn courtyard",2),("C-004","C-025",6),("C-004","W-004",6),("C-004","W-007",7),("C-004","Swimming pool",9),("C-007","C-001",2),("C-007","C-004",1),("C-007","E-013",1),("C-007","E-017",2),("C-007","E-012",2),("C-007","E-011",3),("C-007","E-010",4),("C-007","E-003",6),("C-007","E-002",7),("C-007","Amphitheatre",2),("C-007","C-015",3),("C-007","C-017",5),("C-007","C-023",5),("C-007","C-022",6),("C-007","Swimming pool",7),("C-007","Learn courtyard",3),("C-007","C-025",5),("C-007","W-004",5),("C-007","W-007",6),("E-002","E-003",1),("E-002","C-001",1),("E-002","C-004",2),("E-002","C-007",3),("E-002","E-010",3),("E-002","E-011",4),("E-002","E-012",5),("E-002","E-013",4),("E-002","E-017",5)]
G.add_weighted_edges_from(edges)


source = input("From:")
target = input('To:')


shortest_path = dijkstra_shortest_path(G, source, target)
print(f"Shortest path from {source} to {target}: {shortest_path}")


positions = {
    'C-001': (3, 4),
    'C-004': (5, 4),
    'C-007': (3, 2),
    'E-002': (5, 2),
    'E-003': (4, 1),
    'E-010': (6, 4),
    'E-011': (7, 3),
    'E-012': (8, 2),
    'E-013': (7, 1),
    'E-017': (8, 1),
    'Amphitheatre': (4, 3),
    'C-015': (6, 5),
    'C-017': (7, 4),
    'C-023': (8, 3),
    'C-022': (9, 2),
    'Learn courtyard': (2, 4),
    'C-025': (8, 5),
    'W-004': (2, 6),
    'W-007': (3, 5),
    'Swimming pool': (10, 4),
    'Courts': (11, 3)
}





root = Tk()
root.title("University Map")


canvas = Canvas(root, width=800, height=600, bg='purple')
canvas.pack()
canvas.create_text(400, 300, text="HABIB UNIVERSITY", fill='white', font=('Arial', 30), anchor='center')


show_graph_button = Button(root, text="Show Map", command=lambda: draw_map_with_shortest_path(G, shortest_path, positions))
show_graph_button.pack(side=TOP, padx=5, pady=5)


root.mainloop()

