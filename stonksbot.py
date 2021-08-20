import json
import time as time_true
import pathlib
import pandas as pd
from config import *
from td.client import TDClient
from td.utils import TDUtilities


TDSession = TDClient(
    client_id = TD_CLIENT_ID,
    redirect_uri = 'http://192.168.0.12:8080/',
    credentials_path = '/Users/Jason/Desktop/Code/stonks/stonks.json'
)

TDSession.login()

msft = TDSession.get_quotes(instruments=['MSFT'])
print(msft)