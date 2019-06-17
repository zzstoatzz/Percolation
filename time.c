#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define VACANT 0
#define OCCUPIED 1
#define BURNING 2
#define WIDTH 12
#define MAXRUNS 1000000
#define PRINTFREQ MAXRUNS/10

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


    srand(time(NULL));
    int i, j, k, step, a, b, x, y, burnable, burned, occupied;
    int L = WIDTH;
    int N = L*L;
    int dir[8] = { -1*L-1 ,-1*1 , L-1 , L , -1*L , -1*L+1 , 1 , L+1};
    int forest[N];
    float sum;
    long runs;

    for(sum = runs = 0; runs < MAXRUNS; ++runs){
        if (runs%(PRINTFREQ) == 0 && runs>0) {
            printf("...%d%% complete...\n", (int)(100*runs/MAXRUNS));
        }

        // initialize forest
        occupied = 0;
        burnable = 1;
        for (i = 0; i < N; ++i) {
            a = rand() % 100;
            if (a > 50) {
                b = OCCUPIED;
                occupied += 1;
            }
            else {
                b = VACANT;
            }

            forest[i] = b;

        }

        // start fire in first row
        burned = 0;
        for (i = 0; i < L; ++i) {
            if (forest[i] == OCCUPIED) {
                forest[i] = BURNING;
                burned += 1;
            }
        }

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
                            burned += 1;
                            burnable = 1;
                        }
                    }
                }

            }
            
        }

        sum += (float) burned/occupied;
    }

    printf("DONE \n\n runs: %d \naverage frac forest burned: %f\n\n", MAXRUNS , sum/MAXRUNS);

}
