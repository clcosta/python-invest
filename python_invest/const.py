import os

# BASE PATH FILE
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# API URL
API_URL = 'http://api.scraperlink.com/investpy/?email={email}&{args}'

# PRODUCTS
PRODUCT_LIST = ['cryptos', 'stocks', 'funds']

# Time Frame
TIME_FRAME_LIST = ['daily', 'monthly', 'weekly']

# Firestore API
FB_BASE_URL = 'https://firestore.googleapis.com/v1/projects/python-invest-67b1c/databases/(default)/documents/'
FB_CRYPTO_DOC_ID = 'crypto/IEVxWEmy32J3FDlvq9Cj'

# BASE EMAIL
BASE_EMAIL = os.getenv('BASE_EMAIL', default='youremail@email.com')

# CONFIG PATH
CONFIG_PATH = os.getenv('CONFIG_PATH', default='./pinv.yaml')
