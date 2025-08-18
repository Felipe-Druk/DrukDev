def mostrar_n_tuplas(elementos):
  cantidad_elementos = len(elementos)
  contador = 0 
  limite = 2**cantidad_elementos
  while contador < limite:
        for i in range(0, cantidad_elementos):
            if ((contador >> i) & 1):
                print(elementos[i], end=" ")
        print('')
        contador = contador +1
  

if __name__ == "__main__":
    A = ["hacha","linterna", "taza", "brujula"]
    mostrar_n_tuplas(A)

