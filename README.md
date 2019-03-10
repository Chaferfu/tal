# tal

pour lancer les script depuis le dossier tal:

en indiquant le ficher input, affiche le resultat dans la console, le resultat peut etre redirigé dans un fichier si besoin
* script2-2.py
* script4-2
* scriptForDisambiguatedXML.py

ex depuis la racine du projet
python src/script2-2.py samples/wsj_0010_sample.txt.se.xml > outputs/out.txt
(la lib lxml doit etre installée)

s'utilisent en indiquant fichier source ET dest
* conllToMot_Etiq.py 
* fixSeRefFormat.py
* limaPTBtoUni.py
* limaToStan.py
* stanPOStoUni.py
* stanToEval.py

ex
python src src/conllToMot_Etiq.py samples/blabla.conll outputs/out.txt

s'utilisent en indiquant seulement le fichier input, un fichier out est créé au meme endroit avec une extension suppelementaire
* listToTxt.py

ex
python src/listToTxt.py samples/blabla.pos outputs/out.txt

