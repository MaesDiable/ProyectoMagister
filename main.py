import codecs
from liwc import Liwc

#Hay que sacar todos los que no tengan temas de interacción social y
#lwic = Liwc("dataSource/Spanish_LIWC2007_Dictionary.dic")

#print(lwic.search("crear"))
#print(lwic.categories)


f = codecs.open("dataSource/Spanish_LIWC2007_Dictionary.dic","r","utf-8")
print(f.read())