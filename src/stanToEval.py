import sys


with open(sys.argv[2], "w") as out:

    with open(sys.argv[1]) as file:
        for line in file:
            for word in line.split():
                se = word.split("/")[1]
                if se == "O":
                    out.write(word.replace("/O",""))
                else:
                    out.write(word.replace("/", "_"))
                out.write(" ")
            out.write("\n")
            

