import json

import requests

def get_crypto_data():
    response = requests.get("http://api.coincap.io/v2/assets")
    data = response.json()
    return data


def update_main_data():
    data = get_crypto_data()
    save_data = open("crypto data.txt", 'w')
    save_data.write(json.dumps(data))
    save_data.close()

def get_crypto_datatxt():
    with open("crypto data.txt", 'r') as save_data:
        data = save_data.readline()
    save_data.close()
    return json.loads(data)

def save_user_crypto(*data):
    data_save = open("user data.txt", 'w')
    data_save.write(json.dumps(data))
    data_save.close()

def read_user_crypto():
    with open("user data.txt", 'r') as save_data:
        data = save_data.readline()
    save_data.close()
    return json.loads(data)