import pytest
import pandas as pd
from BS_HW_3_REFACTORED import load_data, filter_data, load_config, create_plots

# A fixture to create a sample DataFrame for testing
@pytest.fixture
def sample_dataframe():
    data = {'ID': [1, 2, 3],
            'LOCATION_CITY': ['Toronto', 'Mississauga', 'Toronto'],
            'OCCUPIED_BEDS': [10, 8, 12],
            'UNOCCUPIED_BEDS': [5, 2, 3]}
    return pd.DataFrame(data)

def test_load_data(sample_dataframe):
    # Test load_data function
    df = load_data("/Users/tdsim/OneDrive/Desktop/DSI/Homework/Building Software/Homework_1/SIMATUPANG_TULUS_python_assignment2_orig.csv")  # Replace with a valid path
    assert df.equals(sample_dataframe)

def test_filter_data(sample_dataframe):
    # Test filter_data function
    filtered_df = filter_data(sample_dataframe, 'Mississauga')
    assert len(filtered_df) == 1
    assert filtered_df.iloc[0]['LOCATION_CITY'] == 'Mississauga'

def test_load_config():
    # Mocking the open function to avoid actual file operations
    with pytest.mock.patch("builtins.open", return_value=pytest.mock.mock_open(read_data="key: value")):
        config = load_config("/Users/tdsim/OneDrive/Desktop/DSI/Homework/Building Software/Homework_1/job_config.yml")  # Replace with a valid path
    assert config == {'key': 'value'}

def test_create_plots(sample_dataframe):
    # Mocking plt.show() to avoid showing the plot during testing
    with pytest.mock.patch("matplotlib.pyplot.show"):
        create_plots(sample_dataframe, 'green', 'red')
