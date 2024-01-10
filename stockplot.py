import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def get_stock_data(symbol, start_date, end_date):
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def main():
    st.title("Stock Price History App")

    # Dropdown menu for selecting a stock
    stock_symbol = st.selectbox("Select a stock:", ["AAPL", "GOOGL", "MSFT", "AMZN"])

    # Date range for fetching stock data
    start_date = st.date_input("Start date", pd.to_datetime("2020-01-01"))
    end_date = st.date_input("End date", pd.to_datetime("2022-01-01"))

    # Fetch stock data
    stock_data = get_stock_data(stock_symbol, start_date, end_date)

    if stock_data is not None:
        # Display fetched data
        st.subheader(f"Stock Price History for {stock_symbol}")
        st.write(stock_data)

        # Plot stock price history
        fig, ax = plt.subplots()
        ax.plot(stock_data['Close'], label='Closing Price')
        ax.set_title(f"{stock_symbol} Stock Price History")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (USD)")
        ax.legend()
        st.pyplot(fig)

if __name__ == "__main__":
    main()
