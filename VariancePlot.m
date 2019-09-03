[x1,fs1] = audioread('Normal_Vesicular.wav');
[x2,fs2] = audioread('EndInspiratoryCoarseCrackles.wav');
[x3,fs3] = audioread('Expiratory-Wheeze.wav');
 
 n1 = size(x1);
 n1 = n1(1,1);
 n2 = size(x2);
 n2 = n2(1,1);
 n3 = size(x3);
 n3 = n3(1,1);
 avg1 = (sum(x1)/n1);
 avg2 = (sum(x2)/n2);
 avg3 = (sum(x3)/n3);  
  y1 = x1-avg1;
  y1 = sum((y1.^2)/n1);
  y2 = x2-avg2;
  y2 = sum((y2.^2)/n1);
  y3 = x3-avg3;
  y3 = sum((y3.^2)/n1);
  figure
   plot(5,y1,'xr');
 hold on;
  plot(5,y2,'og');
  hold on;
 plot(5,y3,'+b');
   legend('normal vesicular','crackles','wheeze');
  xticklabels({'','','','','','','Variance'}); 
  hold off;

 
  
 
 

 