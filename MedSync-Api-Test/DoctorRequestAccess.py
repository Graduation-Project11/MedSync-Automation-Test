import requests
import json
import time
import os

def load_config(config_file):
    config_path = os.path.join(os.path.dirname(__file__), config_file)
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config


def request_sharing_access_api(config):
    try:
        url = config['request_sharing_access_url']
        token = config['token']
        sharing_access_data = config['sharing_access_data']

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        params = {
            'patient_id': sharing_access_data['patient_id'],
            'appointment_id': sharing_access_data['appointment_id']
        }

        start_time = time.time()
        response = requests.post(url, headers=headers, params=params, timeout=30)
        end_time = time.time()
        duration = end_time - start_time

        if response.status_code == 200:
            data = response.json()
            print("RequestSharingAccess API Test Passed Successfully.")
            print("Response:")
            print(json.dumps(data, indent=2))
        else:
            print(f"RequestSharingAccess API Test Failed. Status Code: {response.status_code}")
            print("Response:", response.text)

        print(f"API call duration: {duration:.2f} seconds")

    except requests.RequestException as e:
        print("Error in making request:", e)


if __name__ == "__main__":
    config = load_config('config.json')
    request_sharing_access_api(config)