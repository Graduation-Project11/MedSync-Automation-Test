# main.py
import os
import json
from utils import open_main_website
from login import login
from signup import Signup

def load_config(config_file):
    config_path = os.path.join(os.path.dirname(__file__), config_file)
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

if __name__ == "__main__":
    config = load_config('config.json')
    main_website_url = config['main_website_url']
    email = config['email']
    password = config['password']

    website = open_main_website(main_website_url,email,password)

    if website:
        print("Scenario test completed successfully.")
    else:
        print("Scenario test failed.")
        
if __name__ == "__main__":
    config = load_config('config.json')
    request_sharing_access_api(config)