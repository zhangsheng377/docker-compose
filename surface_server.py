import json
import psutil
from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    return hello_world1()


@app.route("/battery", methods=['POST', 'GET'])
def hello_world1():
    return json.dumps({
   "variables" : {
      "battery" : psutil.sensors_battery().percent,
   },
   "id" : "battery",
   "name" : "battery",
   "connected" : True
})

if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=28866,debug=True)
    # app.run(host='0.0.0.0',port=28866,debug=False)
    #run(host, port, debug, **options)
    #host要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用
    #port 端口号 默认5000
    #debug 提供调试信息 TRUE 为提供
    http_server = WSGIServer(('0.0.0.0', 28866), app)
    http_server.serve_forever()
