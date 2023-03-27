from flask import Flask
   import socket

app = Flask(__name__)

@app.route('/')
def get_ip():
    hostname = socket.gethostname()
    get_ip_address = socket.gethostbyname(hostname)
    return get_ip_address

@app.route('/app')
def get_app_name():
    return "IP App"

if __name__ = '_main_'
    app.run(host="0.0.0.0", port="8090")
 
