# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/6/23 7:50
software: PyCharm

Description:
   main window of pyglet

Illustration:
    T01 for test01

Vocabularies:
    dispatch == assign
"""
import pyglet

# create window
window = pyglet.window.Window()
# Keyword arguments: font, position and anchorage of the label(标签的锚定)
label = pyglet.text.Label(text="Hellow, World",
                          font_name="Times New Roman",
                          font_size=36,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x="center", anchor_y="center")


# attach evenet handlers to objects
@window.event
def on_draw():
    # clear background with default black color
    window.clear()
    # draw label on screen
    label.draw()


# call main loop
pyglet.app.run()
