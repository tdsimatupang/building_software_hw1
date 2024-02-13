#!/usr/bin/env python
# coding: utf-8

# # Assignment #2
# ## Pandas and Visualization
# 
# ### Getting Data
# Select a dataset from [Toronto Open Data](https://open.toronto.ca/catalogue/) or another data portal of your choice, and download it. Some suggested datasets are linked below and additionally available for download in [the course repo /data folder](https://github.com/amfz/dsi-python-workshop/tree/main/data). A good dataset for this exercise will have a mix of data types.
# 
# Some sugested datasets:
# * [TTC bus delays](https://open.toronto.ca/dataset/ttc-bus-delay-data/): Fewer columns, not well documented, some NaNs. Similar to data we've worked with in class. Recommend choosing a full year of data.
# * [Apartment building evaluations](https://open.toronto.ca/dataset/apartment-building-evaluation/): Lots of columns, well-documented, some NaNs.
# * [Daily shelter overnight service occupancy and capcity](https://open.toronto.ca/dataset/daily-shelter-overnight-service-occupancy-capacity/): The largest of the datasets suggested. Lots of columns, well-documented, more NaNs.
# 
# ### Metadata Review
# 1. What organization publishes this dataset? 
#    ***City of Toronto***
# 2. How frequently is the dataset updated? 
#    ***Daily***
# 3. What metadata is available (e.g., column names, data types, descriptions)?
#    ***Column Names, Data Types and Non-Null Counts***
# 4. Is there documentation about who or what produces the data? About who collects it? Through what processes?
#    ***Yes. The data is administered by Shelter, Support & Housing Administration of City of Toronto. Here is the link how they gather the data: https://www.toronto.ca/city-government/data-research-maps/research-reports/housing-and-homelessness-research-and-reports/shelter-census/***
# 5. Is there documentation about limitations of the data, such as possible sources of error or omission?
#    ***Yes. Here is the limitations: This is unaudited data compiled directly from an administrative database. Data reflect only the state of each program's records in the database and may not always accurately reflect the actual current situation in each program.***
# 6. Are there any restrictions concerning data access or use? (e.g.,registraton required or non-commercial use only).
#    ***There is no restriction based on this Open Data License: https://open.toronto.ca/open-data-license/***
# 
# ### Getting started --> ***PLEASE SEE THE CODES BELOW***
# 1. Load the data to a single DataFrame.
# 2. Profile the DataFrame.
#    * What are the column names?
#    * What are the dtypes when loaded? Do any not make sense?
#    * How many NaNs are in each column?
#    * What is the shape of the DataFrame?
# 3. Generate some summary statistics for the data.
#    * For numeric columns: What are the max, min, mean, and median?
#    * For text columns: What is the most common value? How many unique values are there?
#    * Are there any statistics that seem unexpected?
# 4. Rename one or more columns in the DataFrame.
# 5. Select a single column and find its unique values.
# 6. Select a single text/categorical column and find the counts of its values.
# 7. Convert the data type of at least one of the columns. If all columns are typed correctly, convert one to `str` and back.
# 8. Write the DataFrame to a different file format than the original.
# 
# ### More data wrangling, filtering  --> ***PLEASE SEE THE CODES BELOW***
# 1. Create a column derived from an existing one. Some possibilities:
#    * Bin a continuous variable
#    * Extract a date or time part (e.g. hour, month, day of week)
#    * Assign a value based on the value in another column (e.g. TTC line number based on line values in the subway delay data)
#    * Replace text in a column (e.g. replacing occurrences of "Street" with "St.")
# 2. Remove one or more columns from the dataset.
# 3. Extract a subset of columns and rows to a new DataFrame
#    * with the `.query()` method and column selecting `[[colnames]]`
#    * with `.loc[]`
# 4. Investigate null values
#    * Create and describe a DataFrame containing records with NaNs in any column
#    * Create and describe a DataFrame containing records with NaNs in a subset of columns
#    * If it makes sense to drop records with NaNs in certain columns from the original DataFrame, do so.
# 
# ### Grouping and aggregating
# 1. Use `groupby()` to split your data into groups based on one of the columns.
# 2. Use `agg()` to apply multiple functions on different columns and create a summary table. Calculating group sums or standardizing data are two examples of possible functions that you can use.
# 
# ### Plot
# 1. Plot two or more columns in your data using `matplotlib`, `seaborn`, or `plotly`. Make sure that your plot has labels, a title, a grid, and a legend.

# In[10]:


### ***GETTING STARTED***

###1. Load the data to a single DataFrame.
import pandas as pd

daily_shelter = pd.read_csv("/Users/tdsim/OneDrive/Desktop/DSI/Assignment/Python Assignmen 2/SIMATUPANG_TULUS_python_assignment2_orig.csv")


# In[3]:


###2. Profile the DataFrame.
   #* What are the column names?

column_names = daily_shelter.loc[daily_shelter["_id"].isna()]

display(column_names.transpose())


# In[4]:


###2. Profile the DataFrame.
    #* What are the dtypes when loaded? Do any not make sense?

daily_shelter.info()


# In[5]:


###2. Profile the DataFrame.
    #* How many NaNs are in each column?

NaN_count = daily_shelter.isna().sum()


print(NaN_count)


# In[6]:


###2. Profile the DataFrame.
    #* What is the shape of the DataFrame?

print(daily_shelter.shape)


# In[11]:


###3. Generate some summary statistics for the data.
   #* For numeric columns: What are the max, min, mean, and median?

shelter_room_summary = (daily_shelter.groupby("SHELTER_GROUP")
                        .agg(Capacity_Actual_Room_COUNT=("CAPACITY_ACTUAL_ROOM", "count"),
                             Capacity_Funding_Room_MAX=("CAPACITY_FUNDING_ROOM", "max"),
                             Occupied_Rooms_MIN=("OCCUPIED_ROOMS", "min"),
                             Unoccupied_Rooms_MEAN=("UNOCCUPIED_ROOMS", "mean"),
                             Unavailable_Rooms_MEDIAN=("UNAVAILABLE_ROOMS", "median")))

shelter_room_summary


# In[8]:


###3. Generate some summary statistics for the data.
   #* For text columns: What is the most common value? How many unique values are there?

#common values
common_values = daily_shelter[["LOCATION_NAME", "PROGRAM_NAME"]].apply(lambda x: set(x.dropna()), axis=1).apply(set.intersection)

pd.set_option("display.max_colwidth", None)

print(common_values)


# In[9]:


#drop duplicates --> for my own analysis to compare between drop duplicates vs unique.

daily_shelter[["LOCATION_NAME", "PROGRAM_NAME"]].drop_duplicates()


# In[10]:


#unique values from LOCATION_NAME & PROGRAM_NAME columns

unique_locations = daily_shelter["LOCATION_NAME"].unique()
unique_programs = daily_shelter["PROGRAM_NAME"].unique()

print("Unique Locations:")
print(unique_locations)

print("\nUnique Programs:")
print(unique_programs)



# In[11]:


#unique values count

print(f"Number of unique programs: {daily_shelter['PROGRAM_NAME'].nunique()}")
print(f"Number of unique locations: {daily_shelter['LOCATION_NAME'].nunique()}")
print("\n")

print(daily_shelter["PROGRAM_NAME"].value_counts())
print("\n")
print(daily_shelter["LOCATION_NAME"].value_counts())


# ###3. Generate some summary statistics for the data.
#    #* Are there any statistics that seem unexpected?
# 
# No, there are no any statistics that seem unexpected

# In[12]:


###4. Rename one or more columns in the DataFrame.
daily_shelter.rename(columns={"PROGRAM_MODEL": "THE_MODEL_OF_THE_PROGRAM", 
                              "PROGRAM_AREA": "THE_AREA_OF_THE_PROGRAM"}, inplace=True)

print(daily_shelter.columns)


# In[13]:


###5. Select a single column and find its unique values.
unique_location_city = daily_shelter["LOCATION_CITY"].unique()

print("Unique Location City:")
print(unique_location_city)


# In[14]:


###6. Select a single text/categorical column and find the counts of its values.
print(daily_shelter["LOCATION_CITY"].value_counts())


# In[15]:


###7. Convert the data type of at least one of the columns. If all columns are typed correctly, convert one to str and back

# original data type

daily_shelter.info()


# In[16]:


#After I changed the data type for "_id" and "OCCUPANCY_DATE" to str

daily_shelter["_id"] = daily_shelter["_id"].astype("str") #the data type changed from int64 to string

daily_shelter['OCCUPANCY_DATE'] = daily_shelter['OCCUPANCY_DATE'].astype("str") #the data type changed from date to string

ID_and_DATE = daily_shelter[["_id", "OCCUPANCY_DATE"]]
ID_and_DATE.info()


# In[17]:


#I changed back the data type for "_id" and "OCCUPANCY_DATE" from str to original data type

daily_shelter["_id"] = daily_shelter["_id"].astype("int64") #revert it back to int64

#revert it back to date
daily_shelter['OCCUPANCY_DATE'] = pd.to_datetime(daily_shelter['OCCUPANCY_DATE']) 
daily_shelter['OCCUPANCY_DATE'] = daily_shelter['OCCUPANCY_DATE'].astype('object') 

ID_and_DATE = daily_shelter[["_id", "OCCUPANCY_DATE"]]
ID_and_DATE.info()


# In[18]:


###8. Write the DataFrame to a different file format than the original.

daily_shelter.to_csv("/Users/tdsim/OneDrive/Desktop/DSI/Assignment/Python Assignmen 2/SIMATUPANG_TULUS_python_assignment2_proc.csv")


# In[2]:


### MORE DATA WRANGLING, FILTERING

import pandas as pd

daily_shelter_proc = pd.read_csv("/Users/tdsim/OneDrive/Desktop/DSI/Assignment/Python Assignmen 2/SIMATUPANG_TULUS_python_assignment2_proc.csv")


# In[3]:


###1. Create a column derived from an existing one. I use BIN method to to create a range column called OCCUPANCY_RATE_ROOMS_BIN from OCCUPANCY_RATE_ROOMS column.

bin_range = 10

daily_shelter_proc['OCCUPANCY_RATE_ROOMS_BIN'] = pd.cut(
    daily_shelter_proc['OCCUPANCY_RATE_ROOMS'],
    bins=range(0, 120, bin_range),
    include_lowest=True,
    right=False,
    labels=[f"{start}-{start+bin_range}" for start in range(0, 110, bin_range)]
)

print(daily_shelter_proc[['OCCUPANCY_RATE_ROOMS_BIN']].head(11))


# In[21]:


###2. Remove one or more columns from the dataset.

columns_to_remove = ["SECTOR", "CAPACITY_TYPE", "OCCUPIED_BEDS"]
daily_shelter_proc = daily_shelter_proc.drop(columns=columns_to_remove)


# In[33]:


###3. Extract a subset of columns and rows to a new DataFrame
    #* with the .query() method

subset_daily_shelter_proc_query = daily_shelter_proc.query("OCCUPANCY_RATE_ROOMS < 75")[["LOCATION_NAME", "PROGRAM_NAME", "OCCUPANCY_RATE_ROOMS"]]

print(subset_daily_shelter_proc_query.head(7))


# In[34]:


#* with column selecting [[colnames]] method

subset_daily_shelter_proc_colnames = daily_shelter_proc[daily_shelter_proc["OCCUPANCY_RATE_ROOMS"] < 75][["LOCATION_NAME", "PROGRAM_NAME", "OCCUPANCY_RATE_ROOMS"]]

print(subset_daily_shelter_proc_colnames.head(7))


# In[35]:


#*with .loc[]

subset_daily_shelter_proc_loc = daily_shelter_proc.loc[daily_shelter_proc["OCCUPANCY_RATE_ROOMS"] < 75, ["LOCATION_NAME", "PROGRAM_NAME", "OCCUPANCY_RATE_ROOMS"]]

print(subset_daily_shelter_proc_loc.head(7))


# In[49]:


###4. Investigate null values
    #* Create and describe a DataFrame containing records with NaNs in any column

null_values_nan_any_column = daily_shelter_proc.loc[daily_shelter_proc["OCCUPANCY_RATE_ROOMS"].isna()]

null_values_nan_any_column.head(10)


# In[51]:


#* Create and describe a DataFrame containing records with NaNs in a subset of columns

null_values_nan_subset = (daily_shelter_proc.loc[daily_shelter_proc['OCCUPANCY_RATE_ROOMS'].isna(),
                 ["LOCATION_NAME", "PROGRAM_NAME", "OCCUPANCY_RATE_ROOMS"]]
                .head(10))

null_values_nan_subset


# In[4]:


#*If it makes sense to drop records with NaNs in certain columns from the original DataFrame, do so.

null_values_nan_subset = daily_shelter_proc.loc[daily_shelter_proc['OCCUPANCY_RATE_ROOMS'].isna(),
                                            ["LOCATION_NAME", "PROGRAM_NAME", "OCCUPANCY_RATE_ROOMS"]
                                           ].head(10)

# Drop records with NaN values in the specified columns
non_null_values_subset = daily_shelter_proc.dropna(subset=['LOCATION_NAME', 'PROGRAM_NAME', 'OCCUPANCY_RATE_ROOMS']
                                              ).head(10)

# Display the DataFrames
print("Records with NaN values:")
print(null_values_nan_subset)

print("\nRecords without NaN values:")
print(non_null_values_subset)


# In[8]:


### GROUPING AND AGGREGATING
#1. Use groupby() to split your data into groups based on one of the columns.

location_program_groups = daily_shelter_proc.groupby(["LOCATION_NAME", "PROGRAM_NAME"])

location_program_groups.size().unstack(0).head()


# In[12]:


daily_shelter_proc.info()


# In[15]:


#2. Use agg() to apply multiple functions on different columns and create a summary table.

occupancy_summary = (daily_shelter_proc.groupby("OCCUPANCY_DATE")
                        .agg(OCCUPANCY_RATE_ROOMS_COUNT=("OCCUPANCY_RATE_ROOMS", "count"),
                             OCCUPIED_ROOMS_SUM=("OCCUPIED_ROOMS", "sum")))

occupancy_summary


# In[16]:


occupancy_summary.mean()


# In[102]:


### PLOT
#1. Plot two or more columns in your data using matplotlib, seaborn, or plotly. Make sure that your plot has labels, a title, a grid, and a legend.


daily_shelter_proc = daily_shelter_proc.loc[daily_shelter_proc["LOCATION_CITY"] != "Toronto"]

daily_shelter_proc.head()


# In[103]:


daily_shelter_proc.info()


# In[123]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

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


# In[ ]:




