# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder

kv='''
BoxLayout:
    orientation: "vertical"
    BoxLayout:
        Label:
            text: "Kullanıcı Adı:"
            size_hint_x: 1
        TextInput:
            size_hint_x: 5

    BoxLayout:
        Label:
            text: "Parola:"
        TextInput:
            password: True
    BoxLayout:
        Widget:
        Button:
            text: "Gir"
'''

class girisFormu(App):

    def build(self):
        self.root=Builder.load_string(kv)
        return self.root


girisFormu().run()