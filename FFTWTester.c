#include<stdio.h>
#include <fftw3.h>
#include<sys/stat.h>
#include<math.h>
#include "testInput.h"
#define NUM_ELEMENTS 32768 //number of samples
#define fs 8000 //sampling rate

double tempWAV[NUM_ELEMENTS]; //data from WAVto code tool

double fastFourier(); //fft execution
int max(double arr[]); //max amplitude finder
double * fourierABS(fftw_complex arr[]); //absolute value of  fourier output
double * fftShift(double *in); //shifts fourier transform
void cents(double freq);

//compiler instructions
//gcc FFTWTester.c testInput.C testInput.h -o FFTWTester -lfftw3 -lm

int main(){

    double freq = fastFourier();
    printf("%f \n", freq); //output frequency
    cents(freq);
    double test;
    scanf("%f", test); //used to pause output
    return 0;
}

double fastFourier(){
    FILE *fp, *op;
    int size = NUM_ELEMENTS;
    //creates imaginary & real arrays for input data and output data
    fftw_complex *in, *out; //*in, *out
    fftw_plan p; //plan variable created for fft
    in = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * size); //allocating space for arrays
    out = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * size);
    for(int j = 0; j < size; j++){ //filling in array with data
        in[j][0] = tempWAV[j];
    }
    p = fftw_plan_dft_1d(size, in, out, FFTW_FORWARD, FFTW_ESTIMATE); //assign plan to plan variable
    fftw_execute(p); //compute fft
    fp = fopen("testInput.dat", "w"); //open file stream
    for( int k = 0; k < size; k++){
        fprintf(fp, "%f " , in[k][0]); //write input data to see if it matches with input.dat
    }
    op = fopen("testOutput.dat", "w");
    for(int i = 0; i < size; i++){
         fprintf(op, "%f ", out[i][0]); //open output data for graphing with matlab
     }
    out[0][0] = 0;
    double *mag = fourierABS(out);
    fclose(op); //close io streams
    fftw_destroy_plan(p); //destroy plan
    fftw_free(in); fftw_free(out); //free array memory

    return max(mag)*fs/NUM_ELEMENTS;
}

int max(double *arr){
    double max = 0;
    int index = 0;
    for(int i = 0; i < NUM_ELEMENTS; i++){
        if(arr[i] > max){
            max = arr[i];
            index = i;
        }
    }
    return index; //index * fs/NUM_ELEMENTS
}


void fourierABS(fftw_complex arr[], double *out){
	for(int i = 0; i < NUM_ELEMENTS; i++){
		out[i] = sqrt( arr[i][0]*arr[i][0] + arr[i][1]*arr[i][1] );
    }
	return out;
}

double * fftShift(double *in){
    double *rH, *lH;
    lH = in; rH = in + NUM_ELEMENTS/2;
    for (int i = 0; i < NUM_ELEMENTS/2; i++){
        in[i] = rH[i];
    }
    for(int i = NUM_ELEMENTS/2; i < NUM_ELEMENTS; i++){
        in[i] = lH[i];
    }
    return in;
}

void cents(double freq){
    double Fd;
    printf("%s", "Please input desired frequency \n");
    scanf("%f", Fd); //take in freq
    printf("%f \n", Fd); //reprint freq
    double c = 1200*log(freq/Fd)/log(2);
    printf("Note is %f away from the desired note", c);

}
