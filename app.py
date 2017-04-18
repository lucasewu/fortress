#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import sys
import sys
sys.path.append("..")
from fortress.backend.core.request_handler import BaseRequestHandler
from fortress.controllers.account import LoginHandler, ManagerHandler
from fortress.models import db_orm
from fortress.models import db_conn

print(sys.path)

class DBHandler(BaseRequestHandler):
    """docstring for HostHandler"""
    def get(self):
         db_orm.Base.metadata.create_all(db_conn.engine)
         self.write("dbinit success")
        # self.render("login.html")
            # data = {
            # "hostid":"1",
            # "hostname":"host1"
            # }
            # self.write(data)

    def post(self, *args, **kwargs):
        pass


class HostHandler(BaseRequestHandler):
	"""docstring for HostHandler"""
	def get(self):
        # self.render("login.html")
            data = {
            "hostid":"1",
            "hostname":"host1"
            }
            self.write(data)

	def post(self, *args, **kwargs):
		pass

		


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/',
    'cookie_secret': "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
}

application = tornado.web.Application([
    (r"/login", LoginHandler),
    (r"/manager", ManagerHandler),
    (r"/host", HostHandler),
    (r"/dbinit", DBHandler),

], **settings)

if __name__ == "__main__":
    application.listen(8388)
    tornado.ioloop.IOLoop.instance().start()
