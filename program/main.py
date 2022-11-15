import threading
import socket
from os import path, getenv, getlogin, system
from graphic.data.database import Database
from graphic.design import main
from webbrowser import open as webbrowser_open
from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from graphic.screen import ScreenSettings

settings_location = getenv('APPDATA')[0:len(getenv('APPDATA')) - 8] + '\\Local'

width_, height_ = ScreenSettings().width() // 5 * 2, ScreenSettings().height() // 5 * 2

_, file_path = "\ ", ""

for n in path.abspath(__file__).split(_[0])[0: len(file_path) - 1]:
    file_path += (n + _[0])

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', str(width_))
Config.set('graphics', 'height', str(height_))
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

Builder.load_string(main(height_, width_))

def read_default_settings():
    db = Database('installation settings', settings_location + '\\MCT', k = True)
    dt = db.read_table('location')
    f = []
    for i in dt:
        f.append(i[1])
    return f

def open_help(key = None):
    if key == None:
        webbrowser_open('https://github.com/jamesfrienkins3452/MCT')

def run_script(file):
    def run_script_(file):
        system(f'python {file}')
    rs = threading.Thread(target = run_script_, args = (file, ), daemon = True)
    rs.start()

class Main_Screen(Screen):
    def __init__(self, **kwargs):
        super(Main_Screen, self).__init__(**kwargs)

        self.program_location, self.recordings_location, self.logs_location = read_default_settings()

        self.cameraSettingDB = Database('camera settings', self.program_location + "\\MCT\\system files\\data")
        self.cameraList = self.cameraSettingDB.read_table('camera_list')

        print('KEY 1', self.program_location, self.recordings_location, self.logs_location)        
        print('KEY 2', self.cameraList, self.cameraSettingDB.table_list)

        for data in self.cameraList:
            print(self.cameraSettingDB.read_table(data[1]))

    def system_files(self):
        system("start " + self.program_location + "\\MCT")

    def camera(self):
        run_script('graphic/camera.py')

    def logs(self):
        system("start " + self.logs_location + "\\MCT\\logs")

    def recordings(self):
        system(f"start " + self.recordings_location + "\\MCT\\recordings")

    def help(self):
        open_help()

    def exit(self):
        exit()

sm = ScreenManager(transition = NoTransition())
sm.add_widget(Main_Screen(name = 'setup_screen'))

class MCTApp(App):
    def build(self):
        global sm
        return sm

MCTApp().run()