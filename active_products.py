import urllib3
import xmltodict
import pprint
import json
import xml.etree.ElementTree as ET
import pandas as pd
import os
from csv import writer
from csv import reader
import csv

def exportar_csv():
    #PoolManager() instancia para realizar solicitudes
    http = urllib3.PoolManager()
    #Obtener xml
    r = http.request('GET', 'https://www.pepeganga.com/XMLData/test-impresee.xml')
    #Respuesta de la llamada
    #Diccionario JSON identado
    dict = json.dumps(xmltodict.parse(r.data), indent=4, sort_keys=True)
    diction_json = json.loads(dict)
    #items = diction_json.items()
    dict_keys = list(diction_json["Feed"]["Item"][0].keys())
    df = pd.DataFrame(diction_json["Feed"]["Item"], columns=dict_keys)
    path = str(os.path.dirname(__file__))
    df.to_csv(path+'/dataframe.csv', index = False, header=True)

def plu():
    csv = pd.read_csv("dataframe.csv")
    df = pd.DataFrame(csv)
    df['Plu'] = df['Plu'].astype(str)
    TK=df['Plu'].astype(str)
    df=df.assign(Plu_mod=plu_mod(TK.values))
    path = str(os.path.dirname(__file__))
    df.to_csv(path+'/dataframe_mod.csv', index = False, header=True)
    
def plu_mod(plus):
    plus_mod = []
    for plu in plus:
        numS = str(plu)     
        if len(numS) < 6:
            if len(numS) == 1:
                plu = "00000" + str(plu)
                plus_mod.append(plu)
            if len(numS) == 2:
                plu = "0000" + str(plu)
                plus_mod.append(plu)
            if len(numS) == 3:
                plu = "000" + str(plu)
                plus_mod.append(plu)
            if len(numS) == 4:
                plu = "00" + str(plu)
                plus_mod.append(plu)
            if len(numS) == 5:
                plu = "0" + str(plu)
                plus_mod.append(plu)
        else:
            plus_mod.append(plu)

    for plu in plus_mod:
        print(plu)
    return plus_mod



