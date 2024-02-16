import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np
import yaml
import logging

# 1. Load the data to a single DataFrame.
try:
    daily_shelter_proc = pd.read_csv("/Users/tdsim/OneDrive/Desktop/DSI/Homework/Building Software/Homework_1/SIMATUPANG_TULUS_python_assignment2_orig.csv")
except Exception as e:
    logging.error("Error occurred while loading the CSV file.")
    raise e

# Assert that the DataFrame is not empty
assert not daily_shelter_proc.empty, "The DataFrame is empty."

daily_shelter_proc = daily_shelter_proc.loc[daily_shelter_proc["LOCATION_CITY"] != "Toronto"]

# Argument parsing
parser = argparse.ArgumentParser(description='Daily shelter overnight occupancy')
parser.add_argument('filename', type=str, help='Path to the configuration file')
parser.add_argument('--plot_color_occupied', '-pco', type=str, help='plot color for occupied beds', default='green')
parser.add_argument('--plot_color_unoccupied', '-pcu', type=str, help='plot color for unoccupied beds', default='red')
parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose logs')
args = parser.parse_args()

job_config_paths = ['job_config.yml']
job_config_paths += args.filename

# Set logging level
logging_level = logging.DEBUG if args.verbose else logging.WARNING
logging.info('Message')

logging_level = logging.DEBUG if args.verbose else logging.WARNING
logging.basicConfig(
    level=logging_level, 
    handlers=[logging.StreamHandler(), logging.FileHandler('my_python_analysis.log')],
)

filename = {}
for path in job_config_paths:
    try:
        with open(args.filename, 'r') as f:
            this_config = yaml.safe_load(f)
            filename.update(this_config)
    except Exception as e:
        logging.error("Error occurred while loading the YAML file.")
        raise e

# Perform grouping operation
filename = {"group_col" : "OCCUPIED_BEDS"}
daily_shelter_proc.groupby(filename["group_col"])

user_config = ['user_config.yml']
user_config += args.plot_color_occupied
user_config += args.plot_color_unoccupied

plot_color_occupied = {}
for color in plot_color_occupied:
    try:
        with open(args.plot_color_occupied, 'r') as f:
            this_user_config = yaml.safe_load(f)
            plot_color_occupied.update(this_user_config)
    except Exception as e:
        logging.error("Error occurred while loading the user config.")
        raise e
    
plot_color_unoccupied = {}
for color in plot_color_unoccupied:
    try:
        with open(args.plot_color_unoccupied, 'r') as f:
            this_user_config = yaml.safe_load(f)
            plot_color_unoccupied.update(this_user_config)
    except Exception as e:
        logging.error("Error occurred while loading the user config.")
        raise e

# Plotting
occupied = plt.scatter(range(len(daily_shelter_proc)), daily_shelter_proc['OCCUPIED_BEDS'], label='Occupied Beds', color=args.plot_color_occupied)
unoccupied = plt.scatter(range(len(daily_shelter_proc)), daily_shelter_proc['UNOCCUPIED_BEDS'], label='Unoccupied Beds', color=args.plot_color_unoccupied)

# Adding labels and title
plt.xlabel("Data Points")
plt.ylabel("Number of Beds")
plt.title("Occupied vs Unoccupied Beds")

print(filename)
print(args.filename)
print(args.plot_color_occupied)
print(args.plot_color_unoccupied)

# Add a legend
plt.legend()

# Add a grid
plt.grid()

plt.savefig('occ_vs_unocc.png')

# Show the plot
plt.show()