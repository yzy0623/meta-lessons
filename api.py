from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    api_key = "SLl5hjkHwuWvwkEtN"  # 替换为你的 Seniverse API 密钥
    location = request.args.get('location', 'Dongying')  # 默认位置为 Shanghai
    days = request.args.get('days', 5)  # 默认天数为5天
    language = request.args.get('language', 'zh-Hans')  # 默认语言为简体中文
    start = request.args.get('start', 0)  # 默认从今天开始
    
    url = f"https://api.seniverse.com/v3/weather/daily.json"
    params = {
        "key": api_key,
        "location": location,
        "language": language,
        "start": start,
        "days": days
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 如果响应状态码为4xx或5xx，抛出HTTPError
        weather_data = response.json()
        return jsonify(weather_data)
    except requests.RequestException as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()