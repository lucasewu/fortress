#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wuyy
import tornado.ioloop
import tornado.web
from fortress.backend.core.request_handler import BaseRequestHandler

class LoginHandler(BaseRequestHandler):
    """docstring for LoginHandler"""
    def get(self):
        self.render("login.html")

    def post(self, *args, **kwargs):
        pass
class ManagerHandler(BaseRequestHandler):
    """docstring for ManagerHandler"""

    def get(self):
        pass

    def post(self, *args, **kwargs):
        pass