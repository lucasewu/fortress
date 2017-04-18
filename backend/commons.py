#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wuyy


#随机验证码

#MD5值

import hashlib

def generate_hash(str, method=hashlib.md5):
	obj = method()
	obj.update(str.encode())
	return obj.hexdigest()
print(generate_hash("12345"))
