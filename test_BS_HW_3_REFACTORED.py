import pytest
from BS_HW_3_REFACTORED import load_data, filter_data, load_config, create_plots

# Mock data for testing
MOCK_CSV_DATA = """
ID,LOCATION_CITY,OCCUPIED_BEDS,UNOCCUPIED_BEDS
1,Toronto,10,5
2,Mississauga,8,7
3,Toronto,12,3
"""

@pytest.fixture
def mock_csv_file(tmp_path):
    csv_file = tmp_path / "mock_data.csv"
    csv_file.write_text(MOCK_CSV_DATA)
    return str(csv_file)

def test_load_data(mock_csv_file):
    # Test load_data function
    df = load_data(mock_csv_file)
    assert "ID" in df.columns
    assert len(df) == 3

def test_filter_data(mock_csv_file):
    # Test filter_data function
    df = load_data(mock_csv_file)
    filtered_df = filter_data(df, "Mississauga")
    print(filtered_df)
    assert len(filtered_df) == 1
    assert filtered_df["LOCATION_CITY"].unique()[0] == "Mississauga"

def test_load_config(tmp_path):
    # Test load_config function
    yaml_data = """
    key1: value1
    key2: value2
    """
    yaml_file = tmp_path / "config.yaml"
    yaml_file.write_text(yaml_data)
    config = load_config(str(yaml_file))
    assert config["key1"] == "value1"
    assert config["key2"] == "value2"

def test_create_plots(mock_csv_file):
    # Test create_plots function
    df = load_data(mock_csv_file)
    # Assuming plt.savefig and plt.show() don't raise exceptions
    create_plots(df, 'green', 'red')

# Run the tests
if __name__ == "__main__":
    pytest.main(["-v", "test_BS_HW_3_REFACTORED.py"])
