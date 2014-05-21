__author__ = 'jiang'
__version__ = "Encoder 0.1\n"
__copyright__ = """Licensed under BSD 2-clause license.
Copyright (c) 2014 Jiang Zhu, mail.jiang.cn@gmail.com"""

# This is my homework for Information Theory and Coding.
# It implements one coding method(Huffman) for now.
#
# Warning: DO NOT use it in production environment!
#
# Created on 2014-4-18

from util import is_parameter_legal, signals_to_tree, build_huffman_tree, build_code_table

def huffman(signals):
    """convert a list of signals to a code table using Huffman coding method

    arguments:
        signals     a dict that follows the format
                    {symbol1 : probability1, symbol2 : probability2, ... }

    return
        code_table  a dict that follows the format
                    { symbol1 : code1, symbol1 : code1, ... }
    """

    if not is_parameter_legal(signals):
        raise ValueError('signals should be a list of probabilities and sum of them should be 1.')

    trees = signals_to_tree(signals)

    tree = build_huffman_tree(trees)

    code_table = build_code_table(tree.root,{})

    return code_table


