import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.Graph()

pc_nodes = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5']
router_nodes = ['Router1', 'Router2', 'Router3', 'Router4', 'Router5']

G.add_nodes_from(pc_nodes)
G.add_nodes_from(router_nodes)

edges = [
    ('PC1', 'Router1'),
    ('PC2', 'Router2'),
    ('PC3', 'Router3'),
    ('PC4', 'Router4'),
    ('PC5', 'Router5'),
    ('Router1', 'Router2'),
    ('Router2', 'Router3'),
    ('Router3', 'Router4'),
    ('Router4', 'Router5'),
    ('Router5', 'Router1')
]

G.add_edges_from(edges)

pos = {}
angle_step = 2 * 3.14159 / len(router_nodes)
radius = 5

for i, router in enumerate(router_nodes):
    pos[router] = (radius * np.cos(i * angle_step), radius * np.sin(i * angle_step))

side_length = 7
pos['PC1'] = (side_length, 0)
pos['PC2'] = (side_length / 2, side_length / 2)
pos['PC3'] = (0, side_length)
pos['PC4'] = (-side_length, 0)
pos['PC5'] = (0, -side_length)

def ping(node1, node2):
    try:
        if nx.has_path(G, node1, node2):
            print(f'{node1} може пінгувати {node2}. Шлях існує.')
        else:
            print(f'{node1} не може пінгувати {node2}. Шлях відсутній.')
    except nx.NetworkXError as e:
        print(f'Помилка: {e}')

for node1 in G.nodes:
    for node2 in G.nodes:
        if node1 != node2:
            ping(node1, node2)

plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight='bold', edge_color="gray")

plt.title('Мережа з 5 комп\'ютерів і 5 роутерів', fontsize=14)
plt.show()
