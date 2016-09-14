#bootcamp_utils: A collection of statistical functions
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def ecdf(data):
    '''
    compute x, y values for an empirical distribution function
    '''
    x=np.sort(data)
    y=np.arange(1, 1+len(x))/len(x)

    return x, y


def func(array):
    """function that takes in an array and computes a statistic"""
    array_mean=np.mean(array)
    #array_std=np.std(array)
    #array_median=np.median (array)
    return array_mean


def draw_bs_reps(data,func,size=1):
    """function that takes in an array, draws bootstrap reps., and
    returns a statistic"""
    n=len(data)
    reps=np.empty(size)
    for i in range (size):
        bs_sample=np.random.choice(data, replace=True, size=n)
        reps[i]=func(bs_sample)
    return reps


def conf_int(data, u1, u2):
    """function that returns the confidence interval between u1 and u2"""
    confidence_interval=np.percentile(data, [u1,u2])
    print (confidence_interval)
