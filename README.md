# **Tarea 4**

Este repositorio contiene la implementación de los algoritmos **Shannon-Fano** y **Huffman** para comprimir un texto dado.

## **Autores**

- Vargas Ulloa, Daniel Felipe - d.vargasu@uniandes.edu.co
- Bobadilla Suarez, Santiago - s.bobadilla@uniandes.edu.co
- Ariza Lopez, Lina Marcela - l.arizal@uniandes.edu.co

---

## **Descripción del Problema**

Dado un texto, calcular códigos de Shannon-Fano y Huffman que permitan comprimir el texto dado. Para los dos programas, se debe informar la codificación, el número de bits esperado, la entropía en el peor de los casos y el número total de bits que se necesitarían para guardar el texto dado.

**Nota:** Todos los programas realizados deben poder funcionar a partir de un archivo dado por el usuario. Los programas no pueden hacer ninguna suposición acerca del sistema operativo o del sistema de archivos del usuario. El archivo de entrada debe ser un archivo de texto que en una o más lineas contenga el mensaje a comprimir.

**Bono:** Implementar un programa que comprima textos y un segundo programa que descomprima textos comprimidos, utilizando alguno de los dos esquemas de códigos implementados. Se debe indicar cómo se guarda la información en el archivo comprimido, de modo que sea posible descomprimir.

## **Estructura del Problema**

El repositorio contiene los siguientes archivos:

1. **Algoritmos de Solución:**

   - `Codificar.py`: Implementa el algoritmo de los algoritmos de Shannon-Fano y Huffman que permitan comprimir el texto dado y calcular la entropía, el número de bits esperado y el número total de bits que se necesitarían para guardar el texto dado.
   - `huffman_tree.png`: Arbol que muestra como se construyo la codificación de Huffman, este se genera automáticamente al correr el programa `codificar.py`.

2. **Archivos de Entrada y Salida:**
   - `input.txt`: Contiene el texto que se va a comprimir.
   - `output.txt`: Contiene el texto orgininal, las codificaciones para cada uno de los algoritmos, la entropía y número promedio de bits necesarios para guardar el texto con Shannon-Fano y Huffman, y el número total de bits necesarios para guardar el texto con Shannon-Fano y Huffman.

---

## **Formato de los Archivos**

### **Archivo de Entrada (`input.txt`)**

El archivo de entrada debe seguir este formato:

- El archivo de entrada debe ser un archivo de texto que en una o más lineas contenga el mensaje a comprimir.
  **Ejemplo de archivo de entrada:**
  ```
  According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.
  ```

### **Archivo de Salida (`output.txt`)**

El archivo de salida muestra:

- Texto a codificar
- La codificación de Shannon-Fano
- La codificación de Huffman
- Entropía
- El número promedio de bits necesarios para guardar el texto con Shannon-Fano
- El número promedio de bits necesarios para guardar el texto con Huffman
- El número total de bits necesarios para guardar el texto con Shannon-Fano
- El número total de bits necesarios para guardar el texto con Huffman

**Ejemplo de archivo de salida:**

```
Texto a codificar:
According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.

La codificación de Shannon-Fano es:
' ': 000
'e': 0010
'o': 0011
'a': 0100
't': 0101
's': 01100
'i': 01101
'l': 01110
'n': 01111
'b': 10000
'f': 100010
'h': 100011
'r': 100100
'w': 100101
'c': 100110
'd': 100111
'u': 101000
'y': 101001
'g': 101010
',': 1010110
'.': 1010111
'm': 1011000
'k': 1011001
''': 10110100
'A': 10110101
'I': 10110110
'T': 10110111
'p': 10111000
'v': 10111001

La codificación de Huffman es:
' ': 11
'i': 1011
'l': 1010
'w': 10011
'f': 10010
'h': 10001
'm': 100001
''': 10000011
'A': 10000010
'I': 10000001
'T': 10000000
's': 0111
'a': 0110
'b': 01011
'g': 010101
'k': 0101001
'p': 01010001
'v': 01010000
't': 0100
'o': 0011
'c': 001011
'd': 001010
'u': 001001
'y': 001000
'e': 0001
'n': 00001
',': 0000011
'.': 0000010
'r': 000000

Para el texto dado:
  - La entropía en el peor de los casos es: 4.86 bits.
  - El número promedio de bits necesarios usando la codificacón de Shannon-Fano es: 4.70 bits.
  - El número promedio de bits necesarios usando la codificacón de Huffman es: 4.25 bits.

  - El número total de bits necesarios para guardar el texto con Shannon-Fano es: 1137 bits.
  - El número total de bits necesarios para guardar el texto con Huffman es: 1029 bits.

La codificación de Huffman es más eficiente que la de Shannon-Fano en este caso.
```

---

### **Comando de Ejecución**

Despues de ubicarse en la raiz del proyecto y haber creado el archivo `input.txt` con el texto a codificar, ejecute el siguiente comando:

```bash
python codificar.py
```

---

## **BONO**

El bono se encuentra en la carpeta **\Bono** y contiene los siguientes archivos:

- **bono_compresion.py**: Archivo encargado de leer el texto que se desea comprimir, calculas los códigos de Huffman y comprimir el archivo con dicha configuración en formato .bin.
- **bono_descompresion.py**: Archivo que lee el .bin y descomprime el texto al original.
- **compressed.bin**: Guarda (i) los códigos de Huffman y (ii) el texto comprimido.
- **input.txt**: Contiene el texto original que deseamos comprimir.
- **output.txt**: Contiene el texto descomprimido. En escencia debe ser igual al original.

Durante la ejecución de ambos **.py** se observa el proceso.

### **Ejemplo de entrada (`input.txt`)**

```
Me gusta jugar futbol Sala
```

### **Comando de Ejecución - Comprimir**

Despues de ubicarse en la carpeta **\Bono** y haber creado el archivo `input.txt` con el texto a codificar, ejecute el siguiente comando:

```bash
python bono_compresion.py input.txt compressed.bin
```

### **Comando de Ejecución - Descomprimir**

```bash
python bono_descompresion.py compressed.bin output.txt
```

### **Salida (`output.txt`)**

```
Me gusta jugar futbol Sala
```

### Estrategia de Solución

1. **Entrada**: El archivo input.txt contiene el texto que se desea códificar. Puede ser de la longitud deseada por el usuario.

2. **Algoritmos Implementados**
   Las codificaciones de Shannon-Fano y Huffman son métodos de compresión que asignan códigos binarios a símbolos basándose en su frecuencia de aparición. Ambos métodos buscan codificar el archivo de entrada, pero Huffman generalmente logra una compresión más óptima al construir el árbol de tal manera que los símbolos más frecuentes tengan códigos más cortos.

   **Shannon-Faro**: Shannon-Fano calcula las longitudes de los códigos usando el logaritmo de las probabilidades y asigna códigos secuencialmente, garantizando que sean únicamente decodificables.

   **Huffman**:Huffman construye un árbol binario bottom-up, donde los símbolos menos frecuentes se colocan más profundos en el árbol, y los códigos se generan recorriendo el árbol (0 para ramas derechas, 1 para izquierdas).

3. **Salida**: El archivo output.txt muestra los resultados ya descritos.

---

## **Instalación/Configuración**

### **Requisitos**

Este proyecto requiere Python 3 y las siguientes librerias:

- **os, heapq, math, y struct**: Para manejar archivos y calculos sencillos. Esta librerias vienen incluidas con Python 3.
- **graphviz**: Para la visualización del arbol de Huffman.


### **Instalación en Windows**

1. **Instalar Python 3**:
   - Dirigase a la página oficial de Python [python.org](https://www.python.org/downloads/) y descargue la última versión de Python 3.
   - Durante la instalación, asegúrese de seleccionar la opción "Add Python to PATH" y "Install PIP".
2. **Instalar dependencias**:
   - Abra una terminal (símbolo del sistema o PowerShell) y navegue a la carpeta del proyecto.
   - Ejecute el siguiente comando para instalar las dependencias necesarias:
     ```bash
     pip install graphviz
     ```

### **Instalación en Ubuntu**

1. **Instalar Python 3**:

   - En la terminal, ejecute los siguientes comandos:
     ```bash
     sudo apt update
     sudo apt install python3
     ```

2. **Instalar dependencias**:
   - Una vez instalado Python, instale las librerias necesarias con:
     ```bash
     pip3 install graphviz
     ```
   - Si no se encontró el comando pip, debe instalarlo antes usando
     ```bash
     sudo apt-get install python3-pip
     ```

## **Ejecución del Programa**

1. Asegúrese de que el archivo `input.txt` esté ubicado en la misma carpeta principal si se desea ejecutar el archivo ```cofificar.py```.

2. Asumiendo que se encuentra en la raiz del proyecto, para ejecutar ambos algoritmos al tiempo, ejecute:

   ```bash
   python codificar.py
   ```

3. Con el fin de correr el BONO, entre al directorio \Bono y asegúrese de que el archivo `input.txt` esté ubicado en la misma carpeta:

   ```bash
   python bono_compresion.py input.txt compressed.bin
   python bono_descompresion.py compressed.bin output.txt

   ```

---
