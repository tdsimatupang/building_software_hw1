import pandas as pd
import argparse
import matplotlib.pyplot as plt
import yaml
import logging

# Argument parsing
parser = argparse.ArgumentParser(description='Daily shelter overnight occupancy')
parser.add_argument('filename', type=str, help='Path to the configuration file')
parser.add_argument('--plot_colors', '-pc', type=str, help='plot colors', default='green')
parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose logs')
args = parser.parse_args()

# Set logging level
logging_level = logging.DEBUG if args.verbose else logging.WARNING
logging.basicConfig(
    level=logging_level, 
    handlers=[logging.StreamHandler(), logging.FileHandler('my_python_analysis.log')]
    )

# Load the data to a single DataFrame.
try:
    daily_shelter_proc = pd.read_csv("/Users/tdsim/OneDrive/Desktop/DSI/Homework/Building Software/Homework_1/SIMATUPANG_TULUS_python_assignment2_orig.csv")
except Exception as e:
    logging.info("Error occurred while loading the CSV file.")
    raise e

# Assert that the DataFrame is not empty
assert not daily_shelter_proc.empty, "The DataFrame is empty."

daily_shelter_proc = daily_shelter_proc.loc[daily_shelter_proc["LOCATION_CITY"] != "Toronto"]

# Load configuration file
try:
    with open(args.filename, 'r') as f:
        config = yaml.safe_load(f)
except Exception as e:
    logging.info("Error occurred while loading the YAML file.")
    raise e

# Perform grouping operation
group_col = config.get("group_col", "OCCUPIED_BEDS")
grouped_df = daily_shelter_proc.groupby(group_col)

# Plotting
occupied = plt.scatter(range(len(daily_shelter_proc)), daily_shelter_proc['OCCUPIED_BEDS'], label='Occupied Beds', color=args.plot_colors)
unoccupied = plt.scatter(range(len(daily_shelter_proc)), daily_shelter_proc['UNOCCUPIED_BEDS'], label='Unoccupied Beds', color=args.plot_colors)

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
