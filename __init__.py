from flask import Flask
#from gevent.pywsgi import WSGIServer
from config import Config

app = Flask(__name__,  template_folder='template')
app.config.from_object(Config)

#from app import routes


if __name__ == '__main__':
    # Serve the app with gevent
    app.run(host='0.0.0.0')
    #http_server = WSGIServer(('0.0.0.0', 5000), app)
    print("Server is running")
    # http_server.serve_forever()
