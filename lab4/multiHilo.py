import threading
import SocketServer, socket
import sys

TIMEOUT = 10
HOST = '192.168.0.105'
PORT = 8266


class RequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            threadName = threading.currentThread().getName()
            activeThreads = threading.activeCount() - 1
            clientIP = self.client_address[0]
            print '[%s] -- New connection from %s -- Active threads: %d' % (threadName, clientIP, activeThreads)
            data = self.request.recv(1024)
            print '[%s] -- %s -- Received: %s' % (threadName, clientIP, data)
            response = 'Thanks %s, message received!!' % clientIP
            self.request.send(response)
        except Exception, error:
            if str(error) == "timed out":
                print '[%s] -- %s -- Timeout on data transmission ocurred after %d seconds.' % (threadName, clientIP, TIMEOUT)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

    def finish_request(self, request, client_address):
        request.settimeout(TIMEOUT)
        SocketServer.TCPServer.finish_request(self, request, client_address)
        SocketServer.TCPServer.close_request(self, request)

try:
    print "Starting server TCP at IP %s and port %d..." % (HOST,PORT)
    server = ThreadedTCPServer((HOST, PORT), RequestHandler)
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()