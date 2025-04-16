import pytest
from project import load_data, calculate_returns, calculate_moving_averages, calculate_bollinger_bands

def test_load_data():
    data_dict = load_data()
    assert len(data_dict) > 0  # Ensure data is loaded
    for stock_id, data in data_dict.items():
        assert not data.empty
        assert 'Date' in data.columns
        assert 'Price' in data.columns
        assert 'Volume' in data.columns

def test_calculate_returns():
    data_dict = load_data()
    for stock_id, data in data_dict.items():
        data = calculate_returns(data)
        assert 'Return' in data.columns
        assert data['Return'].isnull().sum() == 1  # First value should be NaN

def test_calculate_moving_averages():
    data_dict = load_data()
    for stock_id, data in data_dict.items():
        data = calculate_moving_averages(data)
        assert 'Short_MA' in data.columns
        assert 'Long_MA' in data.columns
        assert data['Short_MA'].isnull().sum() > 0
        assert data['Long_MA'].isnull().sum() > 0

def test_calculate_bollinger_bands():
    data_dict = load_data()
    for stock_id, data in data_dict.items():
        data = calculate_bollinger_bands(data)
        assert 'Upper_Band' in data.columns
        assert 'Lower_Band' in data.columns
        assert data['Upper_Band'].isnull().sum() > 0
        assert data['Lower_Band'].isnull().sum() > 0

if __name__ == "__main__":
    pytest.main()
