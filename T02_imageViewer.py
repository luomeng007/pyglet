# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/6/23 7:50
software: PyCharm

Description:
   Image Viewer, load image

Illustration:
    if image is bundled with app, we can use pyglet.resource.image()
    if image is not bundled with app, we should use pyglet.image.load()
"""
import pyglet

window = pyglet.window.Window()
image = pyglet.image.load(r"C:\Users\15025\Desktop\angle/angle.jpg")


@window.event
def on_draw():
    window.clear()
    # draw image on screen
    image.blit(0, 0)


pyglet.app.run()
