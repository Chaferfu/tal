import xml.etree.ElementTree as ET
import sys 
# from prettytable import PrettyTable 
occurences = {}
nbMots = 0

# print(sys.argv[1])

tree = ET.parse(sys.argv[1])
root = tree.getroot()

for child in root:
	nbMots+=1
	word = {}
	for att in child:
		if att.tag == "lemma":
			word["lemma"] = att.text
		if att.tag == "macro":
			word["macro"] = att.text
	if word["lemma"] in occurences.keys():
		occurences[word["lemma"]][0] += 1
	else:
		occurences[word["lemma"]] = [1, word["macro"]]
		



for entity, value in occurences.items():
	print("{:>25}\t\t{:>8}\t\t{:>5}\t\t{:.2f}\t\t".format(entity,value[1],value[0],value[0]/nbMots))