import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def pig_latinize():
    postHeaders = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Origin': 'https://hidden-journey-62459.herokuapp.com',
        'Referer': 'https://hidden-journey-62459.herokuapp.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.111 Safari/537.36'
    }
    payload = {"input_text": get_fact()}
    session = requests.Session()
    response = session.post(url="https://hidden-journey-62459.herokuapp.com/piglatinize/",
                            data=payload, headers=postHeaders)
    return response.url, '<br/><br/>' + payload["input_text"], response.text


@app.route('/')
def home():
    fact = pig_latinize()
    return Response(response=fact, mimetype="text/html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

