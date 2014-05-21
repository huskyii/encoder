__author__ = 'jiang'
__version__ = "Encoder 0.1\n"
__copyright__ = """Licensed under BSD 2-clause license.
Copyright (c) 2014 Jiang Zhu, mail.jiang.cn@gmail.com"""

# This is my homework for Information Theory and Coding.
# It implements two coding method: Shannon and Huffman.
#
# Warning: DO NOT use it in production environment!
#
# Created on 2014-4-18

from math import log2

from util import is_parameter_legal, add_pre_zero

def shannon(signals):
    """convert a list of signals to a list of code using Shannon coding method

    arguments:
        signals     a list of probabilities of signal's occurrence

    return
        a list of code using Shannon coding method
    """

    if not is_parameter_legal(signals):
        raise ValueError('signals should be a list of probabilities and sum of them should be 1.')
    epsilon = 1e-100
    signals.sort(reverse = True)
    codes = []
    aj = 0
    for signal in signals:
        code_len = int(1 - log2(signal))
        if 1 - log2(signal) - code_len < epsilon:
            code_len -= 1
        code = bin(int(aj * 2**code_len ))
        diff = code_len+2 - len(code)
        if diff > 0:
            code = add_pre_zero(code,diff)
        codes.append(code)
        aj += signal
    return codes


def huffman(signals):
    pass


