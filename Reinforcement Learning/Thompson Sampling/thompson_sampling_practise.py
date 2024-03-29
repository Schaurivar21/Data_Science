"""_____________________Thompson sampling_____________________"""


#Importing Lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing Dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#Implementing Thompson sampling
#Implementing Upper Confidence Bound
import random


N = dataset.shape[0]                 #Length of dataset
d = dataset.shape[1] 


ads_selected = []

numbers_of_rewards_1 = [0] * d            #vector of size d with zeros in it
numbers_of_rewards_0 = [0] * d            #vector of size d with zeros in it
total_reward = 0

for n in range(0, N):
    max_random = 0              #Initialize max_random draw
    ad = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1,
                                         numbers_of_rewards_0[i] + 1)      #different random draw from distributionof beta distribution of parameters that we choose  
        
        
        if random_beta > max_random:
            max_random = random_beta
            ad = i
        
    ads_selected.append(ad) 
    reward = dataset.values[n, ad]
    if reward == 1:     
        numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
    else:
        numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
    total_reward = total_reward + reward
     
#Plotting

plt.hist(ads_selected)
plt.title('Histogram of ads selection')
plt.xlabel('Ads')
plt.ylabel('Numbers of times each ads was selected')
plt.show()