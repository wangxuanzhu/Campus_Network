#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :${NAME}.py
# @Time      :${DATE} ${TIME}
# @Author    :Jay

import os
import requests



class LOGIN():
    url = 'http://172.19.16.2/0.htm'
    data = {"DDDDD": '',
            'upass': '',
            'R1': '0',
            'R2': '1',
            'para': '00',
            '0MKKey': '123456',
            'v6ip': ""}

    def Login(user, pwd):
        data["DDDDD"] = user
        data['upass'] = pwd
        requests.post(url=url, data=data)


    def check_net():
        ip = 'www.baidu.com'
        backinfo = os.system('ping -c 1 -w 1 %s' %ip)
        if backinfo:
            return False;
        else:
            return True;

