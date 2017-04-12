#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wuyy
import tornado.ioloop
import tornado.web

class BaseRequestHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass
        # self.session = SessionFactory.get_session_obj(self)