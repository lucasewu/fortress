#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wuyy
import os,sys

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