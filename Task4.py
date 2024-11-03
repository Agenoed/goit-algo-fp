import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = key  

def add_edges(graph, node, pos, i=0, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(heap):
            graph.add_edge(node.id, heap[left_child].id)
            l = x - 1 / 2 ** layer
            pos[heap[left_child].id] = (l, y - 1)
            add_edges(graph, heap[left_child], pos, left_child, l, y - 1, layer + 1)
        if right_child < len(heap):
            graph.add_edge(node.id, heap[right_child].id)
            r = x + 1 / 2 ** layer
            pos[heap[right_child].id] = (r, y - 1)
            add_edges(graph, heap[right_child], pos, right_child, r, y - 1, layer + 1)
    return graph

def draw_heap(heap):
    tree = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}
    tree = add_edges(tree, heap[0], pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


heap = [Node(0), Node(4), Node(1), Node(5), Node(10), Node(3)]


draw_heap(heap)