import sys

#bad ??

with open(sys.argv[2], "w") as out: #output file
	with open(sys.argv[1]) as f: #input file


	  for line in f:
	  	for word in line.split(): 
	  		
	  		ent = word.split("_")
	  		# print(ent)
	  		out.write(ent[0])
	  		out.write(" \t")
	  		out.write(ent[1])
	  		out.write("\n")


