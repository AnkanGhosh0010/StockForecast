import streamlit as st
from streamlit_option_menu import option_menu

import login_page
import about  
import stock_forecast  

# Page configurations
st.set_page_config(page_title="StockForecast", page_icon=":chart_with_upwards_trend:", layout="wide")

# Hide default Streamlit hamburger menu and footer
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Login", "About", "Stock Forecast"],
        icons=["house", "info-circle", "bar-chart"],
        menu_icon=None,  
        default_index=0,
    )

def centered_title(title):
    st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)


page_bg = """
<style>
    .stApp {
        background-image: url("https://miro.medium.com/v2/resize:fit:1400/1*hnJmoDkR6-inqCe_JRxW0w.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
</style>
"""

# Pages
if selected == "Login":
    st.markdown(page_bg, unsafe_allow_html=True)
    centered_title('Stock Forecast')
    login_page.main()

if st.session_state.get("authenticated", False):

    if selected == "About":
        centered_title('About')
        about.about()

    if selected == "Stock Forecast":
        st.markdown(page_bg, unsafe_allow_html=True)
        centered_title('Stock📈Forecast')
        stock_forecast.stock_forecast()  

else:
    st.error("Please log in to access this section.")
