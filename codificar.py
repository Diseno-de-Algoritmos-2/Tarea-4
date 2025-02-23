

from heapq import heappush, heappop, heapify
from math import log2, ceil
from graphviz import Digraph

# ------------------------------------------------
# TEXTO Y ALFABETO
# ------------------------------------------------

#TEXT = "AABEEWFEBKAEFBKEAFEA"
TEXT = "DVJFVNDFVBKHDSJFVDBHKFJHFLJDKFBVLJDFBVKHF"


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

# 1. Armamos el árbol de Huffman para un alfabeto.
def get_huffman_tree(probabilities):
    
    # Ajustamos la cola de prioridad para que tenga dos espacios y son sus hijos (nodos) binarios.
    heap = [(-prob, symbol, None, None) for prob, symbol in probabilities]
    heapify(heap)
    
    # Construimos el árbol de Huffman.
    root = None         # --> Acá vamos a guardar el árbol.
    while len(heap) > 1:
        
        # Sacamos los dos nodos con menor probabilidad
        prob1, symbol1, left1, right1 = heappop(heap)
        prob2, symbol2, left2, right2 = heappop(heap)
        
        # Creamos el nuevo nodo con la suma de las probabilidades, y sus hijos.
        new_prob = prob1 + prob2
        new_node = (new_prob, symbol1 + symbol2, 
                   (prob1, symbol1, left1, right1),
                   (prob2, symbol2, left2, right2))
        
        heappush(heap, new_node)
        root = new_node

    return root

# 2. Códigos de Huffman leyendo el árbol de Huffman.
def huffman(huffman_tree):    

    # Vamos a recorrer el árbol de manera recursiva para obtener los códigos.
    codes = {}
    def build_codes(node, code=''):

        # Escenario base 1: si el nodo es nulo, salimos de la recursión.
        if node is None:
            return
        
        # Extraemos la información del nodo cuando sí hay.
        _, symbol, left, right = node
        
        # Escenario base 2: Si el nodo es una hoja, guardamos el código, y salimos de la recursión.
        if left is None and right is None:
            codes[symbol] = code
            return
        
        # Si no es hoja, seguimos recorriendo el árbol, dando '0' a la izquierda y '1' a la derecha.
        build_codes(left, code + '1')
        build_codes(right, code + '0')
    
    if huffman_tree:
        build_codes(huffman_tree)
    
    return codes

# 3. Codificación de un texto con los códigos de Huffman
def codificar_huffman(text, codificacion):
    return ''.join([codificacion[symbol] for symbol in text])

# 4. Decodificación de un texto con los códigos de Huffman
def descodificar_huffman(text, codificacion):
    pass

# 5. Gráfica del árbol de Huffman
def plot_huffman_tree(huffman_tree):

    # Creamos un objeto Digraph para graficar el árbol
    dot = Digraph(comment='Huffman Tree')
    dot.attr(rankdir='TB')
    
    # Vamos a mostrar el arbol de Huffman de manera recursiva.
    def add_nodes(node, node_id=''):

        # Escenario base: si el nodo es nulo, salimos de la recursión.
        if node is None:
            return
        
        # Extraemos la información del nodo.
        prob, symbol, left, right = node
        
        # Si es hoja, mostramos solo el símbolo. Sino, mostramos solo la probabilidad.
        if left is None and right is None:
            label = f'{prob:.2f}\n{symbol}'
        else:
            label = f'{prob:.2f}'
            
        # Creamos el nodo en el gráfico.
        dot.node(str(node_id), label)
        
        # Si hay hijos por la rama izquierda, los agregamos.
        if left is not None:
            left_id = f'{node_id}L'
            dot.edge(str(node_id), left_id, '1')
            add_nodes(left, left_id)
        
        # Si hay hijos por la rama derecha, los agregamos.
        if right is not None:
            right_id = f'{node_id}R'
            dot.edge(str(node_id), right_id, '0')
            add_nodes(right, right_id)
    
    # Partimos desde la raíz del árbol.
    add_nodes(huffman_tree, 'root')
    
    # Save and show the graph
    dot.render('huffman_tree', format='png')



# ------------------------------------------------
# PRUEBAS
# ------------------------------------------------

# 1. Probabilidades del alfabeto.

probabilities = obtain_alphabet_probabilities(TEXT)
probabilities = sort_probabilities(probabilities)

# 2. Codificación de Shannon-Fano y Huffman.
codificacion_sf = shannon_fano(probabilities.copy())
print(f"La codificación de Shannon-Fano es: {codificacion_sf}")

huffman_tree = get_huffman_tree(probabilities.copy())
codificacion_huffman = huffman(huffman_tree)
print(f"La codificación de Huffman es: {codificacion_huffman}")

# 3. Entropía
entropy = entropy_worst_case(probabilities)

# 4. Codificación de un texto con los códigos de Shannon-Fano y Huffman.

NEW_TEXT = "BEAWE"
NEW_TEXT = "DVJFV"



cod_shannon_faro = codificar_shannon_fano(NEW_TEXT, codificacion_sf)
cod_huffman = codificar_huffman(NEW_TEXT, codificacion_huffman)

print(f"Para el texto '{NEW_TEXT}', la codificación de Shannon-Fano es: {cod_shannon_faro}")
print(f"Para el texto '{NEW_TEXT}', la codificación de Huffman es: {cod_huffman}")

# 5. Decodificación de un texto con los códigos de Shannon-Fano y Huffman.


# 6. Visualización del árbol de Huffman.
plot_huffman_tree(huffman_tree)