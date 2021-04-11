#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   config.py    
@Contact :   zqqqqz2000@sina.cn
@License :   (C)Copyright 2017-2021 ICCD

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/1 19:05   ICCD       1.0         None
"""
import os

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'token'
USERNAME = 'root'
PASSWORD = ''

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD, host=HOST,
                                                                                        port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SESSION_TYPE = 'filesystem'
SECRET_KEY = os.urandom(128)

APIKEY = "L04yE8UUNqLmTIHW03Bz"
# APIKEY = ""
