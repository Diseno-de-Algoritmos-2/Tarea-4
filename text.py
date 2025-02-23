

from heapq import heappush, heappop, heapify
from math import log2, ceil

# ------------------------------------------------
# TEXTO Y ALFABETO
# ------------------------------------------------

TEXT = "AABEEWFEBKAEFBKEAFEA"

def obtain_alphabet_probabilities(text):

    alphabet = {}
    for i in range(len(text)):
        alphabet[text[i]] = alphabet.get(text[i], 0)
        alphabet[text[i]] = alphabet[text[i]] + 1
    
    probabilities = {}
    for key in alphabet:
        probabilities[key] = alphabet[key] / len(text)
    
    return probabilities


def sort_probabilities(probabilities):
    heap = []

    for key in probabilities:
        heappush(heap, (-probabilities[key], key))

    return heap

# ------------------------------------------------
# ENTROPÍA
# ------------------------------------------------

# 1. Peor Caso
def entropy_worst_case(probabilities):
    return log2(len(probabilities))


# ------------------------------------------------
# CODIFICACIÓN SHANNON-FANO
# ------------------------------------------------

# 1. Códigos de Shannon-Fano de un alfabeto.

def shannon_fano(probabilities):

    # Calculamos las longitudes de los códigos
    longitudes = {symbol: ceil(-log2(-prob)) for prob, symbol in probabilities}
    heapify(probabilities)
    
    # Inicializamos el diccionario de codificación
    codificacion = {}
    first = heappop(probabilities)
    codificacion[first[1]] = '0' * longitudes[first[1]]
   
    # Inicializamos las variables para la primera iteración
    prev_code_int = 0  
    prev_symbol = first[1]

    # Iteramos sobre las probabilidades
    while probabilities:
        current = heappop(probabilities)
        symbol = current[1]

        # d[i] = L[symbol] - L[prev_symbol]
        d = longitudes[symbol] - longitudes[prev_symbol]

        # Calculamos el nuevo código: (código anterior + 1) * 2^d
        new_code_int = (prev_code_int + 1) << d  # << d equivale a multiplicar por 2**d

        # Convertimos el entero a cadena binaria, rellenando con ceros hasta la longitud deseada
        new_code = format(new_code_int, '0{}b'.format(longitudes[symbol]))
        codificacion[symbol] = new_code
        
        # Actualizamos para la siguiente iteración
        prev_code_int = new_code_int
        prev_symbol = symbol

    return codificacion

# 2. Codificación de un texto con los códigos de Shannon-Fano

def codificar_shannon_fano(text, codificacion):
    return ''.join([codificacion[symbol] for symbol in text])


# 3. Decodificación de un texto con los códigos de Shannon-Fano
def descodificar_shannon_fano(text, codificacion):
    pass

# ------------------------------------------------
# CODIFICACIÓN HUFFMAN
# ------------------------------------------------

# 1. Códigos de Huffman de un alfabeto.


# 2. Codificación de un texto con los códigos de Huffman


# 3. Decodificación de un texto con los códigos de Huffman


# ------------------------------------------------
# PRUEBAS
# ------------------------------------------------

# 1. Probabilidades del alfabeto.

probabilities = obtain_alphabet_probabilities(TEXT)
probabilities = sort_probabilities(probabilities)

# 2. Codificación de Shannon-Fano y Huffman.
codificacion_sf = shannon_fano(probabilities.copy())

# 3. Entropía
entropy = entropy_worst_case(probabilities)


# 4. Codificación de un texto con los códigos de Shannon-Fano y Huffman.

NEW_TEXT = "BEAWE"
cod_shannon_faro = codificar_shannon_fano(NEW_TEXT, codificacion_sf)

# 5. Decodificación de un texto con los códigos de Shannon-Fano y Huffman.