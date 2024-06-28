import requests

def register_api(name, email, password, password_confirmation, role, device_key, image=None):
    try:
        # Define API endpoint URL
        register_url = "https://medsyncbackend.smartwaveeg.com/api/register"

        # Prepare request payload
        payload = {
            "name": name,
            "email": email,
            "password": password,
            "password_confirmation" : password_confirmation,
            "role": role,
            "device_key": device_key
        }

        headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
        response = requests.post(register_url, json=payload, headers=headers)

        # Check response status and content
        if response.status_code == 200:
            data = response.json()
            if 'token' in data and 'user' in data:
                print("Registration API Test Passed Successfully.")
                print("User:", data['user'])
                print("Token:", data['token'])
            else:
                print("Registration API Test Failed. Missing expected data in response.")
                print("Response:", data)
        else:
            print(f"Registration API Test Failed. Status Code: {response.status_code}")
            print("Response:", response.text)

    except requests.RequestException as e:
        print("Error in making request:", e)

if __name__ == "__main__":
    name = "Rana Gaballah"
    email = "ranagaba23llah88@gmail.com"
    password = "123456"
    password_confirmation = "123456"
    role = "patient"  # Change to "doctor" if testing doctor registration
    device_key = "your_device_key_here"
    

    register_api(name, email, password, password_confirmation, role, device_key)
