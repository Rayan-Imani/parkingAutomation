from flask import Flask
import threading
from pythonScript import run_parking_bot

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def trigger_bot():
    print("/run endpoint hit")
    threading.Thread(target=run_parking_bot).start()
    print("Bot thread started")
    return "Parking bot finished? maybe", 200

@app.route('/')
def health_check():
    return "Parking bot server is running", 200
