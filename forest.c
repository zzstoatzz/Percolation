#include <stdio.h>
#include <stdlib.h>
#define VACANT 0
#define OCCUPIED 1
#define BURNING 2
#define WIDTH 12

void bc(int *x, int *y, int i) {
    if ((i+1)%WIDTH == 0) {
        *x = 0;
        *y = 5;
    }
    else if ((i+1)%WIDTH == 1) {
        *x = 3;
        *y = 8;
    }
    else {
        *x = 0;
        *y = 8;
    }
}


int main() {

    FILE *fptr = fopen("shabba", "w");
    if (fptr == NULL) {
        printf("Couldn't open file");
        return 0;
    }

    srand(time(NULL));
    int i, j, k, step, a, b, x, y, sum, burnable;
    int L = WIDTH;
    int N = L*L;
    int dir[8] = { -1*L-1 ,-1*1 , L-1 , L , -1*L , -1*L+1 , 1 , L+1};
    int forest[N];


    // initialize forest
    printf("\nThis is the initial forest \n\n 0 : No Tree \n 1 : Tree \n 2 : Burning Tree \n\n");
    for (i = 0; i < N; ++i) {
        a = rand() % 100;
        if (a > 50) {
            b = OCCUPIED;
        }
        else {
            b = VACANT;
        }

        forest[i] = b;

        printf("%d ", b);
        if ((i+1)%L == 0){
            printf("\n");
        }
    }

    printf("\nPress Enter to light fire in the North...\n ");
    getchar();

    // start fire in first row
    for (i = 0; i < L; ++i) {
        if (forest[i] == OCCUPIED) {
            forest[i] = BURNING;
        }
    }
    // show lit forest
    for (i=0; i < N; ++i) {
        printf("%d ", forest[i]);
        if ((i+1)%L == 0) {
            printf("\n");
        }
    }


    printf("\nPress Enter to see how the forest responds...\n ");
    getchar();

    // for all potential tree spots
    while(burnable) {
        burnable = 0;
        for (i=0; i < N; ++i) {
            // BCs -- only valid directions (non periodic system)
            bc(&x, &y, i);
            // if there's a burning tree
            if (forest[i] == BURNING) {
                // check all valid directions around that tree
                for (j = x; j < y; ++j) {
                    step = dir[j];
                    k = i + step;
                    // which are within the bounds of the system && 
                    // if there exists adjacent tree then it shall burn
                    if (k >= 0 && k < N && forest[k] == OCCUPIED) {
                        forest[k] = BURNING;
                        burnable = 1;
                    }
                }
            }
        }
        if (burnable) {
            for (i=0; i < N; ++i) {
                printf("%d ", forest[i]);
                if ((i+1)%L == 0) {
                    printf("\n");
                }
            }
            printf("\nPress Enter to increment time\n");
            getchar();
        }
        else {
            printf("Forest is all burnt out :(\nGoodbye\n\n");
            return 0;
        }
        
    }
 
}
