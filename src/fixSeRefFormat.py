import sys

seType = ""

def peek(f, size = 1):
    pos = f.tell()
    line = f.read(size)
    f.seek(pos)
    return line


with open(sys.argv[2]+".temp", "w") as out:

    with open(sys.argv[1]) as file:

        while True:
            c = file.read(1)
            if not c:
                break

            if c == "<":
                if peek(file) == "/":
                    while c != ">":
                        c = file.read(1)
                    out.write("_" + seType)
                else:

                    seType = ""

                    while c != '"':
                        c = file.read(1)

                    c = file.read(1)

                    while c != '"':
                        seType += c
                        c = file.read(1)

                    # print(seType)
                    file.read(1)
            else:
                out.write(c)

with open(sys.argv[2], "w") as out:

    with open(sys.argv[2]+".temp") as file:

        for line in file:
            if line == "\n": continue
            out.write(line.replace(". ", "\n").replace("Mr\n", "Mr. ").replace("Ms\n","Ms. "))

print("Wrote output at " + sys.argv[2])