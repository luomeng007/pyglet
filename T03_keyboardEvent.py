# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/6/23 7:50
software: PyCharm

Description:
   Mouse and keyboard events

Illustration:

"""
import pyglet

window = pyglet.window.Window()


# press key event
@window.event
def on_key_press(symbol, modifiers):
    print("A key was pressed")


@window.event
def on_draw():
    window.clear()


pyglet.app.run()
