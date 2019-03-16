from server.conf import *
from server import app

if __name__ == '__main__':
    app.run(API_SERVER, API_PORT, threaded=True) 

