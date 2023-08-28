import streamlit as st #
import os#
import os
#from dotenv import load_dotenv#
#load_dotenv()#
import pandas as pd

PASS_COMPRUEBA      = os.getenv('PASS_COMPRUEBA')#


st.title("vemos si los .env funcionan")
st.title(f" por fa dime que ves.... {PASS_COMPRUEBA}")

st.subheader("padnas")

st.table(pd.read_csv("backt_result_5_years.csv"))