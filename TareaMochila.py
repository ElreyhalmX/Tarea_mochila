class Objeto:
    def __init__(self, peso: int, valor: int):
        self.peso = peso
        self.valor = valor

    def __str__(self):
        return f"Objeto(peso={self.peso}, valor={self.valor})"


class Mochila:
    def __init__(self, capacidad_maxima: int, objetos: list):
        self.capacidad_maxima = capacidad_maxima
        self.objetos = objetos

    def resolver(self):
        """
        Resuelve el problema de la mochila utilizando backtracking.
        Retorna una tupla (mejor_combinacion, valor_total) donde:
          - mejor_combinacion: lista de objetos seleccionados.
          - valor_total: suma de los valores de los objetos seleccionados.
        """
        mejor_solucion = {"valor": 0, "combinacion": []}

        def backtrack(indice, peso_actual, valor_actual, combinacion):
            # Caso base: se han considerado todos los objetos
            if indice == len(self.objetos):
                if valor_actual > mejor_solucion["valor"]:
                    mejor_solucion["valor"] = valor_actual
                    mejor_solucion["combinacion"] = combinacion.copy()
                return

            # Decisión de incluir el objeto actual (si cabe en la mochila)
            objeto_actual = self.objetos[indice]
            if peso_actual + objeto_actual.peso <= self.capacidad_maxima:
                combinacion.append(objeto_actual)
                backtrack(indice + 1,
                          peso_actual + objeto_actual.peso,
                          valor_actual + objeto_actual.valor,
                          combinacion)
                combinacion.pop()  # retroceder

            # Decisión de no incluir el objeto actual
            backtrack(indice + 1, peso_actual, valor_actual, combinacion)

        backtrack(0, 0, 0, [])
        return mejor_solucion["combinacion"], mejor_solucion["valor"]


def resolver_mochila(capacidad_maxima: int, objetos: list):
    """
    Función que recibe la capacidad máxima y una lista de objetos,
    resuelve el problema de la mochila y muestra la solución.
    """
    mochila = Mochila(capacidad_maxima, objetos)
    seleccionados, valor_total = mochila.resolver()
    peso_total = sum(obj.peso for obj in seleccionados)

    print("Objetos seleccionados:")
    for obj in seleccionados:
        print(obj)
    print("Valor total:", valor_total)
    print("Peso total:", peso_total)


# Ejemplo de uso:
if __name__ == "__main__":
    # Datos de entrada
    capacidad_maxima = 10
    objetos = [
        Objeto(peso=5, valor=10),
        Objeto(peso=4, valor=40),
        Objeto(peso=6, valor=30),
        Objeto(peso=3, valor=50)
    ]

    resolver_mochila(capacidad_maxima, objetos)
