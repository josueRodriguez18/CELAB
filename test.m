
fs = 8000;
t = 0:1/fs:32768/fs - 1/fs;
N = 32768;
y1 = sin(440*2*pi*t);
y2 = fftshift(abs(fft(y1)));
w = 0:fs/N:fs - fs/N;
w = -fs/2:fs/N:fs/2 - fs/N;

plot(w,y);
title('Matlab FFT');
xlabel('Hz');
pause;
audiowrite('testInput.wav', y1, fs);