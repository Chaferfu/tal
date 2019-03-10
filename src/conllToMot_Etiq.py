import sys
import re

lineNb = 1

with open(sys.argv[2], "w") as out:

    with open(sys.argv[1]) as file:
        for line in file:
            if line != '\n':
                info = line.strip().split("\t")
                w, tag = info[1], info[3]
                # if lineNb == 89: print(w)
                w = re.sub('\s+', 'Espace', w)
                # if lineNb == 89:
                #     print(w)
                out.write(w + "_" + tag + " ")
            else:
                out.write("\n")
            lineNb += 1

