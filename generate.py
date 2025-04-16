import pandas as pd
import numpy as np

def generate_stock_data(num_days=252, initial_price=100, seed=42, num_stocks=3):
    np.random.seed(seed)
    dates = pd.date_range(start='2020-01-01', periods=num_days, freq='B')
    stocks_data = {}

    for stock_id in range(1, num_stocks + 1):
        prices = [initial_price]
        volumes = np.random.randint(100, 1000, size=num_days)

        for _ in range(1, num_days):
            prices.append(prices[-1] * np.exp(np.random.normal(0, 0.01)))

        stocks_data[f'Stock_{stock_id}'] = pd.DataFrame({
            'Date': dates,
            'Price': prices,
            'Volume': volumes
        })

    for stock_id, data in stocks_data.items():
        data.to_csv(f'stock_data_{stock_id}.csv', index=False)

    return stocks_data

if __name__ == "__main__":
    generate_stock_data()

