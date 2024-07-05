import requests
import time

def login_api(email, password):
    try:
        # Define API endpoint URL
        login_url = "https://medsyncbackend.smartwaveeg.com/api/login"

        # Prepare request payload
        payload = {
            "email": email,
            "password": password
        }

        headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json',
        }

        # Measure start time
        start_time = time.time()

        # Make POST request to API with increased timeout
        response = requests.post(login_url, json=payload, headers=headers, timeout=30)  # Set timeout to 30 seconds

        # Measure end time
        end_time = time.time()
        
        # Calculate the duration
        duration = end_time - start_time

        # Check response status and content
        if response.status_code == 200:
            data = response.json()
            if 'token' in data and 'user' in data:
                print("Login API Test Passed Successfully.")
                print("User:")
                for key, value in data['user'].items():
                    print(f"  {key}: {value}")
                print("Token:")
                print(f"  {data['token']}")
            else:
                print("Login API Test Failed. Missing expected data in response.")
                print("Response:", json.dumps(data, indent=2))
        else:
            print(f"Login API Test Failed. Status Code: {response.status_code}")
            print("Response:", response.text)

        # Print the time it took to make the API call
        print(f"API call duration: {duration:.2f} seconds")

    except requests.RequestException as e:
        print("Error in making request:", e)