import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from datetime import datetime

BASE_URL = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok='
START_PAGE = 1
fields = []

CODES = [0, 1]
# KOSPI:0, KOSDAQ:1

res = requests.get(BASE_URL + str(CODES[0]))

"""
43 pg, 50 each, 2149 total (2024-01-23)
"""