#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wuyy


from conf import settings
from hashlib import sha1
import os
import time

create_session_id = lambda: sha1(bytes('%s%s' % (os.urandom(16), time.time()), encoding='utf-8')).hexdigest()


class SessionFactory:

    @staticmethod
    def get_session_obj(handler):
        obj = None

        if settings.SESSION_TYPE == "cache":
            obj = CacheSession(handler)
        elif settings.SESSION_TYPE == "memcached":
            obj = MemcachedSession(handler)
        elif settings.SESSION_TYPE == "redis":
            obj = RedisSession(handler)
        return obj


class CacheSession:
    session_container = {}
    # 键
    session_id = "__sessionId__"

    def __init__(self, handler):
        self.handler = handler
        # 获取浏览器的cookie中__sessionId__的值
        client_random_str = handler.get_cookie(CacheSession.session_id, None)
        if client_random_str and client_random_str in CacheSession.session_container:
            self.random_str = client_random_str
        else:
            self.random_str = create_session_id()
            CacheSession.session_container[self.random_str] = {}

        expires_time = time.time() + settings.SESSION_EXPIRES
        # 设置cookie 键值对和超期时间__sessionId__ = "xxxxxxxxxxxxxxxx"
        handler.set_cookie(CacheSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        ret = CacheSession.session_container[self.random_str].get(key, None)
        return ret

    def __setitem__(self, key, value):
        CacheSession.session_container[self.random_str][key] = value

    def __delitem__(self, key):
        if key in CacheSession.session_container[self.random_str]:
            del CacheSession.session_container[self.random_str][key]


class RedisSession:
    def __init__(self, handler):
        pass


class MemcachedSession:
    def __init__(self, handler):
        pass

