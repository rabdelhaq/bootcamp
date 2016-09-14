import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as spstat
import bootcamp_utils


#set matplotlib rc parameters
rc={'lines.linewidth':2, 'axes.labelsize':18, 'axes.titlesize':18}
sns.set(rc=rc)

k=1
delta_t=0.01
t=np.arange(0,10,delta_t)
n=np.empty_like(t)
n[0]=1
for i in range(1, len(t)):
    n[i]=n[i-1]+delta_t*k*n[i-1]

plt.plot(t,n)
plt.margins(0.02)
plt.xlabel('time')
plt.ylabel('number of bacteria')
plt.show()
plt.close

dr_dt=αr-βfr
df_dt=δfr-γf


α=1
β=0.2
δ=0.3
γ=0.8
delta_t=0.001
t=np.arange(0,60, delta_t)
r[0]=10
f[0]=1

n=np.empty_like(t)
for i in range(1, len(t)):
    n[i]=n[i-1]+delta_t *dr_dt * n[i-1]
    n[i]=n[i-1]+delta_t *df_dt * n[i-1]

plt.plot(t, n)
plt.margins(0.02)
plt.show()
