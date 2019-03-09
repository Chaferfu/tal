import sys
import re


with open(sys.argv[2], "w") as out:

    with open(sys.argv[1]) as file:

        data = file.read()
        data = re.sub('([.,!?()])', r' \1 ', data)
        data = re.sub('\data{2,}', ' ', data)
        out.write(data)

