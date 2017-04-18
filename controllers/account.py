#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wuyy
import tornado.ioloop
import tornado.web
from fortress.backend.core.request_handler import BaseRequestHandler
from fortress.models import db_orm
from fortress.models import db_conn
from fortress.backend import commons
from sqlalchemy import and_

class LoginHandler(BaseRequestHandler):
    """docstring for LoginHandler"""
    def get(self):
        self.render("login.html")

    def post(self, *args, **kwargs):
        user = self.get_argument('username')
        pwd = self.get_argument('passwd')
        print(user,pwd)
        r = db_conn.session.query(db_orm.UserProfile).filter(and_(db_orm.UserProfile.username == "wuyy"),db_orm.UserProfile.password == commons.generate_hash(pwd)).all()
        print(r)
        if r:
            print("sss")
class ManagerHandler(tornado.web.RequestHandler):
    """docstring for HostHandler"""
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("manager.html",items=items)

    def post(self, *args, **kwargs):
        pass