import sys 


correspondance = {}

with open("tableCorrespondance.txt") as f:
    for line in f:
        w = line.split()
        correspondance[w[0]] = w[1]

# correspondance ===  {'Organization.ORGANIZATION': 'ORGANIZATION', 'Location.LOCATION': 'LOCATION', 'Person.PERSON': 'PERSON', '_': 'O'}

with open(sys.argv[2], "w") as out:

    with open(sys.argv[1]) as file:
        for line in file:
            if line != '\n':
                info = line.strip().split("\t")
                w, se = info[1], info[5]
                out.write(w + "/" + correspondance[se] + " ")
            else:
                out.write("\n")

