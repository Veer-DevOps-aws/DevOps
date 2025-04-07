from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello,  Nextgen Team, this is Dockerized Python Application on Port 80!"

if __name__ == "__main__":
    # Flask will listen on all IP addresses (0.0.0.0) and port 80
    app.run(host='0.0.0.0', port=80)
