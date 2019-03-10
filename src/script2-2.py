from lxml import etree
import sys 
# from prettytable import PrettyTable 

#Affiche ce qui est demande dans la parite 2-2
#simple parcours d'arbre xml
#a utiliser sur les fichiers .xml

# print(sys.argv[1])
tree = etree.parse(sys.argv[1])
babu = tree.xpath("/specific_entities/specific_entity")

occurences = {}
nbMots = 0


for se in babu:
	if se[0].text not in occurences.keys():
		occurences[se[0].text] = [se[3].text, 1]
	else:
		occurences[se[0].text][1] += 1;
	nbMots += 1
	# print(se[0].text, occurences[se[0].text][1])


for entity, value in occurences.items():
	print("{:>25}\t\t{:>25}\t\t{:>5}\t\t{:.2f}\t\t".format(entity,value[0],value[1],value[1]/nbMots))