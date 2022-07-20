import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "https://www.kaggle.com/sumitsahjr"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("kaggle_profile.svg", scale=10)
