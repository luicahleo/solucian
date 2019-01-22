import SocketServer, socket
import threading
import time
#import Tkinter


#creo mi TCP Handler
class MiTcpHandler(SocketServer.BaseRequestHandler):
    
    #sobrescribo la funcion handle
    def handle(self):
        data= ""
        while data != "salir":
            #intento recibir informacion
            try:
                #este es el cliente que recibe
                self.data = self.request.recv(1024).strip()
                print ("{} wrote:".format(self.client_address[0]))
                print (self.data)
                time.sleep(0.1) #espero 0.1 segundos antes de leer para que no este tan apurado
                # just send back the same data, but upper-cased
                self.request.sendall(self.data.upper())
            #si hubo un error lo digo y termino el handle
            except:
                print ("El cliente D/C o hubo un error")
                data="salir"

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):

        
        try:
            
            # self.request is the TCP socket connected to the client
            self.data = self.request.recv(1024).strip()
            print ("{} wrote:".format(self.client_address[0]))
            print (self.data)
              
            time.sleep(0.1) #espero 0.1 segundos antes de leer para que no este tan apurado
    
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())
        except:
            print ("El cliente deseo o hubo un error")

#ThreadingMixIn crea un manejador por cada cliente, ForkingTCPServer es el tipo de socket
class ThreadServer (SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    allow_reuse_address = True
    
def main():
    #host & port
    host ="192.168.0.105"
    port= 8266
    #creo el server
    server = ThreadServer((host,port),MyTCPHandler)
    #creo un thread del server
    server_thread = threading.Thread(target=server.serve_forever)
    #empiezo el thread
    server_thread.start()
    
    print ("server corriendo..")

    
main()      

   