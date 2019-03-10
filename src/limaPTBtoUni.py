import sys
#convertit les tags PTB en tags universels en utilisant le fichierPOSTags_PTB_Universal_Linux.txt, doit etre lance depuis un repertoire contenant ce fichier (racine ou src)
correspondance = {} # dictionnaire qui fait le lien entre ptb et uni

with open("POSTags_PTB_Universal_Linux.txt") as f:
    for line in f:
        correspondance[line.split()[0]] = line.split()[1]

# print(correspondance)

with open(sys.argv[2], "w") as out:
    with open(sys.argv[1]) as f:
        for line in f:
            w, tag = line.strip().split('\t')[0], line.split('\t')[1]
            tag = tag.strip()
            print(w, tag)
            out.write(w + "\t" + correspondance[tag] + "\n")
