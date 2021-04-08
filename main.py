import codecs

class Palabra:
    valor = ''
    categoria = []

def limpiarCategoria(LineaCategoria):
    listaCategoria = LineaCategoria.split("\t")
    palabra = Palabra()
    palabra.valor = listaCategoria.pop(0)
    palabra.categoria = listaCategoria
    return palabra

def obtenerPalabras(archivoDiv):
    diccionarioSinFunciones = archivoDiv.split("%")[2].splitlines()
    for linea in diccionarioSinFunciones:
        if linea != "":
            if "*" in linea:
                palabraWildCard = limpiarCategoria(linea)
                print(palabraWildCard.valor,palabraWildCard.categoria)
            else:
                palabra = limpiarCategoria(linea)
    return


f = codecs.open("dataSource/Spanish_LIWC2007_Dictionary.dic","r","utf-8")
#121 social, 125 afect
obtenerPalabras(f.read())