import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as spstat
import bootcamp_utils

#set matplotlib rc parameters
rc={'lines.linewidth':2, 'axes.labelsize':18, 'axes.titlesize':18}
sns.set(rc=rc)


#Question 3.2

#Question3.2a

#load in the three data sets
#load data

wt_lac=np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m_lac=np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a_lac=np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)
#
#
# #Question3.2b


#separate iptg and fold change
#wild type
iptg_wt=wt_lac[:,0]
fold_change_wt=wt_lac[:,1]

#q18m_lac
iptg_q18m=q18m_lac[:,0]
fold_change_q18m=q18m_lac[:,1]

# #q18a_lac
iptg_q18a=q18a_lac[:,0]
fold_change_q18a=q18a_lac[:,1]

#plot wildtype
plt.semilogx(iptg_wt, fold_change_wt, marker='.', linestyle='none', markersize=18)
plt.xlabel('IPTG Concentration (mM)')
plt.ylabel('Fold Change')
#plot q18m_lac
plt.semilogx(iptg_q18m, fold_change_q18m, marker='.', linestyle='none', markersize=18)
#plot q18a_lac
plt.semilogx(iptg_q18a, fold_change_q18a, marker='.', linestyle='none', markersize=18)
plt.legend(('Wildtype', 'Q18m', 'Q18a'), loc='upper right')
plt.title ('IPTG Concentration vs Fold Change')


#Question 3.2c

WT_RK=141.5
Q18A_RK=16.56
Q18M_RK=1332

def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """function to compute the theoretical fold change"""
    #Wildtype
    #store concentrations as scalar


    fold_change_1=(1+((RK*(1+c/KdA)**2))/((1+c/KdA)**2+Kswitch*(1+c/KdI)**2))**-1
    return fold_change_1

#theoretical fold change for WT
#theor_change_wt=fold_change (iptg_wt, 141.5, KdA=0.017, KdI=0.002, Kswitch=5.8)

#theoretical fold change for q18a
#theor_change_q18a=fold_change (iptg_q18a, 16.56, KdA=0.017, KdI=0.002, Kswitch=5.8)

#theoretical fold change for q18m
#theor_change_q18m=fold_change (iptg_q18m, 1332, KdA=0.017, KdI=0.002, Kswitch=5.8)

#Question 3.2d

#theoretical fold change for evenly spaced list of fake IPTG concentrations

#generate array of 50 closely spaced concentrations
iptg_theor=np.logspace(-1,-6, num=50, endpoint=True, base=10.0, dtype=None)

#theoretical fold change for evenly spaced list of fake IPTG concentrations
#RKWT
WT_theor=fold_change(iptg_theor, WT_RK, KdA=0.017, KdI=0.002, Kswitch=5.8)

#RKq18a
q18a_theor=fold_change(iptg_theor, Q18A_RK, KdA=0.017, KdI=0.002, Kswitch=5.8)

#RKq18a
q18m_theor=fold_change(iptg_theor, Q18M_RK, KdA=0.017, KdI=0.002, Kswitch=5.8)


#plot iptg vs. theor fold_change
plt.semilogx(iptg_theor, WT_theor, marker='.', linestyle='none', markersize=18)
plt.semilogx(iptg_theor, q18a_theor, marker='.', linestyle='none', markersize=18)
plt.semilogx(iptg_theor, q18m_theor, marker='.', linestyle='none', markersize=18)
plt.xlabel('IPTG Concentration (mM)')
plt.ylabel('Theoretical Fold Change')
plt.legend(('Wildtype_theor', 'Q18m_theor', 'Q18a_theor'), loc='lower right')
#spstat.norm.cdf(x)
#plt.show()


#Question 3.2d

#Bohr parameter vs theoretical fold change

def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """function that defines the Bohr parameter"""
    bohr=(-np.log(RK)-np.log((1+c/KdA)**2)/((1+c/KdA)**2+Kswitch*(1+c/KdI)**2))
    return bohr

def fold_change_bohr(bohr_parameter):
    """function that gives fold change as a function of the Bohr parameter"""
    fold_change_theoretical=(1)/(1+np.e**(-bohr))
    return fold_change_theoretical
