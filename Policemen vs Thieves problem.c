//Policemen VS Thieves Problem Implementation

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <limits.h>
#define MAX 100
int catchThieves(char grid[MAX][MAX], int n, int k, int policeCount) {
 int caughtCount = 0;
 for (int i = 0; i < n; i++) {
 for (int j = 0; j < n; j++) {
 if (grid[i][j] == 'P') {
 int minDistance = INT_MAX;
 for (int x = i - k; x <= i + k; x++) {
 for (int y = j - k; y <= j + k; y++) {
 if (x >= 0 && x < n && y >= 0 && y < n && grid[x][y] == 'T') {
 int distance = abs(i - x) + abs(j - y);
 if (distance <= k && distance < minDistance) {
 minDistance = distance;
 grid[x][y] = 'C'; 
 caughtCount++;
 policeCount--;
 break;
   }
 }
}
 if (policeCount == 0) {
 return caughtCount;
           }
         }
       }
     }
   }
 return caughtCount;
}

int main() {
 int n, k, policeCount;
 printf("Enter grid size, maximum distance (k), and number of policemen: ");
 scanf("%d %d %d", &n, &k, &policeCount);
 char grid[MAX][MAX];
 printf("Enter the grid (use 'P' for policemen, 'T' for thieves):\n");
 for (int i = 0; i < n; i++) {
 scanf("%s", grid[i]);
 }
 int caughtCount = catchThieves(grid, n, k, policeCount);
 printf("Maximum number of thieves caught: %d\n", caughtCount);
 return 0;
}
