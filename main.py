import requests
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import streamlit as st

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

st.title("Welcome to the PriceCheckNotify(2.0) application")

st.subheader("An application to track prices on Amazon products")

st.markdown("Built by Arian Kharazmi")

text_input = st.text_input("Price Check:")
st.markdown(f"My Amazon URL input:  {text_input}")
text_area_input = st.text_area("Enter the Amazon URL for the Product.")



# Amazon product you want
#url = 'https://www.amazon.com/Game-Thrones-Complete-Digital-Blu-ray/dp/B07QGL9ZT4/ref=sr_1_1_sspa?keywords=Game+of+Thrones+Complete+Series&qid=1662860890&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUVRJRUdNSjJTRUFPJmVuY3J5cHRlZElkPUEwMTQ5OTE1M1U4MFRISzFTOVlUOSZlbmNyeXB0ZWRBZElkPUEwNDU5NDIzMUpWOVg5TE5HTDhRVSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
url = 'https://www.amazon.com/Sony-Alpha-ZV-E10-Interchangeable-Mirrorless/dp/B09BBLH4SG/ref=sr_1_3?keywords=sony+zv-e10&qid=1663042686&sr=8-3'
#url = 'text_area_input'



# Request the webpage

response = Request(url, headers = headers)

# Open and parse the response
webpage = urlopen(response).read()
html = soup(webpage, "html.parser")

# Get product name
product = html.find(id="productTitle").get_text().strip()

# Get and convert price to float
price = float((html.find("span", class_ = "a-offscreen").get_text()).replace('$', ''))

number_input = st.number_input("target_price", min_value=0, max_value=100000)
threshold = st.slider(
    "Select your target price", min_value=1.0, max_value=10000.0, step=1.0)
st.write(threshold)

target_price = number_input
if(price < target_price):
   print("Meets sale target!")
else:
    print("Does not meet sale target!")


st.write("Enter your price target")
if(price < target_price):
   st.write("Meets sale target!")
else:
    st.write("Does **not** meet sale target!")
