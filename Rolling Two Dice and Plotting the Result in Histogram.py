#!/usr/bin/env python
# coding: utf-8

# In[30]:


import random
import matplotlib.pyplot as plt

num_list =[]
number_of_rolls = int(input("Enter the number of dice rolls: "))

for i in range(number_of_rolls):
    dice_sum = random.randint(1,6) + random.randint(1,6)
    num_list.append(dice_sum)
    print(num_list)
    
plt.hist(num_list, bins = 10)
plt.style.use('seaborn-white')
plt.show()


# In[ ]:




