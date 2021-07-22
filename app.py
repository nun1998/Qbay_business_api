import os

# url地址
url = "https://vc4ora8cy4.execute-api.ap-northeast-1.amazonaws.com/dev_v2"

TOKEN = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImlkIjo4NSwidXNlcl90eXBlIjoic2hvcCJ9LCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiaWF0IjoxNjI2OTMzNzc2LCJleHAiOjE2MjcwMjAxNzZ9.xSLqaIkRzgTZoq3hgq0t-p2pCCaE3gBpzN-Am-H2tbs'

header_data = {
    "Content-Type": "application/json",
    "Authorization": TOKEN
}

pepper = "qbaytek2021"

Base_DIR = os.path.dirname(os.path.abspath(__file__))
