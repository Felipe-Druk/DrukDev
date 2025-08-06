
def n_tuplas(n, elementos):
  for i in range (0, len(elementos)):
    if ((n >> i) & 1):
      print(S[j], end="")
    print('')

if __name__ == "__main__":
  S = [1, 2, 3]
  combinaciones(S)
