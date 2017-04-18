#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wuyy
import tornado.ioloop
import tornado.web
from fortress.backend.session.session import SessionFactory

class BaseRequestHandler(tornado.web.RequestHandler):
    def initialize(self):
        # pass
        self.session = SessionFactory.get_session_obj(self)