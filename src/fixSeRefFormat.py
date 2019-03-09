import sys

seType = ""

def peek(f, size = 1):
    pos = f.tell()
    line = f.read(size)
    f.seek(pos)
    return line


with open(sys.argv[2], "w") as out:

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

                

        

