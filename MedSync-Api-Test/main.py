import requests
import os
import json
from LoginApiTest import login_api


def load_config(config_file):
    config_path = os.path.join(os.path.dirname(__file__), config_file)
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

if __name__ == "__main__":
    config = load_config('config.json')
    main_website_url = config['login_url']
    email = config['email']
    password = config['password']
    #test-flow
    login_api(email, password)
