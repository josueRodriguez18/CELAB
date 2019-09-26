#include<stdio.h>
#include<unistd.h>
#include <fftw3.h>
#include<sys/stat.h>
#include<math.h>
#include "testInput.h"
#define NUM_ELEMENTS 32768 

double tempWAV[NUM_ELEMENTS]; //data from WAVto code tool

void fastFourier(); //fft execution
int max(double arr[]); //max amplitude finder
double * fourierABS(fftw_complex arr[]); //absolute value of  fourier output

//compiler instructions
//gcc FFTWTester.c testInput.C testInput.h -o FFTWTester -lfftw3 -lm

int main(){
    char k[2];
    fgets(k, 2, stdin); //pause to see results
    fastFourier();
    return 0;
}

void fastFourier(){
    FILE *fp, *op;
    int size = NUM_ELEMENTS;
    //creates imaginary & real arrays for input data and output data
    fftw_complex *in, *out; //*in, *out
    fftw_plan p; //plan variable created for fft
    in = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * size); //allocating space for arrays
    out = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * size);
    for(int j = 0; j < size; j++){ //filling in array with data
        in[0][j] = tempWAV[j];
    }
    p = fftw_plan_dft_1d(size, in, out, FFTW_FORWARD, FFTW_ESTIMATE); //assign plan to plan variable
    fftw_execute(p); //compute fft
    fp = fopen("testInput.dat", "w"); //open file stream
    for( int k = 0; k < size; k++){
        fprintf(fp, "%c %f", ' ', in[k]); //write input data to see if it matches with input.dat
    }
    op = fopen("testOutput.dat", "w");
    for(int i = 0; i < size; i++){
         fprintf(op, "%c %f", ' ', out[i]); //open output data for graphing with matlab
     }
    fclose(op); //close io streams
    fftw_destroy_plan(p); //destroy plan
    fftw_free(in); fftw_free(out); //free array memory
}

int max(double arr[]){
    double max = 0;
    int index = 0;
    double pos[NUM_ELEMENTS];
    for(int i = 0; i < NUM_ELEMENTS; i++){
        pos[i] = fabs(arr[i]);
    }
    for(int i = 0; i < NUM_ELEMENTS; i++){
        if(arr[i] > max){
            max = arr[i];
            index = i;
        }
    }
    return index;
}


double * fourierABS(fftw_complex arr[]){
	static double out[NUM_ELEMENTS];
	return out;
}
