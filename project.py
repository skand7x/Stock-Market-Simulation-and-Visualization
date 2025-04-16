import pandas as pd
import plotly.graph_objects as go
import glob
import os

def load_data():
    data_files = glob.glob('stock_data_*.csv')
    all_data = {}
    for file in data_files:
        stock_id = os.path.splitext(os.path.basename(file))[0].split('_')[-1]
        all_data[stock_id] = pd.read_csv(file, parse_dates=['Date'])
    return all_data

def calculate_returns(data):
    data['Return'] = data['Price'].pct_change()
    return data

def calculate_moving_averages(data, short_window=20, long_window=50):
    data['Short_MA'] = data['Price'].rolling(window=short_window).mean()
    data['Long_MA'] = data['Price'].rolling(window=long_window).mean()
    return data

def calculate_bollinger_bands(data, window=20):
    data['MA20'] = data['Price'].rolling(window=window).mean()
    data['20_STD'] = data['Price'].rolling(window=window).std()
    data['Upper_Band'] = data['MA20'] + (data['20_STD'] * 2)
    data['Lower_Band'] = data['MA20'] - (data['20_STD'] * 2)
    return data

def visualize_data(data_dict):
    for stock_id, data in data_dict.items():
        data = calculate_returns(data)
        data = calculate_moving_averages(data)
        data = calculate_bollinger_bands(data)

        fig = go.Figure()


        fig.add_trace(go.Candlestick(x=data['Date'],
                                     open=data['Price'],
                                     high=data['Price'],
                                     low=data['Price'],
                                     close=data['Price'],
                                     name='Price'))


        fig.add_trace(go.Scatter(x=data['Date'], y=data['Short_MA'], line=dict(color='blue', width=1), name='20-day MA'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Long_MA'], line=dict(color='orange', width=1), name='50-day MA'))


        fig.add_trace(go.Scatter(x=data['Date'], y=data['Upper_Band'], line=dict(color='gray', width=1, dash='dash'), name='Upper Band'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Lower_Band'], line=dict(color='gray', width=1, dash='dash'), name='Lower Band'))


        fig.add_trace(go.Bar(x=data['Date'], y=data['Volume'], name='Volume', yaxis='y2', marker_color='rgba(0, 0, 255, 0.3)'))

        fig.update_layout(
            title=f'Stock Price Analysis for Stock {stock_id}',
            xaxis_title='Date',
            yaxis_title='Price',
            yaxis2=dict(title='Volume', overlaying='y', side='right'),
            legend=dict(x=0, y=1, traceorder='normal'),
            xaxis_rangeslider_visible=False
        )

        fig.show()

def main():
    data_dict = load_data()
    visualize_data(data_dict)

if __name__ == "__main__":
    main()
