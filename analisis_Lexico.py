import numpy as np
from nltk.tokenize import word_tokenize 
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

def pasarMinusculas(data):
    return np.char.lower(data)

def listaParada(data):
    stop_words = stopwords.words('spanish')
    new_text = ""
    for w in data:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text

def simbolosPuntuacion(data):
    symbols = "!$%&()*+-./:;<=>?@[]^`{|}~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
    data = np.char.replace(data, ',', '')
    return data

def quitarApostrofes(data):
    return np.char.replace(data, "'", "")

def stemming(data):
    stemmer= SnowballStemmer('spanish')
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text

def preprocess(data):
    data=np.array(data)
    data = pasarMinusculas(data)
    data = simbolosPuntuacion(data)
    #print("puntuacion:",data,"tipo:",type(data),"\n\n")
    #print("apostrofe:",data,"tipo:",type(data),"\n\n")
    data = quitarApostrofes(data)
    #data = listaParada(data)
    #print("stopwords:",data,"tipo:",type(data),"\n\n")
    data = stemming(data)
    data = quitarApostrofes(data)
    return str(data)

data="Hola"
print(preprocess(data))
    