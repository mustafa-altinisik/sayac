# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'widht', '800')
Config.set('graphics', 'height', '480')

Config.set('kivy', 'keyboard_mode', 'systemanddock')
Config.set('kivy', 'keyboard_layout', 'numeric')
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import os
#import RPi.GPIO as GPIO
speed = 1.0
beepPin = 17
ledPin = 27
buttonPin = 22
flashLedPin = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(beepPin, GPIO.OUT)
GPIO.output(beepPin, GPIO.LOW)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)
GPIO.setup(flashLedPin, GPIO.OUT)
GPIO.output(flashLedPin, GPIO.LOW)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Window.size = (800, 480)

Window.clearcolor = (0, 0, 0, 0)

class Uygulama(App):
    def tusaBasildi(self, *args):

        keyboard = Window.request_keyboard(self,input_type='number')

        if keyboard.widget:
            vkeyboard = self._keyboard.widget
            vkeyboard.layout = 'numeric.json'

#
#
    def build(self, *args):
         self.title = u"Otomat Sayacı"

    kv = '''
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            Label:
                id: "durum"
                text: "Makine Durumu:"
                size_hint_x: 1
            Button:
                id: "durumbuton"
                color: (0, 1, 0, 1)
                size_hint_x: 2
                text: "Çalışıyorrr"


        BoxLayout:
            Label:
                id: "yapilantext"
                text: "Yaılan İş:"
                size_hint_x: 1
            TextInput:
                id: "yapilan"
                size_hint_x: 2
                color: (0, 0, 0, 1)


        BoxLayout:
            Label:
                id: "cevrimsuresitext"
                text: "Çevrim Süresi:"
                size_hint_x: 1
            Button:
                id: "cevrimsuresi"
                size_hint_x: 2
        BoxLayout:
            Label:
                id: "isinaditext"
                text: "İşin Adı:"
                size_hint_x: 1
            TextInput:
                id: "isinadi"
                size_hint_x: 2

    '''

    GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=self.tusaBasildi1, bouncetime=50)
#    return Demo()
#    return Ekran



Uygulama().run()