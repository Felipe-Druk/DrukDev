#include <stdio.h>

typedef void (*mostrar_elemento_t)(void*);

int factorial(int n) {
  if (n == 0) return 1;
  return n * factorial(n - 1);
}

void swap(void** a, void** b) {
  void* temp = *a;
  *a = *b;
  *b = temp;
}

void permutacion(void** S, int n, mostrar_elemento_t mostrar) {
  for (int i = 0; i < factorial(n); i++) {
    for (int j = 0; j < n; j++) {
      mostrar(S[j]);
    }
    swap(&S[i % n], &S[(i + 1) % n]);
    printf("\n");
  }
}

void mostrar_int(void* a) {
  printf("%d ", *(int*)a);
}

int main() {
  int S[3] = {1, 2, 3};

  void* elementos[3];
  for (int i = 0; i < 3; i++) {
    elementos[i] = &S[i];
  }

  permutacion(elementos, 3, mostrar_int);
  return 0;
}
