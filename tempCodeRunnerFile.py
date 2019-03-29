#
#
# PRO:
#
#



import os
import cmath
import numpy as np
import math


# def eulers_formula(number):
#     import cmath 

def abs_value_of_complex(complex_number):
    import cmath
    i = complex_number
    return(math.sqrt((i.real)**2 + (i.imag)**2))


def DFT(x,delta=1):
    # Special Notes: 
    # 
    # Typically delta = 1
    #
    # x is a LIST of numbers. Generally a frequency / pattern we wish to apply a FFT. 

    N = len(x)
    amplitude = []
    frequency = []
    i = complex(0-1j)
    
    for k in range(0,N):
        ans = 0

        for r in range(0,N):
            ans =  ans + round((x[r] * np.exp((i * 2 * math.pi * k *r)/N)),ndigits=3)

            # If there is imaginary number in exp run eulers formula
            #if ans.imag != 0:
            if r == N-1:
                
                abs_ans = abs_value_of_complex(ans)

                # Calculate frequency
                p = (2 * math.pi * k)/ (N * delta)
                frequency.append(p)

                amplitude.append(abs_ans)

    return(frequency,amplitude)


x1 = [1,4,3,2]

freq, amp = DFT(x1)
print(freq)
print(amp)


import matplotlib.pyplot as plt 
# plotting the points  
fig, ax = plt.subplots()
plt.plot(freq, amp, color='#000000', linestyle='solid', linewidth = 1, 
        marker='o', markerfacecolor='#0336ad', markersize=5)


ax.set_xlabel(r'Frequency', fontsize=15)
ax.set_ylabel(r'Amplitude', fontsize=15)
ax.set_title('Discrete Fourier Transformation', fontsize=15)

ax.grid(True)

# function to show the plot 
#plt.show() 

dir_path = os.path.dirname(os.path.realpath(__file__))

plt.savefig("hello.png")
