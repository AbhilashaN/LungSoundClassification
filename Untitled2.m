[x1,fs1] = audioread('P3.1-Coarse-Crackles.wav');
 n1 = size(x1);
 n1 = n1(1,1);
% avg1 = (sum(x1)/n1);
%   y1 = x1-avg1;
%   y1 = sum((y1.^2)/n1);
% y = hilbert(x1);
% figure
% plot(abs(y));
[maxSignal, indexOfMax] = max(x1);
[minSignal, indexOfMin] = min(x1);


