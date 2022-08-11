import socket
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from screen import ScreenSettings
from os import path, getenv, getlogin
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from design import locations_
from webbrowser import open as webbrowser_open
from data.database import Database

scr = ScreenSettings()

width_ = scr.width() // 2
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

default_settings_location = getenv('APPDATA')[0:len(getenv('APPDATA')) - 8] + '\\Local'
default_data_location = f'C:\\Users\\{getlogin()}\\Documents'
default_logs_location = f'C:\\Users\\{getlogin()}\\Documents'

if not path.exists(file_path + '/graphic/data/st-location.db'):
    db = Database('st-location')
    db.new_table('location', [('type', 'text', 'PRIMARY KEY'), ('location', 'text', '')])
    db.add_data('location', ('Program location', default_settings_location))
    db.add_data('location', ('Files location', default_data_location))
    db.add_data('location', ('Log location', default_logs_location))
else:
    db = Database('st-location')

info = ["" , "", ""]

try:
    sock = socket.socket()
    sock.connect(('localhost', 5002))
except:
    pass

Builder.load_string(locations_(program_location = info[0], files_location = info[1], logs_location = info[2], height_ = height_))

def open_help(key = None):
    if key == None:
        webbrowser_open('https://github.com/jamesfrienkins3452/MCT')

class LocationsSettings_Screen(Screen):
    def __init__(self, **kwargs):
        super(LocationsSettings_Screen, self).__init__(**kwargs)
        if info[0] != "":
            self.ids['program_location_label'].color = (1, 1, 1, 0)
        if info[1] != "":
            self.ids['files_location_label'].color = (1, 1, 1, 0)
        if info[2] != "":
            self.ids['logs_location_label'].color = (1, 1, 1, 0)
        dt = db.read_table('location')
        self.ids['program_location'].text = dt[0][1]
        self.ids['files_location'].text = dt[1][1]
        self.ids['logs_location'].text = dt[2][1]

    def exit_screen(self):
        exit()

    def help(self):
        open_help()

    def update_data(self):
        self.program_location = self.ids['program_location'].text
        self.files_location = self.ids['files_location'].text
        self.logs_location = self.ids['logs_location'].text

        if path.isdir(self.program_location) == False:
            self.program_location = ""
            self.ids['program_location_label'].color = (1, 1, 1, 1)
            db.edit_data('location',  ('type', default_settings_location), 'type', 'Program location')
        else:
            self.ids['program_location_label'].color = (1, 1, 1, 0)
            db.edit_data('location',  ('type', self.program_location), 'type', 'Program location')

        if path.isdir(self.files_location) == False:
            self.files_location = ""
            self.ids['files_location_label'].color = (1, 1, 1, 1)
            db.edit_data('location',  ('type', default_data_location), 'type', 'Files location')
        else:
            self.ids['files_location_label'].color = (1, 1, 1, 0)
            db.edit_data('location',  ('type', self.files_location), 'type', 'Files location')

        if path.isdir(self.logs_location) == False:
            self.logs_location = ""
            self.ids['logs_location_label'].color = (1, 1, 1, 1)
            db.edit_data('location',  ('type', default_logs_location), 'type', 'Log location')
        else:
            self.ids['logs_location_label'].color = (1, 1, 1, 0)
            db.edit_data('location',  ('type', self.logs_location), 'type', 'Log location')

        dt = self.program_location + '|' + self.files_location + '|' + self.logs_location
        sock.send(str.encode(dt))

    def get_data(self):
        return db.read_table()
sm = ScreenManager(transition = NoTransition())
sm.add_widget(LocationsSettings_Screen(name = 'locationssettings_screen'))

class SettingsApp(App):
    def build(self):
        global sm
        return sm

SettingsApp().run()