import sys

correspondance = {}

#change les tags ptb en tags uni pour les fichirs stanford

with open("POSTags_PTB_Universal_Linux.txt") as f:
    for line in f:
        correspondance[line.split()[0]] = line.split()[1]

with open(sys.argv[2], "w") as out:
    with open(sys.argv[1]) as f:
        for line in f:
            for word in line.split():
                w, tag = word.split("_")[0], word.split("_")[1]
                out.write(w + "_" + correspondance[tag] + " ")
            out.write("\n")
