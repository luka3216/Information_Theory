#include <stdio.h>

int main(int argc, char** argv) {
  int N, M;
  int benches[100];
  scanf("%d %d", &N, &M);
  for (int i = 0; i < N; i++) {
    scanf("%d", benches + i);
  }
  int min = benches[0], max = benches[0];
  for (int i = 1; i < N; i++) {
    if (benches[i] > max) max = benches[i];
    if (benches[i] < min) min = benches[i];
  }
  int sum = 0;
  int sumsum = 0;
  for (int i = 0; i < N; i++) {
    sum += max - benches[i];
    sumsum += benches[i];
  }
  if (sum >= M) {
    min = max;
  } else {
    min = (sumsum + M) / N;
  }
  if (N == 1) {
    printf("%d %d", benches[0] + M, benches[0] + M);
  } else {
    printf("%d %d", min, max + M);
  }
}