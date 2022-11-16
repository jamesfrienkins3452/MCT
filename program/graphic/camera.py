import cv2
import socket
import threading
from video.detector import recognize_image
from os import path, getenv
from webbrowser import open as webbrowser_open
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from data.database import Database
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from video.translator import Camera
import tkinter as tk

__data__ = []

settings_location = getenv('APPDATA')[0:len(getenv('APPDATA')) - 8] + '\\Local'

def read_default_settings():
    db = Database('installation settings', settings_location + '\\MCT', k = True)
    dt = db.read_table('location')
    f = []
    for i in dt:
        f.append(i[1])
    return f

program_location, recordings_location, logs_location = read_default_settings()

cameraSettingDB = Database('camera settings', program_location + "\\MCT\\system files\\data")
cameraList = cameraSettingDB.read_table('camera_list')

for cameraInfo in cameraList:
    a1, a2, a3 = cameraSettingDB.read_table(cameraInfo[1])
    __data__.append([a1[1], a2[1], a3[1]])
    print(a1, a2, a3)

def camera_(height_, camera_id = "", camera_link = "", camera_name = "", data = __data__):
    main_screen = f"""
<CameraSettings_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label: 
            text: "       Current camera list:"
            size: "160", 0
            pos: "40", {height_- 30}
            font_size: 30

        Label:
            text: "Name:"
            size: "0", "0"
            pos: "55", {height_- 85}
            font_size: 20

        Label:
            text: "ID:"
            size: "0", "0"
            pos: "200", {height_- 85}
            font_size: 20

        Label:
            text: "IP:"
            size: "0", "0"
            pos: "377", {height_- 85}
            font_size: 20

        Label:
            text: "{data[0][0]}"
            size: "0", "0"
            pos: "68", {height_- 130}
            font_size: 20

        Label:
            text: "{data[0][1]}"
            size: "0", "0"
            pos: "450", {height_- 130}
            font_size: 20

        Label:
            text: "{data[0][2]}"
            size: "0", "0"
            pos: "245", {height_- 130}
            font_size: 20

        Button:
            text: "View"
            size: "100", "34"
            pos: "650", {height_- 145}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.cam_1_start()

        Button:
            text: "Close"
            size: "100", "34"
            pos: "780", {height_- 145}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.cam_1_end()

        Button:
            text: "Analyse"
            size: "140", "34"
            pos: "10", "10"
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.analyse()
        Button:
            text: "Exit"
            size: "140", "34"
            pos: "160", "10"
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.exit_screen()

        Button:
            text: "Help"
            size: "140", "34"
            pos: "650", {10}
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

width_ = scr.width() // 12 * 6
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

Builder.load_string(camera_(camera_id = info[0], camera_link = info[1], camera_name = info[2], height_ = height_))

def open_help(key = None):
    if key == None:
        webbrowser_open('https://github.com/jamesfrienkins3452/MCT')

class CameraSettings_Screen(Screen):
    def __init__(self, **kwargs):
        super(CameraSettings_Screen, self).__init__(**kwargs)

        self.cam_1_thread = True

    def cam_1_start(self):
        self.cam_1_thread = True
        if self.cam_1_thread:
            threading.Thread(target = self.cam_1_start_, daemon = True).start()
    
    def cam_1_start_(self):
        self.cam_1_img = Camera(a2[1])
        self.cam_1_img.connect()
        while self.cam_1_thread:
            cv2.imshow(a1[1], recognize_image(self.cam_1_img.reshape(self.cam_1_img.frame())))
            cv2.waitKey(5)
        cv2.destroyWindow(a1[1])

    def cam_1_end(self):
        self.cam_1_thread = False

    def analyse(self):
        pass

    def exit_screen(self):
        exit()

    def help(self):
        open_help()

sm = ScreenManager(transition = NoTransition())
sm.add_widget(CameraSettings_Screen(name = 'camera_settings'))

class InformationApp(App):
    def build(self):
        global sm
        return sm

InformationApp().run()