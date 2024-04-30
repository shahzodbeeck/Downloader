from flask import *
import requests
import base64

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('media-downloader.html')


@app.route('/convert', methods=["POST", "GET"])
def convert():
    if request.method == "POST":
        decoded_bytes = base64.b64decode(request.headers.get('accept-message'))
        name = decoded_bytes.decode('utf-8')
        if 'instagram.com' in name:
            response = requests.get(f"https://shaha.u11117.xvest2.ru/Video%20Downloader/insta4.php?url={name}")
            data = response.json()
            serialized_genres = []
            for item in data:
                response = f'<div class="down_center_divs"><img src="{item["thumb"]}" alt=""><a href="{item["link"]}">Yuklab olish</a></div>'
                serialized_genres.append(response)
            return serialized_genres




if __name__ == '__main__':
    app.run(host="0.0.0.0:7000",debug=True)
