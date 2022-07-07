from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

# HTML to grab product price, Best Buy link for ex.
url = 'https://www.amazon.com/MSI-RTX-3080-LHR-10G/dp/B09FSWGS7L/ref=sr_1_2?crid=3NKWMC4XDVNJ&keywords=3080&qid=1654958938&sprefix=3080%2Caps%2C91&sr=8-2'

# Request the webpage
response = Request(url, headers = headers)

# Open and parse the response
webpage = urlopen(response).read()
html = soup(webpage, "html.parser")

# Get product name
product = html.find(id="productTitle").get_text().strip()

# Get and convert price to float
price = float((html.find("span", class_ = "a-offscreen").get_text()).replace('$', ''))

# Twilio
account_sid = 'ACc566b540ea3b8f8ad5bc161def33b4df'
auth_token = '2311913d7534328089006e99e50ce054'
client = Client(account_sid, auth_token)

# Set price threshold and phone number for sending SMS notification
target_price = 650
if(price < target_price):
    message = client.messages \
                    .create(
                         body=f"{product} is now below {target_price} at {price}! \n \n {url}",
                         from_='+19785479096',
                         to='+1---'
                     )
