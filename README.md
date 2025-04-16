# Advanced Stock Market Simulation and Visualization
#### Video Demo:  [(https://youtu.be/jPbsWh9aTyU)]
#### Description:
This project simulates stock market data using geometric Brownian motion, stores the data in CSV files, and visualizes it with line plots, candlestick charts, moving averages, Bollinger Bands, and volume data using interactive plots from Plotly.

## Files:
- `generate_data.py`: Generates synthetic stock data for multiple stocks and saves them to CSV files.
- `project.py`: Contains the main function and additional functions to load data, calculate returns, moving averages, Bollinger Bands, and visualize the data.
- `test_project.py`: Contains tests for the custom functions using pytest.
- `requirements.txt`: Lists the required packages for the project.
- `dataset`: The 3 csv files contain the synthetic stock simulation data for 3 different stocks.

## How to Run:
1. Generate synthetic data:
    ```bash
    python generate_data.py
    ```
2. Run the main script to visualize the data:
    ```bash
    python project.py
    ```
3. Run tests:
    ```bash
    pytest test_project.py
    ```

## Visualizations:
- **Line Plot**: Shows the stock price over time.
- **Candlestick Chart**: Visualizes open, high, low, and close prices.
- **Moving Averages**: Displays short-term and long-term moving averages.
- **Bollinger Bands**: Shows the volatility of the stock price.
- **Volume**: Visualizes the volume of stocks traded.

## Design Choices:
- Used geometric Brownian motion to simulate realistic stock price movements.
- Included volume data to simulate stock trading activity.
- Chose pandas and numpy for data manipulation and calculation.
- Used Plotly for interactive and dynamic visualizations.
- Added multiple stocks for more comprehensive analysis.
