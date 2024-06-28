import requests
def login_api(email, password):
    try:
        # Define API endpoint URL
        # Replace with your actual API endpoint URL
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

        # Make POST request to API
        response = requests.post(login_url, json=payload, headers=headers)

        # Check response status and content
        if response.status_code == 200:
            data = response.json()
            if 'token' in data and 'user' in data:
                print("Login API Test Passed Successfully.")
                print("User:", data['user'])
                print("Token:", data['token'])
            else:
                print("Login API Test Failed. Missing expected data in response.")
                print("Response:", data)
        else:
            print(
                f"Login API Test Failed. Status Code: {response.status_code}")
            print("Response:", response.text)

    except requests.RequestException as e:
        print("Error in making request:", e)


if __name__ == "__main__":
    email = "ranagaballah88@gmail.com"
    password = "123456789"

    login_api(email, password)
