[x1,fs1] = audioread('P4.1.wav');
[x2,fs2] = audioread('EndInspiratoryCoarseCrackles.wav');
[x3,fs3] = audioread('Expiratory-Wheeze.wav');
 figure
 dt1 = 1/fs1;
 t1 = 0:dt1:(length(x1)*dt1)-dt1;
 plot(t1,x1);xlabel('Seconds');ylabel('Amplitude');title('Normal Vesicular');
 figure
 plot(psd(spectrum.periodogram,x1,'Fs',fs1,'NFFT',length(x1))); %taking number of points in DFT equal to the length of the signal. If nfft>length, the signal is zero-padded. Otherwise it is wrapped modulo nfft and summed using datawrap.
 title('Normal Vesicular');
 figure
 
 dt2 = 1/fs2;
 t2 = 0:dt2:(length(x2)*dt2)-dt2;
 plot(t2,x2); xlabel('Seconds'); ylabel('Amplitude');
 title('Coarse Crackles');
 figure
 plot(psd(spectrum.periodogram,x2,'Fs',fs2,'NFFT',length(x2)));
 title('Coarse Crackles');
 figure
 dt3 = 1/fs3;
 t3 = 0:dt1:(length(x3)*dt3)-dt3;
 plot(t3,x3); xlabel('Seconds'); ylabel('Amplitude');
 title('Wheeze');
 figure
 plot(psd(spectrum.periodogram,x3,'Fs',fs3,'NFFT',length(x3)));
 title('Wheeze');
 figure
 n1 = size(x1);
 n1 = n1(1,1);
 n2 = size(x2);
 n2 = n2(1,1);
 n3 = size(x3);
 n3 = n3(1,1);
 avg1 = (sum(x1)/n1);
 avg2 = (sum(x2)/n2);
 avg3 = (sum(x3)/n3);
 plot(5,avg1,'Xr');
 hold on;
  plot(5,avg2,'Og');
  hold on;
 plot(5,avg3,'+b');
  xticklabels({'','','','','','Mean'});  
  legend('Normal','Crackles','Wheeze');
  hold off;