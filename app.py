from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask app!"

if __name__ == '__main__':
    # Get the port from the environment variable, default to 5000 if not set
    port = int(os.environ.get('PORT', 5000))
    # Run the Flask app
    app.run(host='0.0.0.0', port=port)
