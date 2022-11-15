import socket
from os import path
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
import tkinter as tk

def camera_(height_, camera_id = "", camera_link = "", camera_name = ""):
    main_screen = f"""
<CameraSettings_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label: 
            text: "      Current objects list:"
            size: "160", 0
            pos: "40", {height_- 30}
            font_size: 30


        Label:
            text: "Activity level: 4/10"
            size: "135", "30"
            pos: "10", {66}

        Label:
            text: "IP: http://192.168.0.1:8080/"
            size: "135", "36"
            pos: "38", {40}
        
        Button:
            text: "Analyze"
            size: "140", "34"
            pos: "10", "10"
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.exit_screen()
        Button:
            text: "Report"
            size: "140", "34"
            pos: "160", "10"
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""
    
    result = main_screen

    return result

class ScreenSettings:
    def __init__(self):
        self.root = tk.Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
    
    def width(self):
        return self.screen_width
    
    def height(self):
        return self.screen_height
    
    def size(self):
        return self.screen_width, self.screen_height

scr = ScreenSettings()

width_ = scr.width() // 12 * 2
height_ = scr.height() // 8 * 2

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', str(width_))
Config.set('graphics', 'height', str(height_))
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

file_path_list = path.abspath(__file__)
k, file_path = "\ ", ""
file_path_list = file_path_list.split(k[0])
for n in file_path_list[0: len(file_path) - 2]:
    file_path += (n + k[0])

default_camera_id = 'Camera 1'
default_camera_name = 'Main camera'

info = ["", "", ""]

try:
    sock = socket.socket()
    sock.connect(('localhost', 5001))
except:
    pass

Builder.load_string(camera_(camera_id = info[0], camera_link = info[1], camera_name = info[2], height_ = height_))

def open_help(key = None):
    pass

class CameraSettings_Screen(Screen):
    def __init__(self, **kwargs):
        super(CameraSettings_Screen, self).__init__(**kwargs)
    def exit_screen(self):
        exit()
    def help(self):
        open_help()
    def update_data(self):
        pass
    def get_data(self):
        pass

sm = ScreenManager(transition = NoTransition())
sm.add_widget(CameraSettings_Screen(name = 'camera_settings'))

class InformationApp(App):
    def build(self):
        global sm
        return sm

InformationApp().run()