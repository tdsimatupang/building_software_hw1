import pandas as pd
import argparse
import matplotlib.pyplot as plt
import yaml
import logging

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description='Daily shelter overnight occupancy')
    parser.add_argument('filename', type=str, help='Path to the configuration file')
    parser.add_argument('--plot_color_occupied', '-pco', type=str, help='plot color for occupied beds', default='green')
    parser.add_argument('--plot_color_unoccupied', '-pcu', type=str, help='plot color for unoccupied beds', default='red')
    parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose logs')
    args = parser.parse_args()

    # Set logging level
    logging_level = logging.DEBUG if args.verbose else logging.WARNING
    logging.basicConfig(
        level=logging_level, 
        handlers=[logging.StreamHandler(), logging.FileHandler('my_python_analysis.log')],
    )

    # Load the data
    daily_shelter_proc = load_data("/Users/tdsim/OneDrive/Desktop/DSI/Homework/Building Software/Homework_1/SIMATUPANG_TULUS_python_assignment2_orig.csv")

    # Filter out rows with "LOCATION_CITY" equal to "Toronto"
    daily_shelter_proc = filter_data(daily_shelter_proc, "Toronto")

    # Load configuration file
    config = load_config(args.filename)

    # Create plots
    create_plots(daily_shelter_proc, args.plot_color_occupied, args.plot_color_unoccupied)

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        assert not df.empty, "The DataFrame is empty."
        return df
    except Exception as e:
        logging.error("Error occurred while loading the CSV file.")
        raise e

def filter_data(df, city):
    return df[df["LOCATION_CITY"] == city]

def load_config(file_path):
    try:
        with open(file_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        logging.error("Error occurred while loading the YAML file.")
        raise e

def create_plots(df, plot_color_occupied, plot_color_unoccupied):
    plt.scatter(range(len(df)), df['OCCUPIED_BEDS'], label='Occupied Beds', color=plot_color_occupied)
    plt.scatter(range(len(df)), df['UNOCCUPIED_BEDS'], label='Unoccupied Beds', color=plot_color_unoccupied)
    plt.xlabel("Data Points")
    plt.ylabel("Number of Beds")
    plt.title("Occupied vs Unoccupied Beds")
    plt.legend()
    plt.grid()
    plt.savefig('occ_vs_unocc.png')
    plt.show()

if __name__ == "__main__":
    main()
