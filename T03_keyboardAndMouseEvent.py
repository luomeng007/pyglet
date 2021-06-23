# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/6/23 7:50
software: PyCharm

Description:
    Mouse and keyboard events
    The document of all keys:
    https://pyglet.readthedocs.io/en/latest/modules/window_key.html#module-pyglet.window.key

Illustration:

"""
import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()


# keyboard event
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print("The A key was pressed.")
    if symbol == key.LEFT:
        print("The left arrow key was pressed.")
    if symbol == key.ENTER:
        print("The enter key was pressed.")


# mouse event
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')


@window.event
def on_draw():
    window.clear()


# get the event we want to use
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

pyglet.app.run()
