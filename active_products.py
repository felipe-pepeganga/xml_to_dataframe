import urllib3
import xmltodict
import pprint
import json
import xml.etree.ElementTree as ET
import pandas as pd
import os

def exportar_csv():
    #PoolManager() instancia para realizar solicitudes
    http = urllib3.PoolManager()
    #Obtener xml
    r = http.request('GET', 'https://www.pepeganga.com/XMLData/test-impresee.xml')
    #Respuesta de la llamada
    print(r.status)
    #Diccionario JSON identado
    dict = json.dumps(xmltodict.parse(r.data), indent=4, sort_keys=True)
    diction_json = json.loads(dict)
    #items = diction_json.items()
    dict_keys = list(diction_json["Feed"]["Item"][0].keys())
    """print(dict_keys)
    #print(items[0])
    for item in diction_json["Feed"]["Item"]:
        #print(key, ":", diction_json[key])
        #print(item)
        break
    #print(diction_json)
    
    print("////")
    
    for i in dict_keys:
        print(i)"""

    df = pd.DataFrame(diction_json["Feed"]["Item"], columns=dict_keys)
    path = str(os.path.dirname(__file__))
    df.to_csv(path+'/dataframe.csv', index = False, header=True)
    print("Termino.")



