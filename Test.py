#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author  : mundane
# @time    : 2017/5/10 13:23
# @file    : Test.py
# @Software: PyCharm Community Edition

str_nihao = '你好'
# byte
bytes_nihao = str_nihao.encode('utf-8')
print(type(bytes_nihao))
print(bytes_nihao)
bytes2 = b'\xe4\xbd\xa0\xe5\xa5\xbd'
str2 = bytes2.decode('utf-8')
print(type(str2))
print('str2 =', str2)
