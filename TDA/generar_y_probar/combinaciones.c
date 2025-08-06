#include <stdio.h>

void combinaciones(int* S, int n) {
  for (int i = 0; i < (1 << n); i++) {
    for (int j = 0; j < n; j++) {
      if (((i >> j) & 1) > 0) {
        printf("%d ", S[j]);
      }
    }
    printf("\n");
  }
}

int main() {
  int S[3] = {1, 2, 3};
  combinaciones(S, 3);
  return 0;
}
