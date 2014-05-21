from encoder import huffman

def print_code_table(code_table):
    for key in sorted(code_table.keys()):
        print(key, code_table[key], sep = " : ")

signals1 = {'A':0.25, 'B':0.05, 'C':0.10, 'D':0.25, 'E':0.20, 'F':0.15}
signals2 = {'A':0.4, 'B':0.2, 'C':0.2, 'D':0.1, 'E':0.1}
code1 = huffman(signals1)
code2 = huffman(signals2)

print_code_table(code1)

print()

print_code_table(code2)

