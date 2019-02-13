from lxml import etree

tree = etree.parse("wsj_0010_sample.txt.se.xml")
babu = tree.xpath("/specific_entities/specific_entity")
print(babu)
for se in babu:
	print("{}\t\t{}\t\t{}\t\t{}\t\t".format(se[0].text,se[3].text,se[2].text,se[1].text))