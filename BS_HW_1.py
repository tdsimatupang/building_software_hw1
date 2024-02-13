#!/usr/bin/env python
# coding: utf-8

# In[2]:


### ***GETTING STARTED***

###1. Load the data to a single DataFrame.
import pandas as pd

daily_shelter_proc = pd.read_csv("/Users/tdsim/OneDrive/Desktop/DSI/Assignment/Python Assignment 2/SIMATUPANG_TULUS_python_assignment2_orig.csv")


# In[3]:


daily_shelter_proc = daily_shelter_proc.loc[daily_shelter_proc["LOCATION_CITY"] != "Toronto"]

daily_shelter_proc.head()


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np

occupied = plt.scatter(range(len(daily_shelter_proc)), daily_shelter_proc['OCCUPIED_BEDS'], label='Occupied Beds')
unoccupied = plt.scatter(range(len(daily_shelter_proc)), daily_shelter_proc['UNOCCUPIED_BEDS'], label='Unoccupied Beds')

# Adding labels and title
plt.xlabel("Data Points")
plt.ylabel("Number of Beds")
plt.title("Occupied vs Unoccupied Beds")

# Add a legend
plt.legend()

# Add a grid
plt.grid()

plt.savefig('occ_vs_unocc.png')

# Show the plot
plt.show()

