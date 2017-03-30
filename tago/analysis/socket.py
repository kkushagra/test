from socketIO_client import SocketIO, LoggingNamespace
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()
import json

# options = {'reconnectionDelay': 10000, 'reconnection': true}

class TagoRealTime:

    def __init__(self, address, token, callback):
        self.socket   = SocketIO(address, 443, LoggingNamespace)
        self.token    = token
        self.callback = callback

    def run(environment, data , token):
        if data.empty():
            data = []

        context = {token, environment}
        self.analysis(context, data)

    def on_response(*arg):
        print 'arg response:'
        # print json.dump(arg)
        print arg['result']

    def listening(self, wait):
        self.socket.emit('register:analysis', self.token)
        self.socket.on('register:analysis', self.on_response)
        self.socket.on('run:analysis', self.on_response)
        
        if wait:
            self.socket.wait(seconds=wait)
        else:
            self.socket.wait()

        return self.socket

    def get_socket():
        self.socket
