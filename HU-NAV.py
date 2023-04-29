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


data_set_complete = ['W-244','W-243',20],['W-243','W-242',39],['N-219','N-220',10],['N-220','C-200',32],['N-220','Courtyard Stairs',153],['W-242','Vending Machine Stairs',122],['W-234','Courtyard Lifts',17],['W-242','Courtyard Lifts',75],['C-200','Reception Lifts',18],['Courtyard Lifts','Courtyard Stairs',37],['E-220','Vending Machine Stairs',38],['C-200','Courtyard Stairs',133],['Courtyard Stairs','Vending Machine Stairs',142],['C-007','Reception Lifts',181],['Reception Stairs','C-001',102],['Reception Stairs','E-002',147],['W-100','W-110',22],  ['Reception Lifts','Entrance Stairs',102], ['Courtyard Stairs','Courtyard Lifts',35],['Courtyard Stairs','W-118',189],['Courtyard Stairs','W-111',189],  ['W-118','W-110',191], ['W-111','W-110',191],['W-118','W-100',189],['W-111','W-100',189],['E-101','Vending Machine Stairs',260],['E-121','Amphi Stairs',86],['W-121','W-118',10],['W-114','W-111',10],['W-118','W-111',18],['E-101','Ramp',48 ], ['C-109','E-101',244], ['W-118','C-109',144],['W-110','Courtyard Stairs',50],['W-100','Courtyard Stairs',48],['C-109','Courtyard Stairs',61],['C-109','Courtyard Lifts',96],['W-118','Courtyard Lifts',184],['W-111','Courtyard Lifts',184],['E-121','Tapal Stairs',46],['C-109','Tapal Stairs',98],['E-101','Tapal Stairs',250],['Reception Lifts','Reception Stairs',65],['Reception Stairs','Entrance Stairs',42],['Entrance Stairs','E-101',165],['Entrance Stairs','C-109',199],['W-118','Amphi Stairs',104],['W-111','Amphi Stairs',104],['E-100','Reception Lifts',93],['E-100','Reception Stairs',64],['E-100','Entrance Stairs',101]['Courtyard Lifts','W-321',39],['Courtyard Lifts','Courtyard Stairs',60]

lg_lecture_rooms = ['C-015','E-011','E-012','E-002']
gf_lecture_rooms=['E-121','C-109','E-101','E-100']
ff_lecture_rooms = ['W-243','W-242','W-234','C-200','N-220','N-219','E-220','E-215']
sf_lecture_rooms=['W-321']   
lg_labs = ['E-010','E-003','C-007','C-004','C-001','C-025']
gf_labs = ['W-121','W-118','W-111','W-114','W-110','W-100']
ff_labs = ['E-226','W-244']
sf_labs = ['W-311']     
lg_staircases_and_lifts = ['Reception Stairs','Amphi Stairs','Entrance Stairs','Tapal Stairs','Ramp','Courtyard Stairs','Courtyard Lifts','Reception Lifts']
gf_staircases_and_lifts = ['Reception Stairs','Amphi Stairs','Entrance Stairs','Tapal Stairs','Ramp','Vending Machine Stairs','Courtyard Stairs','Courtyard Lifts','Reception Lifts']
ff_staircases_and_lifts = ['Reception Stairs','Vending Machine Stairs','Courtyard Stairs','Courtyard Lifts','Reception Lifts']
sf_staircases_and_lifts = ['Courtyard Stairs','Courtyard Lifts']