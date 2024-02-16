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

import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np
import yaml
import logging

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description='Daily shelter overnight occupancy')
parser.add_argument('filename', type=str, help='Path to the configuration file')
parser.add_argument('--plot_colors', '-pc', type=str, help='plot colors', default='green')
args = parser.parse_args()

job_config_paths = ['job_config.yml']
job_config_paths += args.filename

filename = {}
for path in job_config_paths:
    with open(args.filename, 'r') as f:
        this_config = yaml.safe_load(f)
        filename.update(this_config)

filename = {"group_col" : "OCCUPIED_BEDS"}
daily_shelter_proc.groupby(filename["group_col"])

user_config = ['user_config.yml']
user_config += args.plot_colors

plot_colors = {}
for color in plot_colors:
    with open(args.plot_colors, 'r') as f:
        this_user_config = yaml.safe_load(f)
        plot_colors.update(this_user_config)

occupied = plt.scatter(range(len(daily_shelter_proc)), daily_shelter_proc['OCCUPIED_BEDS'], label='Occupied Beds')
unoccupied = plt.scatter(range(len(daily_shelter_proc)), daily_shelter_proc['UNOCCUPIED_BEDS'], label='Unoccupied Beds')

# Adding labels and title
plt.xlabel("Data Points")
plt.ylabel("Number of Beds")
plt.title("Occupied vs Unoccupied Beds")

print(filename)

print(args.filename)

print(args.plot_colors)

# Add a legend
plt.legend()

# Add a grid
plt.grid()

plt.savefig('occ_vs_unocc.png')

# Show the plot
plt.show()

