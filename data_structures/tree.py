

class tree_node:
    def __init__(self, value, parent=None, children=[]):
        self.value = value
        self.parent = parent
        self.children = children

class tree:
    def __init__(self, root_value=None):
        self.root = None if root_value is None else tree_node(root_value)
        self.size = 0 if self.root is None else 1

    # cases: empty tree with no nodes, tree with only root node, tree with root node that has children
    def set_root(self, root_value):
        self.size = 1 if self.root is None else self.size
        self.root = tree_node(root_value, children=self.root.children) if self.root is not None else tree_node(root_value)


    def add_child(self, value, parent):
        child_node = tree_node(value, parent)
        self.size += 1
        parent.children.append(child_node)

    def max_depth(self, root): # this function should return the maximum depth of the tree (max number of nodes from root to leaf, max length of path from root to leaf)
        if root is None:
            return 0
        if len(root.children) == 0:
            return 1
        depths = []
        for child in root.children:
            depths.append(self.max_depth(child))
        return max(depths) + 1

    def min_depth(self, root): # same as above but min
        if root is None:
            return 0
        if len(root.children) == 0:
            return 1
        depths = []
        for child in root.children:
            depths.append(self.min_depth(child))
        return min(depths) + 1

    def max_sum_path(self, root): # if each node has a value, return the max sum of a path from root to leaf
        if root is None:
            return 0
        if len(root.children) == 0:
            return root.value
        values = []
        for child in root.children:
            values.append(self.max_sum_path(child))
        return max(values) + root.value

def dfs(root):
    if root is None:
        return None
    if len(root.children) == 0:
        print(root.value)
        return
    print(root.value)
    for child in root.children:
        dfs(child)

# time complexity: O(n)
# space complexity: O(n)