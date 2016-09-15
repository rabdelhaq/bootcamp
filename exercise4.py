import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set()


#question 4.2a:


#load each files into a separate data frame
df_1973 = pd.read_csv('data/grant_1973.csv', comment='#')


#load each files into a separate data frame
df_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df_2012 = pd.read_csv('data/grant_2012.csv', comment='#')


#change column names so they are all the sample

df_1973 = df_1973.rename(columns={'yearband': 'year', 'beak length':'beak length (mm)','beak depth': 'beak depth (mm)'})


#change 1973 year from 73 to 1973
#delete column and create a new one
del df_1973['year']
df_1973.insert(2, 'year', np.array(1973))

#add a year column for the other frames

df_1975.insert(2, 'year', np.array(1975))
df_1987.insert(2, 'year', np.array(1987))
df_1991.insert(2, 'year', np.array(1991))
df_2012.insert(2, 'year', np.array(2012))



#change column names so they are all the sample
df_1975 = df_1975.rename(columns={'Beak length, mm':'beak length (mm)',
                    'Beak depth,mm': 'beak depth (mm)'})

df_1987 = df_1987.rename(columns={'Beak length, mm':'beak length (mm)',
                    'Beak depth,mm': 'beak depth (mm)'})

df_1991 = df_1991.rename(columns={'blength':'beak length (mm)',
                    'bdepth': 'beak depth (mm)'})

df_2012 = df_2012.rename(columns={'blength':'beak length (mm)',
                    'bdepth': 'beak depth (mm)'})




#merge all files into one data frame

df_merge=pd.concat((df_1973, df_1975, df_1987, df_1991,df_2012), ignore_index=True, axis=1)


#Question 4.2: Hacker Stats (bees data)

#load done weight data
df_bees= pd.read_csv('~/git/bootcamp/data/bee_weight.csv', comment='#')

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1)/len(data)


#separate column 4 and 5

df_bees34= df_bees.loc[:, ['Weight', 'Treatment']]

#separate control and pesticide groups

df_control=df_bees.loc[df_bees['Treatment']=='Control', ['Weight']]
df_pesticide=df_bees.loc[df_bees['Treatment']=='Pesticide', ['Weight']]



#Find ECDFs of the drone weight of control and pesticide

x_beesc, y_beesc =ecdf(df_control)
x_beesp, y_beesp =ecdf(df_pesticide)

#plot ECDF
plt.plot(x_beesc, y_beesc, marker='.', linestyle='none')
plt.plot(x_beesp, y_beesp, marker='.', linestyle='none')
plt.legend(('Control, Pesticide'), loc='lower left')

#Question 4.3: Monte Carlo Simulation (DNA transcription)


def backtrack_steps(steps):
    """Function the number of steps it takes for a random walker starting at
    position x=0 to get to position x=+1"""

    rd_steps=np.random.random(steps)
    return rd_steps

random_steps=backtrack_steps(10000)


plt.hist(random_steps, bins=100,normed=True)
plt.close()

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1)/len(data)


randx, randy =ecdf(random_steps)
plt.plot(randx, randy, marker='.', linestyle='none')
