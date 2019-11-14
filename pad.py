import os
from os.path import expanduser
home = expanduser("~")

path = (os.path.dirname(os.path.abspath(__file__)))

f = open(path + "/newvars2.txt", "r")

tote = sum(1 for line in f)

f.close()

g = open(path + "/newvars2.txt", "r")

i = 1

if tote == 1:
    for line in g:
        if i == 1:
            linetem = line
        i+=1
    line1 = linetem
    line2 = linetem
    line3 = linetem
    line4 = linetem
    line5 = linetem

if tote == 2:
    for line in g:
        if i == 1:
            linetem1 = line
        elif i == 2:
            linetem2 = line
        i+=1
    line1 = linetem1
    line2 = linetem2
    line3 = linetem1
    line4 = linetem2
    line5 = linetem1

if tote == 3:
    for line in g:
        if i == 1:
            linetem1 = line
        elif i == 2:
            linetem2 = line
        elif i == 3:
            linetem3 = line
        i+=1
    line1 = linetem1
    line2 = linetem2
    line3 = linetem3
    line4 = linetem1
    line5 = linetem2

if tote == 4:
    for line in g:
        if i == 1:
            linetem1 = line
        elif i == 2:
            linetem2 = line
        elif i == 3:
            linetem3 = line
        elif i == 4:
            linetem4 = line
        i+=1
    line1 = linetem1
    line2 = linetem2
    line3 = linetem3
    line4 = linetem4
    line5 = linetem1

if tote > 4:
    for line in g:
        if i == 1:
            linetem1 = line
        elif i == 2:
            linetem2 = line
        elif i == 3:
            linetem3 = line
        elif i == 4:
            linetem4 = line
        elif i == 5:
            linetem5 = line
        i+=1
    line1 = linetem1
    line2 = linetem2
    line3 = linetem3
    line4 = linetem4
    line5 = linetem5

g.close()

h = open(home + "/.colourvars", "w+")

h.write("LINE1=" + line1)
h.write("LINE2=" + line2)
h.write("LINE3=" + line3)
h.write("LINE4=" + line4)
h.write("LINE5=" + line5)

h.close()
