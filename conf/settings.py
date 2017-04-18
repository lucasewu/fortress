#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wuyy
import os,sys

SESSION_TYPE = "cache"
#session超期时间，单位s
SESSION_EXPIRES = 1800

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



DB_CONN ="mysql+pymysql://root:@localhost:3306/fortress?charset=utf8"

'''
# Database
DATABASES = {
    'default': {
        'ENGINE': 'mysqldb',
        'NAME': 'LittleFinger',
        'HOST': '',
        'PORT':3306,
        'USER':'root',
        'PASSWORD': ''
    }
}
'''