import requests
import json
import time
import os

def load_config(config_file):
    config_path = os.path.join(os.path.dirname(__file__), config_file)
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config



def specialties_recommendation_api(config):
    try:
        url = config['specialties_recommendation_url']
        token = config['token']
        recommendation_data = config['recommendation_data']

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.post(url, json=recommendation_data, headers=headers, timeout=60)

        if response.status_code == 200:
            data = response.json()
            print("Specialties Recommendation API Test Passed Successfully.")
            print("Response:")
            print(json.dumps(data, indent=2))
        else:
            print(f"Specialties Recommendation API Test Failed. Status Code: {response.status_code}")
            print("Response:", response.text)

    except requests.RequestException as e:
        print("Error in making request:", e)



if __name__ == "__main__":
    config = load_config('config.json')
    specialties_recommendation_api(config)      