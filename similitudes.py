from scipy import spatial
import analisis_Lexico as al
import math
import numpy as np

def ficheroListaPalabras(fichero): 
    wordlist1 = []
    f1=open(fichero,'r',encoding="utf8")
    for linea1 in f1:
        wordlist1=wordlist1+linea1.split()
    return wordlist1

def frecuencias(wordlist,referencia):
    wordfreq = []
    for w in referencia:
        wordfreq.append(wordlist.count(w))
    return wordfreq

def frecuenciasFich(fichero):
    wordlist =ficheroListaPalabras(fichero)
    wordlist=al.preprocess(wordlist)
    return frecuencias(wordlist)

def similitud(freq1,freq2):
    numerador=0.0
    denominador1=0.0
    denominador2=0.0
    for i in range(len(freq1)):
        numerador+=freq1[i]*freq2[i]
        denominador1+=freq1[i]**2
        denominador2+=freq2[i]**2
    denominador=math.sqrt(denominador1)*math.sqrt(denominador2)
    if denominador==0:
        result=0
    else:
        result=numerador/denominador
    return result
        
def ordenarsimilitudes(d):
    l=[(k,v) for k, v in sorted(d.items(), key=lambda item: item[1])]#sorted es para insertar, d.items da cada elemento del diccionario(clave,valor) y luego de cada elemento ordena por la valor(posicion 1, la 0 es la clave), reverse para que sea de mayor a menor 
    l.reverse()
    return l