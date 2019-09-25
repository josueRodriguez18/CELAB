#include<stdio.h>
#include<unistd.h>
#include <fftw3.h>
#include<sys/stat.h>
#include "testInput.h"
#define NUM_ELEMENTS 32768 

unsigned char tempWAV[NUM_ELEMENTS];

void fastFourier(){
    FILE *fp, *op;
    int size = NUM_ELEMENTS;
    //creates imaginary & real arrays for input data and output data
    fftw_complex *in, *out; //*in, *out
    fftw_plan p;
    in = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * size);
    out = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * size);
    for(int j = 0; j < size; j++){
        in[0][j] = tempWAV[j];
    }
    p = fftw_plan_dft_1d(size, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_execute(p);   
    fp = fopen("testInput.dat", "w");
    for( int k = 0; k < size; k++){
        fprintf(fp, "%f %f", k, in[0][k]);
    }
    op = fopen("testOutput.dat", "w");
    for(int i = 0; i < size; i++){
         fprintf(op, "%f %f", i, out[0][i]);
     }
    fclose(op);
    fftw_destroy_plan(p);
    fftw_free(in); fftw_free(out);
}

//gcc FFTWTester.c -o test -L/usr/local/lib -lfftw3

int main(){
    char k[2];
    fgets(k, 2, stdin);
    fastFourier();
    return 0;
}



