#coding:utf-8

from webserver import mainhandler
from socketserver import sockethandler

routes = [
        (r"/", mainhandler.MainHandler),
        (r"/chat", sockethandler.SocketHandler),
    ]