#include<stdio.h>
#include <fftw3.h>
#include<sys/stat.h>

void helpmeout(){
    FILE *fp;
    fp = fopen("ANote.wav", "r");
    fseek(fp, 0, SEEK_END);
    int size = ftell(fp);
    printf("%d", size);
    //creates imaginary & real arrays for input data and output data
    fftw_complex *in, *out;
    fftw_plan p;
    int N = size;
    in = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * N);
    // out = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * N);
    // p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
    // fftw_execute(p);   
    // fftw_destroy_plan(p);
    // fftw_free(in); fftw_free(out);
}

int main(){
    helpmeout();
    getchar();
    return 0;
}