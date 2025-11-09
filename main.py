# main.py
import threading
import webview
import subprocess
import time
from app import app

def run_flask():
    # disable reloader when launching inside thread
    app.run(port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    t = threading.Thread(target=run_flask, daemon=True)
    t.start()
    # give flask a moment to start
    time.sleep(1)
    webview.create_window("AI Translator", "http://127.0.0.1:5000")
    webview.start()
