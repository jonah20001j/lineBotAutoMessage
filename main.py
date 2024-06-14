import os
import requests
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from config import channel_access_token, line_authtoken, ngrok_url

print('ngrok_url:' + ngrok_url)
print('channel_access_token:' + channel_access_token)
print('line_authtoken:' + line_authtoken)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def getNgrokUrltest():
    return 'test'

def send_post_request():
    try:
        # 這裡放置您想要傳送的資料
        data = {
            'info': ngrok_url
        }
        response = requests.post('http://lineBotReply:5000/test', json=data)

        print("定時任務執行，回傳狀態碼：", response.status_code)
        if response.status_code == 200:
            print("回傳資料：", response.json())
    except requests.exceptions.RequestException as e:
        print("POST 請求失敗：", e)

if __name__ == "__main__":
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(func=send_post_request, trigger="interval", seconds=10)  # 每10秒執行一次
    # scheduler.start()
    if not os.getenv("WERKZEUG_RUN_MAIN"):  # 這行確保只有在主進程中執行定時任務
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=send_post_request, trigger="interval", seconds=10)
        scheduler.start()
    try:
        app.run(host='0.0.0.0', port=5001, debug=True)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
