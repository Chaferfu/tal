import xml.etree.ElementTree as ET
import sys 
# from prettytable import PrettyTable 
occurences = {}
nbMots = 0

# print(sys.argv[1])
tree = ET.parse(sys.argv[1])
root = tree.getroot()

for child in root:
	word = {}
	for att in child:
		if att.tag == "lemma":
			word["lemma"] = att.text
		if att.tag == "macro":
			word["macro"] = att.text
	print(word)
			


words = etree.Element("vertex")

print(words)

for entity, value in occurences.items():
	print("{:>25}\t\t{:>25}\t\t{:>5}\t\t{:.2f}\t\t".format(entity,value[0],value[1],value[1]/nbMots))