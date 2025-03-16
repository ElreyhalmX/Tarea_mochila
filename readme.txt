 Problema de la Mochila con Programación Entera

Este repositorio contiene una solución al clásico Problema de la Mochila (Knapsack Problem) utilizando Programación Entera y Programación Orientada a Objetos (POO) en Python. La solución implementa un algoritmo de búsqueda exhaustiva (backtracking) para determinar la combinación de objetos que maximiza el valor total sin exceder la capacidad máxima de la mochila.

 Contenido del Repositorio

- README.md: Este archivo que explica el funcionamiento y uso del proyecto.
- mochila.py: Archivo que contiene la implementación de las clases `Objeto` y `Mochila`, y la función `resolver_mochila`.

 Descripción del Problema

El objetivo es seleccionar una combinación de objetos, cada uno con un peso y un valor, de modo que:
- El peso total de los objetos seleccionados no exceda la capacidad máxima de la mochila.
- El valor total de los objetos seleccionados sea el máximo posible.

Cada objeto se considera de forma binaria: se puede incluir (1) o no incluir (0) en la mochila.

 Funcionamiento del Programa

 Clases y Funciones

 Clase `Objeto`
- Atributos: 
  - `peso`: Número entero que representa el peso del objeto.
  - `valor`: Número entero que representa el valor del objeto.
- Método `__str__`: Permite imprimir el objeto en un formato legible, por ejemplo: `"Objeto(peso=3, valor=4)"`.

Clase `Mochila`
- Atributos:
  - `capacidad_maxima`: Capacidad máxima de la mochila (entero).
  - `objetos`: Lista de objetos (`Objeto`).
- Método `resolver`:
  - Implementa un algoritmo de backtracking para explorar todas las combinaciones posibles de objetos.
  - Evalúa cada combinación y, si el peso acumulado es menor o igual a la capacidad máxima, se considera para maximizar el valor total.
  - Guarda y retorna la mejor combinación encontrada (mayor valor total) junto con el valor acumulado.

 Función `resolver_mochila`
- Entrada:
  - `capacidad_maxima`: Capacidad máxima de la mochila.
  - `objetos`: Lista de instancias de la clase `Objeto`.
- Proceso:
  - Crea una instancia de `Mochila` con los datos de entrada.
  - Llama al método `resolver` para obtener la mejor combinación de objetos.
  - Calcula el peso total y muestra en consola los objetos seleccionados, el valor total y el peso total.
- Salida:
  - Imprime en la consola la solución óptima.

 Ejemplo de Uso

Para probar el programa, se utiliza el siguiente conjunto de datos de ejemplo:

python
capacidad_maxima = 10
objetos = [
    Objeto(peso=5, valor=10),
    Objeto(peso=4, valor=40),
    Objeto(peso=6, valor=30),
    Objeto(peso=3, valor=50)
]

resolver_mochila(capacidad_maxima, objetos)
