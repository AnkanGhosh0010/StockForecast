import streamlit as st

def about():
    st.markdown(f"<h2 style='text-align: center;'>Stock Prediction using Linear Regression</h2>", unsafe_allow_html=True)
    st.write("""
    Stock price prediction is an essential task for investors and companies to make informed decisions.
    This app uses linear regression models to predict future stock prices based on historical data.
    Linear regression is a supervised machine learning algorithm that models the relationship between 
    dependent and independent variables.\n
    Stock prediction analysis is crucial for investors to make informed decisions in financial markets. 
    This project explores the application of linear regression in predicting stock prices using Python. 
    Leveraging Python's strong libraries such as plotly, prophet, datetime, and yfinance, we preprocess historical stock data, 
    select relevant features, and train linear regression models. Through thorough evaluation and prediction, 
    we aim to identify trends and patterns in stock data, enabling more accurate forecasting of future stock prices. 
    By conducting stock prediction analysis using linear regression with Python, this project seeks to 
    provide investors with valuable insights and tools for navigating the complexities of financial markets 
    and making informed investment decisions.\n
    With this research a web based application has been created  for stock prediction analysis using linear regression. 
    It leverages historical stock data, downloaded using the Yahoo Finance (yfinance) API, to train a linear regression 
    model for predicting stock prices. The user interface is built using Streamlit, a popular Python library for creating 
    interactive web applications with minimal code. The app starts with a user interface (UI) where the user provides the 
    stock ticker symbol (e.g., TSLA for Tesla) and a date range (start date and end date) for the analysis. The input fields
    for the ticker symbol and date range are created using Streamlit widgets (st.textinput and st.dateinput). 
    The app then downloads historical stock data for the provided ticker and date range using the yfinance API. 
    The stock data includes information such as the stock's opening price, closing price, high and low prices, and trading volume for each day.
    The downloaded data is prepared for analysis by converting the date index into Unix timestamps (int64 format). 
    This transformation is necessary for linear regression modeling. The data is split into features 
    (X - the date in Unix timestamp format) and target (y - the closing price of the stock). 
    The linear regression model is trained using the historical data (X and y). Once the model is trained, 
    it can be used to predict future prices.The app calculates future dates from the last date in the dataset and reshapes them into
    the expected input format for the model. The model predicts the closing prices for the next 30 days based on the future dates.
    The app uses matplotlib and Streamlit's plotting capabilities to display the historical closing prices as a line chart. 
    The predicted prices for the next 30 days are also visualized as a line chart. Additionally, the historical closing prices 
    and the predicted prices are plotted on the same graph, providing an insightful visual representation of the analysis.
    """)

