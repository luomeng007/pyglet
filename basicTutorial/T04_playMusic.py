# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/6/23 7:50
software: PyCharm

Description:
    sounds and musics

Illustration:
    if music is bundled with app, we can use pyglet.resource.media()
    if music is not bundled with app, we should use pyglet.media.load()
"""
import pyglet

window = pyglet.window.Window()
music = pyglet.media.load(r"C:\Users\15025\Documents\WeChat Files\wxid_l2sptoavqivz12\FileStorage\File\2020-11/芒种.mp3")
music.play()


pyglet.app.run()
