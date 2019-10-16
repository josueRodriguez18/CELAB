#include<stdio.h>
#include<math.h>

#define NUM_ELEMENTS 32768 //number of samples
#define fs 8000 //sampling rate

double output[NUM_ELEMENTS];

double parser(){
    double Fd = 0;
    printf("Please input desired frequency in Hz to be generated");
    scanf("%f", Fd);
    return Fd;
}

double * sigGen(double Fd){
    double endTime = NUM_ELEMENTS/fs;
    static double out[NUM_ELEMENTS];
    double t;
    for(int i = 0; i < NUM_ELEMENTS; i++){
        t = i/(endTime*fs);
        out[i] = sin(2*M_PI*t);
    }
    FILE *Fp;
    for(int k = 0; k < NUM_ELEMENTS; i++){
        fprintf(Fp, "f", sigOut[i])
    }
    fclose(fp);
    return out;

}