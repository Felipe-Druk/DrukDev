#include <stdio.h>

int factorial(int n) {
  if (n == 0) return 1;

  return n * factorial(n - 1);
}

void swap(int* a, int* b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void permutacion(int* S, int n) {
  for (int i = 0; i < factorial(n); i++) {
    for (int j = 0; j < n; j++) {
       printf("%d ", *(S + j));
    }
    swap(S + (i % n), S + ((i + 1) % n));
    printf("\n");
  }
}

int main() {
  int S[3] = {1, 2, 3};
  permutacion(S, 3);
  return 0;
}
