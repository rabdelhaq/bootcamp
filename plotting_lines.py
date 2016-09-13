import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
import seaborn as sns

#generate an array of x values
x=np.linspace(-15, 15, 400)

#compute the normalized intensity
norm_I=4*(sp.j1(x)/x)**2

#plot our computation
plt.close()
plt.plot(x, norm_I, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x)/I_0$')
#plt.show()


#processing spike data
data=np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')
time=data[:,0]
voltage=data[:,1]

#close all other plots just in case
plt.close()

plt.plot(time,voltage)
plt.xlabel('t(ms)')
plt.ylabel('B(µV)')
plt.xlim(1395,1400)
plt.show()
