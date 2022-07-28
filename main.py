from flask import Flask, render_template
from regex import D
from API_KEY import G00GLE_API_KEY 
import requests
from datetime import datetime

# Replace channel id for another channel
channel_id = "UCIabPXjvT5BVTxRDPCBBOOQ"

app = Flask(__name__)

def fetchData():
    url = "https://www.googleapis.com/youtube/v3/search?key=" + G00GLE_API_KEY + "&channelId=" + channel_id + "&part=snippet,id&order=date&maxResults=1"
    try:
        res = requests.get(url).json()
        return res
    except:
        print("Fetch failed")

@app.route("/")
def index():
    data = fetchData()

    title = data['items'][0]['snippet']['title']
    channel_name = data['items'][0]['snippet']['channelTitle']
    date_placed = data['items'][0]['snippet']['publishedAt'][:-1].replace('T',' ')
    video_id = data['items'][0]['id']['videoId']
    days_since = (datetime.today() - datetime.strptime(date_placed, '%Y-%m-%d %H:%M:%S')).days
    if days_since == 0:
        today = "YESS!"
    else: 
        today = "No... :("
    return render_template('index.html', title=title, channel=channel_name, date=date_placed, id=video_id, days=days_since, today=today)

if __name__ == '__main__':
    app.run()