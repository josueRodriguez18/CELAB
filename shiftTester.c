#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#define NUM_ELEMENTS 20
#define fs 8000

typedef double fftw_complex[2];
double *fourierABS(fftw_complex *arr);
double max(double * arr);
double fastFourier(fftw_complex *tester);

double * fftShift(double *in){
    double * rH = NULL, *lH = NULL;
    rH = malloc(NUM_ELEMENTS/2*sizeof(double));
    lH = malloc(NUM_ELEMENTS/2*sizeof(double));
    lH = in; rH = in + NUM_ELEMENTS/2;
    for (int i = 0; i < NUM_ELEMENTS/2; i++){
        in[i] = rH[i];
    }
    free(rH);
    for(int i = NUM_ELEMENTS/2; i < NUM_ELEMENTS; i++){
        in[i] = lH[i];
    }
    free(lH);
    return in;
}

double * fourierABS(fftw_complex * arr){
	static double out[NUM_ELEMENTS];
	for(int i = 0; i < NUM_ELEMENTS; i++){
		out[i] = sqrt( arr[i][0]*arr[i][0] + arr[i][1]*arr[i][1] );
    }
	return out;
}

double max(double * arr){
    double max = 0;
    int index = 0;
    for(int i = 0; i < NUM_ELEMENTS; i++){
        if(arr[i] > max){
            max = arr[i];
            index = i;
        }
    }
    return index*fs/NUM_ELEMENTS; //index * fs/NUM_ELEMENTS
}

void cents(double freq){
    double Fd;
    printf("%s", "Please input desired frequency");
    scanf("%f", Fd);
    double c = 1200*log(Fd/freq)/log(2);
    printf("Note is %f away from the desired note", c);

}

double fastFourier(fftw_complex *tester){
        for(int i = 0; i < 20; i++){
            for(int j = 0; j < 2; j++){
                tester[i][j] = 6;
                printf("%d ", tester[i][0]);
            }
            
        }
        double *mag = NULL;
        mag = malloc(20*sizeof(double));
        mag = fourierABS(tester);
        return max(mag);
}
int main(){
    fftw_complex *tester;
    tester = malloc(20*sizeof(fftw_complex));
                for(int i =0; i <20; i++){
                    for(int j = 0; j < 2; j++){
                        tester[i][j] = 6;
                        printf("%d ", tester[i][0]+1);
                    }
                }
    double t = fastFourier(tester); char te[10];


    scanf("%s", te);
    free(tester);
    return 0;
}



