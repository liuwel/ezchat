# coding:utf-8
import tornado.websocket
import json
import time

class SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    clients = set()

    @staticmethod
    def send_all(message):
        for c in SocketHandler.clients:
            c.write_message(message)

    def open(self):
        # self.write_message(u'=====open=====')
        SocketHandler.clients.add(self)
        # print(id(self))
        # print(SocketHandler.clients)
        # print("WebSocket opened")

    def on_message(self, message):
        msg = json.loads(message)
        if msg['command'] == 'message':
            reMsg = {'command':'message','options':{'type':1,'content':msg['options']['content'],'time':time.time()}}
            SocketHandler.send_all(json.dumps(reMsg))
        elif msg['command'] == 'init':
            pass

    def on_close(self):
        SocketHandler.clients.remove(self)
        print("WebSocket closed")
