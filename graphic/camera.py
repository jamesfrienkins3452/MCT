import socket
from os import path
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from screen import ScreenSettings
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from design import camera_
from webbrowser import open as webbrowser_open
from data.database import Database

scr = ScreenSettings()

width_ = scr.width() // 9 * 2
height_ = scr.height() // 6 * 2

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

if not path.exists(file_path + '/graphic/data/st-camera.db'):
    db = Database('st-camera')
    db.new_table('camera', [('type', 'text', 'PRIMARY KEY'), ('information', 'text', '')])
    db.add_data('camera', ('Camera id', default_camera_id))
    db.add_data('camera', ('Camera link', ''))
    db.add_data('camera', ('Camera name', default_camera_name))
else:
    db = Database('st-camera')

info = ["", "", ""]

try:
    sock = socket.socket()
    sock.connect(('localhost', 5001))
except:
    pass

Builder.load_string(camera_(camera_id = info[0], camera_link = info[1], camera_name = info[2], height_ = height_))

def open_help(key = None):
    if key == None:
        webbrowser_open('https://github.com/jamesfrienkins3452/MCT')

class CameraSettings_Screen(Screen):
    def __init__(self, **kwargs):
        super(CameraSettings_Screen, self).__init__(**kwargs)
        dt = db.read_table('camera')
        if dt != []:
            self.ids['camera_id'].text = dt[0][1]
            self.ids['camera_link'].text = dt[1][1]
            self.ids['camera_name'].text = dt[2][1]
    def exit_screen(self):
        exit()
    def help(self):
        open_help()
    def update_data(self):
        self.camera_id = self.ids['camera_id'].text
        self.camera_link = self.ids['camera_link'].text
        self.camera_name = self.ids['camera_name'].text
        db.edit_data('camera',  ('type', self.camera_id), 'type', 'Camera id')
        db.edit_data('camera',  ('type', self.camera_link), 'type', 'Camera link')
        db.edit_data('camera',  ('type', self.camera_name), 'type', 'Camera name')
        dt = self.camera_id + '|' + self.camera_link + '|' + self.camera_name
        sock.send(str.encode(dt))
    def get_data(self):
        return db.read_table()

sm = ScreenManager(transition = NoTransition())
sm.add_widget(CameraSettings_Screen(name = 'camera_settings'))

class SettingsApp(App):
    def build(self):
        global sm
        return sm

SettingsApp().run()