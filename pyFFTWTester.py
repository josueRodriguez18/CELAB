import math
from scipy.fftpack import fft
import numpy as np
import spitest
import matplotlib
import matplotlib.pyplot as plt
from spitest import NUM_ELEMENTS
from spitest import out as IN
Fs = 7522
NOTERY = { "C":16.35, "C#":17.32, "D":18.35, "D#":19.45, "E#":20.60,"F":21.83, "F#":23.12, "G":24.5, "G#":25.96, "A":27.5, "A#":29.14, "B":30.87, 
 16.35:"C", 17.32:"C#", 18.35:"D", 19.45:"D#", 20.60:"E#", 21.83:"F", 23.12:"F#", 24.5:"G", 25.96:"G#", 27.5:"A", 29.14:"A#", 30.87:"B"}

# absOut = [None] * NUM_ELEMENTS
# def fastFourier():
# 	input = pyfftw.empty_aligned(NUM_ELEMENTS, dtype ='complex128')
# 	for i in range(0, NUM_ELEMENTS):
# 		input[i] = IN[i]
# 	output = pyfftw.empty_aligned(NUM_ELEMENTS, dtype ='complex128')
# 	fft_object = pyfftw.FFTW(input, output)
# 	return output

def max( arr ):
	max = 0
	k = 0
	while k < len(arr):
		if(arr[k] > max):
			max = arr[k]
			pp = k
		k+=1

	return pp
# def fourierABS( arr ):
# 	for x in range(0, NUM_ELEMENTS):
# 		absOut[x] = math.sqrt(arr[x].real**2 + arr[x].imag**2)
# 	return absOut



def nFourier():
	x = np.array(IN)
	output = fft(x)
	output = nFourier()
	output[0] = 0
	output = np.abs(output)
	return output


def noteTable(note):
	octave = 0		
	if ( 11.00 < note and note < 17.32): 
		result = "C"
	elif( 17.32 < note and note < 18.35): 
		result = "C#"
	elif( 18.35 < note and note < 19.45):
		result = "D"
	elif( 19.45 < note and note < 20.60):
		result = "D#"
	elif( 20.60 < note and note < 21.83):
		result = "E"
	elif( 21.83 < note and note < 23.12):
		result = "F"
	elif( 23.12 < note and note < 24.50):
		result = "F#"
	elif( 24.50 < note and note < 25.96):
		result = "G"
	elif( 25.96 < note and note < 27.50):
		result = "A"
	elif( 29.14 < note and note < 30.87):
		result = "A#"
	elif( 30.87 < note and note < 32.70):
		result = "B"
	elif( 32.70 < note and note < 33.0):
		while (note > 32.7):
			note = note/2
			octave += 1
		result = noteTable(note)
	return result, octave


def inOut( freq ):
	print("Frequency: " , freq)
	note = noteTable(freq)
	print(note[0], note[1]) 
	desired = input("Please input desired note (no flats)")
	diff = freq - NOTERY[desired]
	print(diff)

spitest.main()
outty = nFourier()
index = max(outty)
freq = index*Fs/NUM_ELEMENTS
#print(index)
print("Frequency: ", freq)
inOut(freq)
spitest.printer(outty)