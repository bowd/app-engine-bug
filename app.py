from flask import Flask
import google.cloud.logging

client = google.cloud.logging.Client()
client.setup_logging()

app = Flask(__name__)

@app.route('/')
def hello():
    app.logger.info("This is a test")
    return "Hello World!"

@app.route('/exception')
def hello():
    raise ValueError("this is an error")
