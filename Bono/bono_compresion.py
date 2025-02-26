import json
import struct
from heapq import heappush, heappop, heapify
from math import log2, ceil

# ------------------------------------------------
# TEXTO Y ALFABETO
# ------------------------------------------------

def obtain_alphabet_probabilities(text):
    alphabet = {}
    for char in text:
        alphabet[char] = alphabet.get(char, 0) + 1
    return {char: count / len(text) for char, count in alphabet.items()}

def sort_probabilities(probabilities):
    return sorted(probabilities.items(), key=lambda item: -item[1])

# ------------------------------------------------
#  HUFFMAN
# ------------------------------------------------

def get_huffman_encoding(probabilities):
    return huffman(get_huffman_tree(probabilities))

def get_huffman_tree(probabilities):
    heap = [(prob, symbol, None, None) for symbol, prob in probabilities]
    heapify(heap)
    while len(heap) > 1:
        prob1, symbol1, left1, right1 = heappop(heap)
        prob2, symbol2, left2, right2 = heappop(heap)
        new_node = (prob1 + prob2, symbol1 + symbol2, (prob1, symbol1, left1, right1), (prob2, symbol2, left2, right2))
        heappush(heap, new_node)
    return heap[0]

def huffman(huffman_tree):
    codes = {}
    def build_codes(node, code=''):
        if node[2] is None and node[3] is None:
            codes[node[1]] = code
        else:
            build_codes(node[2], code + '1')
            build_codes(node[3], code + '0')
    build_codes(huffman_tree)
    return codes

# ------------------------------------------------
# COMPRESIÓN
# ------------------------------------------------

def compress_text(input_file, output_file):
    try:
        
        print("\nIniciando compresión...")
        print(f"Archivo de entrada: {input_file}")

        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read().strip()
        probabilities = sort_probabilities(obtain_alphabet_probabilities(text))
        codes = get_huffman_encoding(probabilities)

        print("\nCodigos Huffman:")
        for symbol, code in codes.items():
            print(f"'{symbol}': {code}")

        compressed_text = ''.join([codes[symbol] for symbol in text])
        padding = (8 - len(compressed_text) % 8) % 8
        compressed_text += '0' * padding
        byte_array = bytearray(int(compressed_text[i:i+8], 2) for i in range(0, len(compressed_text), 8))

        print("\nCompresión:")
        print(f"Texto original: {text}")
        print(f"Texto comprimido: {compressed_text}")
        print(f"Bytes: {byte_array}")


        with open(output_file, 'wb') as file:
            file.write(struct.pack('B', padding))
            file.write(json.dumps(codes).encode('utf-8'))
            file.write(b'\n')
            file.write(byte_array)
        print(f"\nCompresión exitosa. Archivo generado: {output_file}\n")
    except Exception as e:
        print(f"Error en compresión: {e}")

# ------------------------------------------------
# EJECUCIÓN PRINCIPAL
# ------------------------------------------------

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("\nUso del programa:")
        print("  python bono_compresion.py <archivo_entrada> <archivo_salida>")
        print("\nEjemplo:")
        print("  python bono_compresion.py input.txt compressed.bin")
        print("\nEste programa comprime un archivo de texto utilizando el algoritmo de Huffman y guarda el resultado en un archivo binario.")
    else:
        _, input_file, output_file = sys.argv
        compress_text(input_file, output_file)

