__author__ = 'jiang'

def is_parameter_legal(signals):
    if isinstance(signals,dict) and sum([signals[key] for key in signals.keys()]) == 1:
        return True
    return False


def signals_to_tree(signals):
    trees = []
    for symbol,probability in signals.items():
        node = Huff_node(probability,symbol)
        tree = Btree(node)
        trees.append(tree)
    trees.sort(key = lambda x : x.root.probability )
    return trees


class Huff_node():
    def __init__(self, probability = 0, symbol = None):
        self.right = None
        self.left = None
        self.code = '0'
        self.symbol = symbol
        self.probability = probability

    def add_right(self, right):
        self.right = right

    def add_left(self, left):
        self.left = left


class Btree():
    def __init__(self,root = None):
        self.root = root

    def merge(self, right, left):
        self.root = Huff_node( right.root.probability + left.root.probability )
        self.root.add_left(left.root)
        self.root.add_right(right.root)


def build_code_table(root, code_table):
    """
    return a dict that follows format
    { symbol1 : code1 , symbol2 : code2 , ... }
    """
    if root.left is None and root.right is None :
        code_table[root.symbol] = root.code[1:]
    if root.right is not None :
        root.right.code = root.code + '1'
        build_code_table(root.right, code_table)
    if root.left is not None :
        root.left.code = root.code + '0'
        build_code_table(root.left, code_table)
    return code_table



def build_huffman_tree(trees):
    while len(trees) >= 2:
        tree = Btree()
        tree.merge(trees[0], trees[1])
        trees.pop(0)
        trees.pop(0)
        trees.append(tree)
        trees.sort(key = lambda x : x.root.probability)
    return trees[0]
