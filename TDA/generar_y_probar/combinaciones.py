
def combinaciones(S):
  for i in range(0, 2 ** len(S)):
    for j in range(0, len(S)):
      if ((i >> j) & 1) > 0:
        print(S[j], end="")
    print('')

if __name__ == "__main__":
  S = [1, 2, 3]
  combinaciones(S)
