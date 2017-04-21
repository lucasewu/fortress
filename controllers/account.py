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
        r = db_conn.session.query(db_orm.UserProfile).filter(and_(db_orm.UserProfile.username == user),db_orm.UserProfile.password == commons.generate_hash(pwd)).all()
        print(r)
        if r:
            self.session["is_login"]=1
            self.redirect(self.get_argument("next", "/manager")) 
            print(self.session.session_container)
class ManagerHandler(BaseRequestHandler):
    """docstring for HostHandler"""
    def get(self):
        # if self.session["is_login"] == 1:
        hostnames = []
        for h in db_conn.session.query(db_orm.Host.hostname).filter().all():
            hostnames.append(h.hostname)

        print(hostnames)
    
        self.render("manager.html",items=hostnames)
        # else:
            
        #     self.redirect(self.get_argument("next", "/login")) 

    def post(self, *args, **kwargs):
        pass