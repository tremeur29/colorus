import os

path = (os.path.dirname(os.path.abspath(__file__)))

f = open(path + "/var.txt", "r")

g = open(path + "/newvars.txt", "w+")

for line in f:
    shortline = line[45:-14]
    preserve = int((len(shortline) - 1)/2)
    newline = shortline[:preserve]
    g.write(newline + "\n")

f.close()
g.close()
