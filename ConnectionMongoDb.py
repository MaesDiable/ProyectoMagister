import pymongo

client = pymongo.MongoClient()

Db = client["ProyetoMagister"]
Db = client["word"]
Db = client["wordwild"]
def Connection():
    client = pymongo.MongoClient()
    Db = client["ProyectoMagister"]
    return Db