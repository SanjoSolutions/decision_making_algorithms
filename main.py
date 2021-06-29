class Tree:
    def __init__(self, root):
        self.root = root


class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []

    def add_child(self, node):
        self.children.append(node)


tree = Tree(root=Node())
tree.root.add_child(Node())


def expand_tree(node):
    create_children(node)


def create_children(node):
    pass
