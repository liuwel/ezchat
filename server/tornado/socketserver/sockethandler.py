#coding:utf-8
import tornado.websocket
import json
class SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    clients = set()

    @staticmethod
    def send_all(message):
        for c in SocketHandler.clients :
            c.write_message(json.dumps(message))

    def open(self):
        self.write_message(u'=====open=====')
        SocketHandler.clients.add(self)
        print(id(self))
        print(SocketHandler.clients)
        print("WebSocket opened")

    def on_message(self, message):
        SocketHandler.send_all(message)

    def on_close(self):
        SocketHandler.clients.remove(self)
        print("WebSocket closed")