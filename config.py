# config.py
import os
import requests
import time
from dotenv import load_dotenv

# 獲取當前目錄
current_dir = os.path.dirname(os.path.abspath(__file__))
print('current_dir:' + current_dir)

# 構建上一層目錄的 .env 檔案路徑
dotenv_path = os.path.join(current_dir, '../', '.env')
print('dotenv_path:' + dotenv_path)

# 加載 .env 檔案
load_dotenv(dotenv_path)

# 獲取 line channel 金鑰
channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
# 獲取 line control 金鑰
line_authtoken = os.getenv('LINE_AUTHTOKEN')
# 獲取 OpenAI 金鑰
openai_secret_key = os.getenv('OPENAI_SECRET_KEY')
# 獲取 OpenAI 組織
openai_organization = os.getenv('OPENAI_ORGANIZATION')

def get_ngrok_url():
    while True:
        try:
            response = requests.get("http://ngrok:4040/api/tunnels")
            if response.status_code == 200:
                data = response.json()
                tunnels = data.get("tunnels", [])
                if tunnels:
                    # 獲取第一個隧道的 public_url
                    public_url = tunnels[0].get("public_url", None)
                    return public_url
                else:
                    print("No active tunnels found.")
                    print("等待2秒後重試.")
                    time.sleep(2)  # 等待2秒後重試
            else:
                print(f"Failed to get tunnels: {response.status_code}")
                print("等待2秒後重試.")
                time.sleep(2)  # 等待2秒後重試
        except requests.ConnectionError:
            print("Could not connect to ngrok API.")
            print("等待2秒後重試.")
            time.sleep(2)  # 等待2秒後重試

ngrok_url = get_ngrok_url()
