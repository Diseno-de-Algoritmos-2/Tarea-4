import json
import struct

# ------------------------------------------------
# DESCOMPRESIÓN
# ------------------------------------------------

def decompress_text(input_file, output_file):
    try:
        print("\nIniciando descompresión...")
        print(f"Archivo de entrada: {input_file}")
        print(f"Archivo de salida: {output_file}")
        
        with open(input_file, 'rb') as file:
            padding = struct.unpack('B', file.read(1))[0]
            codes = json.loads(file.readline().decode('utf-8'))
            compressed_data = file.read()
        
        print("\nCodigos Huffman:")
        for symbol, code in codes.items():
            print(f"'{symbol}': {code}")
        
        print("\nDescompresión finalizada.")
        print()
        print(f"Bytes: {compressed_data}")
        print()

        bit_string = ''
        for byte in compressed_data:
            bits = format(byte, '08b')
            bit_string += bits

        if padding > 0:
            bit_string = bit_string[:-padding]


        print(f"Texto comprimido: {bit_string}")
        print()

        reverse_codes = {v: k for k, v in codes.items()}
        decoded_text = ""
        temp_code = ""
        for bit in bit_string:
            temp_code += bit
            if temp_code in reverse_codes:
                decoded_text += reverse_codes[temp_code]
                temp_code = ""
        
        print(f"Texto descomprimido: {decoded_text}")
        print()

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decoded_text)
        
        print(f"Descompresión exitosa. Archivo generado: {output_file}\n")
    except Exception as e:
        print(f"Error en descompresión: {e}")

# ------------------------------------------------
# EJECUCIÓN PRINCIPAL
# ------------------------------------------------

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("\nUso del programa:")
        print("  python bono_descompresion.py <archivo_entrada> <archivo_salida>")
        print("\nEjemplo:")
        print("  python bono_descompresion.py compressed.bin output.txt")
        print("\nEste programa descomprime un archivo binario generado con Huffman y lo guarda en un archivo de texto.")
    else:
        _, input_file, output_file = sys.argv
        decompress_text(input_file, output_file)
