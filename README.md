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

   - `Codificar.py`: Implementa el algoritmo de los algoritmos de Shannon-Fano y Huffman que permitan comprimir el texto dado.
   - `huffman_tree.png`: Arbol que muestra como se construyo la codificación de Huffman.

2. **Archivos de Entrada y Salida:**
   - `input.txt`: Contiene el texto que se va a comprimir.
   - `output.txt`: Contiene el texto orgininal, las condificaciones para cada uno de los algoritmos, la entropía y número promedio de bits.

---

## **Formato de los Archivos**

### **Archivo de Entrada (`input.txt`)**

El archivo de entrada debe seguir este formato:

- **N Líneas:** Texto que se va a codificar.
  **Ejemplo de archivo de entrada:**
  ```
  According to all known laws of aviation, there is no way a bee should be able to flyyyyyyyyyyyyyyyyyy
  ```

### **Archivo de Salida (`output.txt`)**

El archivo de salida muestra:

- Texto a codificar
- La codificación de Shannon-Fano
- La codificación de Huffman
- Entropía
- El número promedio de bits

**Ejemplo de archivo de salida:**

```
Texto a codificar:
According to all known laws of aviation, there is no way a bee should be able to flyyyyyyyyyyyyyyyyyy

La codificación de Shannon-Fano es:
'y': 000
' ': 001
'o': 0100
'a': 0101
'e': 01100
'l': 01101
'n': 01110
'i': 01111
't': 10000
'b': 100010
's': 100011
'w': 100100
'c': 100101
'd': 100110
'f': 100111
'h': 101000
'r': 101001
',': 1010100
'A': 1010101
'g': 1010110
'k': 1010111
'u': 1011000
'v': 1011001

La codificación de Huffman es:
'y': 11
't': 1011
'n': 1010
'b': 10011
's': 10010
'e': 1000
'l': 0111
'a': 0110
'w': 01011
',': 0101011
'A': 0101010
'c': 010100
'd': 010011
'f': 010010
'g': 0100011
'k': 0100010
'h': 010000
'i': 00111
'r': 001101
'u': 0011001
'v': 0011000
'o': 0010
' ': 000

Para el texto dado:
  - La entropía en el peor de los casos es: 4.52 bits.
  - El número promedio de bits necesarios para guardar el texto con Shannon-Fano es: 4.45 bits.
  - El número promedio de bits necesarios para guardar el texto con Huffman es: 3.96 bits.

  - El número total de bits necesarios para guardar el texto con Shannon-Fano es: 449 bits.
  - El número total de bits necesarios para guardar el texto con Huffman es: 400 bits.

La codificación de Huffman es más eficiente que la de Shannon-Fano en este caso.
```

---

## **Ejemplo de Ejecución**

### **Entrada (`input.txt`)**

```
Hola
```

### **Comando de Ejecución**

```bash
python codificar.py
```

### **Salida (`output.txt`)**

```
Texto a codificar:
Hola

La codificación de Shannon-Fano es:
'H': 00
'a': 01
'l': 10
'o': 11

La codificación de Huffman es:
'H': 11
'a': 10
'l': 01
'o': 00

Para el texto dado:
  - La entropía en el peor de los casos es: 2.00 bits.
  - El número promedio de bits necesarios para guardar el texto con Shannon-Fano es: 2.00 bits.
  - El número promedio de bits necesarios para guardar el texto con Huffman es: 2.00 bits.

  - El número total de bits necesarios para guardar el texto con Shannon-Fano es: 8 bits.
  - El número total de bits necesarios para guardar el texto con Huffman es: 8 bits.

La codificación de Huffman es más eficiente que la de Shannon-Fano en este caso.
```

---

## **BONO**

El bono se encuentra en la carpeta **\Bono** y contiene los siguientes archivos:

- **bono_compresion.py**: Archivo encargado de leer el texto que se desea comprimir, calculas los códigos de Huffman y comprimir el archivo con dicha configuración en .bin.
- **bono_descompresion.py**: Archivo que lee el .bin y descomprime el texto al original.
- **compressed.bin**: Guarda (i) los códigos de Huffman y (ii) el texto comprimido.
- **input.txt**: Contiene el texto original que deseamos comprimir.
- **output.txt**: Contiene el texto descomprimido. En escencia debe ser igual al original.

Durante la ejecución de ambos **.py** se observa el proceso.

### **Entrada (`input.txt`)**

```
Me gusta jugar futbol Sala
```

### **Comando de Ejecución - Comprimir**

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
   Las codificaciones de Shannon-Fano y Huffman son métodos de compresión que asignan códigos binarios a símbolos basándose en su frecuencia de aparición. Ambos métodos buscan minimizar la longitud promedio del código, pero Huffman generalmente logra una compresión más óptima al construir el árbol de manera que los símbolos más frecuentes tengan códigos más cortos.

   **Shannon-Faro**: Shannon-Fano calcula las longitudes de los códigos usando el logaritmo de las probabilidades y asigna códigos secuencialmente, garantizando que sean únicamente decodificables.

   **Huffman**:Huffman construye un árbol binario bottom-up, donde los símbolos menos frecuentes se colocan más profundos en el árbol, y los códigos se generan recorriendo el árbol (0 para ramas derechas, 1 para izquierdas).

3. **Salida**: El archivo output.txt muestra los resultados ya descritos.

---

## **Instalación/Configuración**

### **Requisitos**

Este proyecto requiere Python 3 y las siguientes librerias:

- **os, heapq, math, y struct**: Para manejar archivos y calculos sencillos. Esta librerias vienen incluidas con Python 3.
- **graphviz**: Para la visualización del arbol de Huffman.

  ```bash
  from graphviz import Digraph
  ```

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

1. Asegúrese de que el archivo `input.txt` esté ubicado en la misma carpeta principal.

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
