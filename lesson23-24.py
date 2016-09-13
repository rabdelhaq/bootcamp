import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as spstat



#set matplotlib rc parameters
rc={'lines.linewidth':2, 'axes.labelsize':18, 'axes.titlesize':18}
sns.set(rc=rc)

data_txt=np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

#slice out iptg and gfp (columns one and two
iptg=data_txt[:,0]
gfp=data_txt[:,1]

#plot ipgt vs gfp x log
# plt.semilogx(iptg, gfp, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG(mM)')
# plt.ylabel('Normalized GFP')
# plt.title ('IPTG Titration-semilog X')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()


#slice out iptg and gfp
sem=data_txt[:,2]

#Plot with error bars
#
# plt.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.', markersize=18)
# plt.xlabel('IPTG(mM)')
# plt.ylabel('Normalized GFP')
# plt.title ('IPTG Titration-semilog X')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.xscale('log')
# plt.show()

#Practice exercise 3
