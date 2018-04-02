#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import web
from utils import *
import hashlib
import os
import subprocess

urls = (
    '/', 'index',
    '/sorry', 'sorry',
    '/chinese', 'chinese',
    '/wangjingze', 'wangjingze',
    '/roll', 'roll'
)

render = web.template.render('templates')

class index:
    def GET(self):
        raise web.seeother('/sorry')

class sorry:
    def GET(self):
        return render.sorry()

    def POST(self):
        data = web.input()
        s1 = str(data.get('s1'))
        s2 = str(data.get('s2'))
        s3 = str(data.get('s3'))
        s4 = str(data.get('s4'))
        s5 = str(data.get('s5'))
        s6 = str(data.get('s6'))
        s7 = str(data.get('s7'))
        s8 = str(data.get('s8'))
        s9 = str(data.get('s9'))
        name1 = str(data.get('name1'))
        name2 = str(data.get('name2'))
        name3 = str(data.get('name3'))
        ass = genass_sorry(s1, s2, s3, s4, s5, s6, s7, s8, s9, name1, name2, name3)
        md5_sr = hashlib.md5()
        md5_sr.update(("sorry" + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + name1 + name2 + name3).encode(encoding='gb2312'))
        md5 = md5_sr.hexdigest()
        with open('cache/' + md5 + '.ass', 'w') as f:
            f.write(ass)
        command_str = 'ffmpeg -i sorry.mp4 -r 8 -vf ass=cache/' + md5  + '.ass -y cache/' + md5 + '.gif'
        os.system(command_str)
        return './cache/' + md5 + '.gif'


class chinese:
    def GET(self):
        return render.chinese()

    def POST(self):
        data = web.input()
        s1 = str(data.get('s1'))
        s2 = str(data.get('s2'))
        ass = genass_chinese(s1, s2)
        md5_sr = hashlib.md5()
        md5_sr.update(("chinese" + s1 + s2).encode(encoding='gb2312'))
        md5 = md5_sr.hexdigest()
        with open('cache/' + md5 + '.ass', 'w') as f:
            f.write(ass)
        command_str = 'ffmpeg -i chinese.mp4 -r 8 -vf ass=cache/' + md5  + '.ass,scale=300:-1 -y cache/' + md5 + '.gif'
        os.system(command_str)
        return './cache/' + md5 + '.gif'


class wangjingze:
    def GET(self):
        return render.wangjingze()

    def POST(self):
        data = web.input()
        s1 = str(data.get('s1'))
        s2 = str(data.get('s2'))
        s3 = str(data.get('s3'))
        s4 = str(data.get('s4'))
        ass = genass_wangjingze(s1, s2, s3, s4)
        md5_sr = hashlib.md5()
        md5_sr.update(("wangjingze" + s1 + s2 + s3 + s4).encode(encoding='gb2312'))
        md5 = md5_sr.hexdigest()
        with open('cache/' + md5 + '.ass', 'w') as f:
            f.write(ass)
        command_str = 'ffmpeg -i wangjingze.mp4 -r 8 -vf ass=cache/' + md5  + '.ass,scale=300:-1 -y cache/' + md5 + '.gif'
        os.system(command_str)
        return './cache/' + md5 + '.gif'


class roll:
    def GET(self):
        return render.roll()

    def POST(self):
        data = web.input()
        s1 = str(data.get('s1'))
        s2 = str(data.get('s2'))
        s3 = str(data.get('s3'))
        ass = genass_roll(s1, s2, s3)
        md5_sr = hashlib.md5()
        md5_sr.update(("roll" + s1 + s2 + s3).encode(encoding='gb2312'))
        md5 = md5_sr.hexdigest()
        with open('cache/' + md5 + '.ass', 'w') as f:
            f.write(ass)
        command_str = 'ffmpeg -i roll.mp4 -r 8 -vf ass=cache/' + md5  + '.ass,scale=300:-1 -y cache/' + md5 + '.gif'
        os.system(command_str)
        return './cache/' + md5 + '.gif'


app = web.application(urls, globals())
application = app.wsgifunc()
