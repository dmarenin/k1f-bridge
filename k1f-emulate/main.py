from socketserver import TCPServer, ThreadingMixIn, BaseRequestHandler
from datetime import datetime, date
from protocol import do_command


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

class K1FSocketServerHandler(BaseRequestHandler):
    def handle(self):
        self.callback(self.server, self.request, self.client_address)

class K1FSocketServer():
    handler = K1FSocketServerHandler

    def __init__(self):
        self.handler.callback = self.callback

    def callback(self, server, request, client_address):    
        print('')

        while True:
            try:
                buf = request.recv(8192)
            except:
                break

            if not buf: 
                break
            
            res = do_command(buf)

            request.sendall(res)

        print('')


TCP_IP = '0.0.0.0'
TCP_PORT = 49152

if __name__ == '__main__':
    ones_serv = K1FSocketServer()
    server = ThreadedTCPServer((TCP_IP, TCP_PORT), K1FSocketServerHandler)
    
    print('starting k1f socket server '+str(TCP_IP)+':'+str(TCP_PORT)+' (use <Ctrl-C> to stop)')

    server.serve_forever()
    
