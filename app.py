#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import sys
# from fortress.controllers.account import LoginHandler, ManagerHandler

print(sys.path)
class HostHandler(tornado.web.RequestHandler):
	"""docstring for HostHandler"""
	def get(self):
		self.render("login.html")

	def post(self, *args, **kwargs):
		pass
		


settings = {
    'template_path': 'views',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'cookie_secret': "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
}

application = tornado.web.Application([
    # (r"/login", LoginHandler),
    # (r"/manager", ManagerHandler),
    (r"/host", HostHandler),

], **settings)

if __name__ == "__main__":
    application.listen(8388)
    tornado.ioloop.IOLoop.instance().start()
