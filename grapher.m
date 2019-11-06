load testInput.dat
[n] = size(testInput);
t = 1:459756;
plot(t, testInput);
pause;

load testOutput.dat
x = fft(testInput);
f = 459756/2*[-1:2/459756:1-2/459756];
%f = fs/N
%f = 0:48000/459756:48000-48000/459756;
f = 0:459756-1;
f = f*48000/459756;
plot(f, x);
title('matlab fft');
pause;
plot(f, testOutput);
title('fftw fft');
pause;
%plot(f, z);

[y, Fs] = audioread('ANote.wav');
f = -49756/2:Fs/49756:49756/2;
f = -Fs/2:Fs/49755:Fs/2-Fs/49755;
y = fftshift(abs(fft(y)));
data = y(1:49755,2);
plot(f,data);