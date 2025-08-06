
def factorial(n):
  if n == 0: return 1

  return n * factorial(n - 1)

def permutacion(S):
  for i in range(0, factorial(len(S))):
    for j in range(len(S)):
      print(S[j], end="")
    S[i % len(S)], S[(i + 1) % len(S)] = S[(i + 1) % len(S)], S[i % len(S)]
    print('')

if __name__ == "__main__":
  S = [1, 2, 3]
  permutacion(S)
