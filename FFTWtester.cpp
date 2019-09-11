#include <fftw.3.h>
#include <ifstream>
//setup code from tutorial
string filename
//opens file as ifstream object, seeks to end of file
std::ifstream in_file(filename, std::ios::binary | std::ios::ate);
//returns position of the cursor in stream (which we moved to end of file in previous line)
//gives file size in bytes
int file_size = in_file.tellg()
//creates imaginary & real arrays for input data and output data
fftw_complex *in, *out;
//
fftw_plan p;
...
in = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * N);
out = (fftw_complex*)fftw_malloc(sizeof(fftw_complex) * N);
p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
...
fftw_execute(p); /* repeat as needed */
...
fftw_destroy_plan(p);
fftw_free(in); fftw_free(out);
