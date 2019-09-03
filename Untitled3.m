[s,fs1] = audioread('P11-T-N.wav');
y = medfilt1(s,15);
order    = 6;
fcutlow  = 150;
fcuthigh = 1500;
[b,a]    = butter(order,[fcutlow,fcuthigh]/(fs1/2), 'bandpass');
x1        = filter(b,a,y); % filtered signal
% x2        = filter(b,a,s);
 dt1 = 1/fs1;
 t1 = 0:dt1:(length(x1)*dt1)-dt1;
  figure(1)
  plot(t1,x1);title('filtered signal');
% 
%  t2 = 0:dt1:(length(x2)*dt1)-dt1;
%   figure(2)
%   plot(t2,x2);title('unfiltered signal');
  n1 = size(x1);
 n1 = n1(1,1);
avg1 = (sum(x1)/n1)
  y1 = x1-avg1;
  y1 = sum((y1.^2))/n1
  

