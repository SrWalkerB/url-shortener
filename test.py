import requests


def send_request():
    return requests.get('https://url-shortener-1067149136139.us-central1.run.app').json()


for i in range(1000):
    send_request()
    print(f'request = {i+1}')

# print(send_request())