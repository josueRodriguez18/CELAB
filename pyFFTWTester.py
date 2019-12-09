import math
from scipy.fftpack import fft
import numpy as np
import spitest
import matplotlib
import matplotlib.pyplot as plt
from spitest import NUM_ELEMENTS
from spitest import out as IN
Fs = 7522
NOTERY = { 'C':16.35, "C#":17.32, 'D':18.35, "D#":19.45, "E":20.60,'F':21.83, "F#":23.12, 'G':24.5, "G#":25.96, 'A':27.5, "A#":29.14, 'B':30.87,
 16.35:'C', 17.32:"C#", 18.35:'D', 19.45:"D#", 20.60:"E", 21.83:'F', 23.12:"F#", 24.5:'G', 25.96:"G#", 27.5:'A', 29.14:"A#", 30.87:'B'}


def max( arr ):
	max = 0
	k = 0
	while k < len(arr):
		if(arr[k] > max):
			max = arr[k]
			pp = k
		k+=1

	return pp



def nFourier():
	x = np.array(IN)
	output = fft(x)
	output[0] = 0
	output = np.abs(output)
	return output


def noteTable(note):
	octave = 0
	result = 0
	while ( note > 31.79 ):
		note = note/2
		octave = octave + 1
	if ( 15.00 < note and note <= 16.84):
		result = "C"  #16.35
	elif( 16.84 < note and note <= 17.84):
		result = "C#" #17.32
	elif( 17.84 < note and note <= 18.90):
		result = "D"  #18.35
	elif( 18.90 < note and note <= 20.03):
		result = "D#" #19.45
	elif( 20.03 < note and note <= 21.22):
		result = "E"  #20.60
	elif( 21.22 < note and note <= 22.48):
		result = "F"  #21.83
	elif( 22.48 < note and note <= 23.81):
		result = "F#" #23.12
	elif( 23.81 < note and note <= 25.23):
		result = "G"  #24.50
	elif( 25.23 < note and note <= 26.73):
		result = "G#" #25.96
	elif( 26.73 < note and note <= 28.32):
		result = "A"  #27.5
	elif( 28.32 < note and note <= 30.00):
		result = "A#" #29.14
	elif( 30.00 < note and note <= 31.79):
		result = "B"  #30.87
	return result, octave


def inOut( freq ):
	print("Frequency: " , freq)
	note = noteTable(freq)
	print(note[0], note[1]) #frequency, octave
	desired = raw_input("Please input desired note (no flats): ")
	desiredoct = input("Please input desired note octave: ")
	#print(desired)
	if (note[1] > 0):
		scale = NOTERY[desired]*2**desiredoct
	diff = freq - scale
	print(diff)

spitest.main()
outty = nFourier()
index = max(outty)
freq = index*Fs/NUM_ELEMENTS
inOut(freq)
spitest.printer(outty)
