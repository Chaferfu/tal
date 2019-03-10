import sys
import re

#OBSOLETE

with open(sys.argv[1]+".clean", "w") as out:

    with open(sys.argv[1]) as file:
        for line in file:
            out.write(re.sub('\s+', '\t', line))
            out.write("\n")

