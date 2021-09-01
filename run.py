#!/usr/bin/env python3

import requests, os

# create results directory
if not os.path.exists('results'):
    os.makedirs('results')

# Set variables
link = "https://c5a5571227544bdc90e4f391de560db7.apigw.ntruss.com/custom/v1/10889/43cc23fa52b87b4cc1d02b5b114154151d6adddb17c9fddc06b027fa99e24008/general"
secret_key = input("Enter secret key: ")
headers = {'Content-Type': 'application/json', 'X-OCR-SECRET': secret_key}

for filename in os.listdir('/var/www/html/data'):
    # Set request data
    data = {
        "images": [
        {
            "format": "jpg",
            "name": filename,
            "data": None,
            "url": "http://jju.asuscomm.com/data/" + filename
        }
        ],
        "lang": "ko",
        "requestId": "string",
        "resultType": "string",
        "timestamp": 0,
        "version": "V1"
    }

    # Send request and receive response
    response = requests.post(link, headers=headers, json=data)

    # Write to the file
    with open("results/" + filename.split('.')[0] + '.txt', "w") as f:
        for dic in response.json()['images'][0]['fields']:
            text = dic['inferText']
            f.write(text + ' ')
            if text.endswith('.') | text.endswith('?'):
                f.write('\n')
    
    print(filename, "Done!")
