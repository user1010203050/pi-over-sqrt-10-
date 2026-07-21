import mpmath
import time
mpmath.mp.dps=50
E=mpmath.sqrt(10)/125
ST=time.perf_counter()
C=[1,2]
A=0
S=mpmath.mpf(0)

for n in range(2,51,1):
   A=2*(2*n-1)*C[n-1]/n
   C.append(A)
"""
for k in range(0,51,1):
   S=mpmath.mpf(S+C[k]*(125*50**(2*k)-3*6**(2*k))/(10**(5*k)*(2*k+1)))
   print("pi_",k,"=",E*S); 
   print(" ")
ET=time.perf_counter()
TT=ET-ST
print("Work poress is",TT,"sec")
"""
S1=0;
E1=mpmath.sqrt(10)
ST=time.perf_counter()
for k in range(0,51,1):
   S1=mpmath.mpf(S1+C[k]*(97375*50**(2*k)-27*6**(2*k))/(10**(5*k)*(2*k+1)*(2*k+3)))
   print("pi1_",k,"=",(715500-E1*S1)/194750); 
   print(" ")
ET=time.perf_counter()
TT=ET-ST
print("Work poress is",TT,"sec")    
