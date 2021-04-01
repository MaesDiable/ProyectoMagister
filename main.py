import codecs
from liwc import Liwc

#Hay que sacar todos los que no tengan temas de interacción social y
lwicDicctionary = Liwc("dataSource/Spanish_LIWC2007_Dictionary.dic")

print(lwicDicctionary.search("crear"))


