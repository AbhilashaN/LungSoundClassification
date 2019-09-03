[s,fs1] = audioread('P11-T-N.wav');
order    = 6;
fcutlow  = 150;
fcuthigh = 1500;
[b,a]    = butter(order,[fcutlow,fcuthigh]/(fs1/2), 'bandpass');
x        = filter(b,a,s); % filtered signal
% 
%  dt1 = 1/fs1;
%  t1 = 0:dt1:(length(y)*dt1)-dt1;
%   figure(1)
%   plot(t1,y);
%  t2 = 0:dt1:(length(s)*dt1)-dt1;
%   figure(2)
%   plot(t2,s); title('Ronchi');

% NFFT=1024; %NFFT-point DFT      
% X=fft(x,NFFT);        
% nVals=0:NFFT-1; %DFT Sample points       
% plot(nVals,abs(X));      
% title('Double Sided FFT - without FFTShift');        
% xlabel('Sample points (N-point DFT)')        
% ylabel('DFT Values');
%   n1 = size(x);
%  n1 = n1(1,1);
% avg1 = (sum(x)/n1);
%   y1 = x-avg1;
%   y1 = sum((y1.^2))/n1;

% p = seqperiod(x);
% M = movmean(x,5);
% sum(M)
% max(M)
[pk,dist]=findpeaks(x,5,'MinPeakDistance',800,'MinPeakHeight',0.001); %signal,order of filte
  mean(diff(dist))

 