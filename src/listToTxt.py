import sys 
import re

#tranforme les listes mot   POSTAG en textes au format mot_POSTAG

with open(sys.argv[1]+".toText", "w") as out:

    with open(sys.argv[1]) as file:
        for line in file:
            info = line.strip().split("\t")
            w, tag = info[0].strip(), info[1]
            w = re.sub('\s+', 'Espace', w)
            out.write(w+"_"+tag+" ")

