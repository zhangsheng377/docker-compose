import json
import os
import platform
import psutil
from flask import Flask
from gevent.pywsgi import WSGIServer

sys_flag = platform.system()

app = Flask(__name__)


def request_parse(req_data):
    """解析请求数据并以json形式返回"""
    if req_data.method == 'POST':
        return req_data.json
    elif req_data.method == 'GET':
        return req_data.args
    return {}


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    return "hello_world"


def handle_shutdown():
    if sys_flag == "Linux":
        return os.system("shutdown -t 0")
    else:
        return os.system("shutdown -s -t 0")


def handle_reboot():
    if sys_flag == "Linux":
        return os.system("reboot")
    else:
        return os.system("shutdown -r -t 0")


def handle_reboot_to_other():
    if sys_flag == "Linux":
        """
        # /usr/local/bin/reboot_to_windows
        sudo -S grub-reboot 4
        sudo -S reboot
        """
        return os.system("reboot_to_windows")
    else:
        return handle_reboot()


@app.route("/<action>.action", methods=['POST', 'GET'])
def handle(action):
    if action == "shutdown":
        return str(handle_shutdown())
    elif action == "reboot":
        return str(handle_reboot())
    elif action == "reboot_to_other":
        return str(handle_reboot_to_other())
    else:
        print(f"handle action:{action} is unknown!")
        return f"handle action:{action} is unknown!"
    

if __name__ == '__main__':
    # app.debug = True
    http_server = WSGIServer(('0.0.0.0', 28866), app)
    http_server.serve_forever()
    # app.run(host="0.0.0.0", debug=True)
