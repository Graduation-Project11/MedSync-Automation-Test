import requests
import json
import time
import os

def load_config(config_file):
    config_path = os.path.join(os.path.dirname(__file__), config_file)
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

def add_workplace_api(config):
    try:
        url = config['add_workplace_url']
        token = config['token']
        workplace_data = config['workplace_data']

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        # Measure start time
        start_time = time.time()

        # Make POST request to API
        response = requests.post(url, json=workplace_data, headers=headers, timeout=30)

        # Measure end time
        end_time = time.time()
        
        # Calculate the duration
        duration = end_time - start_time

        # Check response status and content
        if response.status_code == 200:
            data = response.json()
            print("AddWorkPlace API Test Passed Successfully.")
            print("Response:")
            print(json.dumps(data, indent=2))
        else:
            print(f"AddWorkPlace API Test Failed. Status Code: {response.status_code}")
            print("Response:", response.text)

        # Print the time it took to make the API call
        print(f"API call duration: {duration:.2f} seconds")

    except requests.RequestException as e:
        print("Error in making request:", e)

if __name__ == "__main__":
    config = load_config('config.json')
    add_workplace_api(config)