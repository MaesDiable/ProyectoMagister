import codecs
import ConnectionMongoDb
import json


class Word:
    valor = ''
    classification = []


def LineToWord(LineaCategoria):
    listacategoriatexto = LineaCategoria.split("\t")
    word = Word()
    listacategorynumeros = []
    word.valor = listacategoriatexto.pop(0)
    for category in listacategoriatexto:
        listacategorynumeros.append(int(category))
    word.classification = listacategorynumeros
    return word


def getwords(archivoDiv, option):
    dictionary = archivoDiv.split("%")[2].splitlines()
    dictionary.pop(0)
    dictionarywords = [Word]
    dictionarywordswild = [Word]
    for linea in dictionary:
        if linea != "" and ('121' in linea or '125' in linea):
            if "*" in linea:
                wordwildcard = LineToWord(linea)
                dictionarywordswild.append(wordwildcard)
            else:
                word = LineToWord(linea)
                dictionarywords.append(word)
    if option == 1:
        finallist = dictionarywords
    else:
        finallist = dictionarywordswild
    finallist.pop(0)
    return finallist

def encoderword(word):
    return {'valor': word.valor, 'classification': word.classification}

def sendListDataBase(wordlist):
    column = ConnectionMongoDb.Connection()["word"]
    listtosend = [{}]
    for word in wordlist:
        value = json.dumps(word, default=encoderword)
        listtosend.append(value)
    for asd in listtosend:
        print(asd)
        #listtosend.append(value)
    #value = json.dumps(value)
    column.insert_many(listtosend)
    # column = ConnectionMongoDb.Connection()["wordwild"]
    # column.insert_many(dictionarywordswild)
    ##value = json.dumps(word)
    # column.insert(word)
    return 0




# 121 social, 125 afect
def main():
    f = codecs.open("dataSource/Spanish_LIWC2007_Dictionary.dic", "r", "utf-8")
    g = codecs.open("dataSource/Spanish_LIWC2007_Dictionary.dic", "r", "utf-8")
    commonwords = getwords(f.read(), 1)
    wildwords = getwords(g.read(), 2)
    sendListDataBase(commonwords)
    #sendListDataBase(wildwords)



main()
