#include <stdio.h>

typedef void (*mostrar_elemento_t)(void*);

void combinaciones(void** S, int n, mostrar_elemento_t mostrar) {
  for (int i = 0; i < (1 << n); i++) {
    for (int j = 0; j < n; j++) {
      if (((i >> j) & 1) > 0) {
        mostrar(S[j]);
      }
    }
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
  
  combinaciones(elementos, 3, mostrar_int);
  return 0;
}
