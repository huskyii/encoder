#!/usr/bin/env python

__author__ = 'jiang'
__version__ = "Encoder 0.1\n"
__copyright__ = """Licensed under BSD 2-clause license.
Copyright (c) 2014 Jiang Zhu, mail.jiang.cn@gmail.com"""

# This is my homework for Information Theory and Coding.
# It implements three coding method: Shannon, Fano and Huffman.
# For more information about these three coding method, see
#
#
#
#
# Warning: DO NOT use it in production environment!
#
# Created on 2014-4-18
# Last modified on 2014-5-4

from docopt import docopt
from math import log2

usage = """%s
Usage:
    encoder [-hv] [-V] [-i FILE] [-o FILE] [-m METHODS]

Options:
    -h --help     show help message
    -v --version  show version
    -i FILE       input filename  [default: input.txt]
    -o FILE       output filename [default: output.txt]
    -m METHODS    coding method, it can be arbitrary combination
                  of Shannon, Fano, Huffman, separated by comma
""" % __version__

def Shannon(signals):
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
            tmp = ''
            for c in code :
                tmp += c
                if c == 'b':
                    for i in range(diff):
                        tmp += '0'
            code = tmp
        codes.append(code)
        aj += signal
    return codes

def Fano(signals):
    pass

def Huffman(signals):
    pass

def getSignalsFromFile(path):
    return signals

if __name__ == '__main__':
    args = docopt(usage, version=__version__ + __copyright__)
    if args['-m']:
        signals = getSignalsFromFile(args['-i'])
        methods = args['-m'].split(',')
        if 'Shannon' in methods:
            pass
        elif 'Fano' in methods:
            pass
        elif 'Huffman' in methods:
            pass


