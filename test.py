from encoder import shannon
signals = [0.25, 0.05, 0.10, 0.25, 0.20, 0.15]
code = shannon(signals)

for elem in code:
  print(elem)
print (type(code[0]))
