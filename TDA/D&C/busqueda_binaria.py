

def busqueda_binaria(array, objetivo):
    izquierda = 0
    derecha = len(array) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if array[medio] == objetivo:
            return medio
        elif array[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print(f"{objetivo} no esta en el arreglo")
    return None





if __name__ == "__main__":
  S = [1, 2, 3]
  busqueda_binaria(S, 3)
  busqueda_binaria(S, 4)