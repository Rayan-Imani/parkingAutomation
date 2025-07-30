from flask import Flask
import threading
from pythonScript import run_parking_bot

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def trigger_bot():
    threading.Thread(target=run_parking_bot).start()
    return "✅ Parking bot started", 200

@app.route('/')
def health_check():
    return "Parking bot server is running", 200
