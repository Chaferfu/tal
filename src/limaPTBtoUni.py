import sys

correspondance = {}

with open("POSTags_PTB_Universal_Linux.txt") as f:
    for line in f:
        correspondance[line.split()[0]] = line.split()[1]

print(correspondance)

with open(sys.argv[2], "w") as out:
    with open(sys.argv[1]) as f:
        for line in f:
            w, tag = line.strip().split('\t')[0], line.split('\t')[1]
            tag = tag.strip()
            print(w, tag)
            out.write(w + "\t" + correspondance[tag] + "\n")
