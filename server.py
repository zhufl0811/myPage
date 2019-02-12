import tornado
import json
import os
from tornado.web import StaticFileHandler

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish('asdfas')


current_path = os.path.join(os.path.dirname(__file__))
url = [
(r'^/statics/(.*?)$', StaticFileHandler, {"path": os.path.join(current_path, "statics")}),
(r'^/(.*?)$', StaticFileHandler, {"path": os.path.join(current_path, "templates")}),
(r'/index', IndexHandler),
]

application = tornado.web.Application(handlers=url)

def main():
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9438)
    print("Development server is running at http://127.0.0.1:9438")
    tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
    main()
