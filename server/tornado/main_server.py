#!/bin/env/python
#-*- encoding=utf-8 -*-

from tornado.options import define,options
from etc import config

define('port',default=8888,help=' run application port ',type=int)

if __name__ == "__main__":
    
    import tornado.ioloop
    import tornado.web
    import tornado.options

    options.parse_command_line()
    app = tornado.web.Application(config.routes,debug=True)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
