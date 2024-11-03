import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = key

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def count_nodes(node):

    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def generate_color_gradient(num_colors):
    
    start_color = [0, 0, 128]  
    end_color = [240, 240, 255]  
    colors = []
    for i in range(num_colors):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / (num_colors - 1))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / (num_colors - 1))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / (num_colors - 1))
        colors.append('#%02x%02x%02x' % (r, g, b))
    return colors

def dfs(root):
    if root is None:
        return []

    stack = [root]
    visited = set()
    colors = generate_color_gradient(count_nodes(root))
    color_index = 0
    node_colors = {} 

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            node_colors[node.id] = colors[color_index]
            color_index += 1

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return node_colors

def bfs(root):
    if root is None:
        return []

    queue = deque([root])
    visited = set()
    colors = generate_color_gradient(count_nodes(root))
    color_index = 0
    node_colors = {} 

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            node_colors[node.id] = colors[color_index]
            color_index += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return node_colors

def draw_tree(tree_root, title="Binary Tree", node_colors=None):

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node_colors.get(node[0], "skyblue") for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід в глибину (DFS)
dfs_colors = dfs(root)
draw_tree(root, "DFS Traversal", dfs_colors)

# Обхід в ширину (BFS)
bfs_colors = bfs(root)
draw_tree(root, "BFS Traversal", bfs_colors)