import time
import pandas as pd
import json
import requests
import os

ais_data = pd.read_csv("./ais20171001_top5/ais_top4_mmsi440311690.csv")

address = os.environ.get('SEND_IP')
port = os.environ.get('PORT')
address = "172.20.10.6"
port = "5005"
i = 0
while True:
    record = ais_data.loc[i, ['MMSI', 'Latitude', 'Longitude', 'SOG', 'COG']]
    record['no'] = i
    r = requests.post(f"http://{address}:{port}/receive_ais_data",
                      data=json.dumps(record.to_dict()))
    if i == len(ais_data):
        i = 0
    i += 1
    time.sleep(1)
