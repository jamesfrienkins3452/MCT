import time
import threading
from webbrowser import open as webbrowser_open
from internet.check_connection import Connection_status
from internet.check_speed import Connection_speed
from video.camera import Camera
from graphic.design import design
from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from graphic.screen import ScreenSettings
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

scr = ScreenSettings()

width_ = scr.width() // 5 * 2
height_ = scr.height() // 5 * 2

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', str(width_))
Config.set('graphics', 'height', str(height_))

Builder.load_string(design(height_))

dataset = {"timenow" : 0}

def open_help(key = None):
    if key == None:
        webbrowser_open('https://github.com/')

class Setup_Screen(Screen):
    def __init__(self, **kwargs):
        super(Setup_Screen, self).__init__(**kwargs)
    def install(self):
        pass
    def repair(self):
        pass
    def uninstall(self):
        pass
    def help(self):
        open_help()

class Installation_Screen(Screen): 
    def __init__(self, **kwargs):
        super(Installation_Screen, self).__init__(**kwargs)

    def check_connection_status(self):        
        cs = Connection_status()
        cn_status = cs.status()
        if cn_status == True:
            cn = Connection_speed()
            cn_speed = round(cn.download() / 1048576, 2)

            self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.text = f"Connection status: Okay ({cn_speed} mb/sec)"
            self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.pos = 37, height_- 80
            self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_Continue.disabled = False
        else:
            self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.text = f"Connection status: No connection"
            self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.pos = 20, height_- 80
  
    def install(self):
        dataset['timenow'] = time.time()
        ccs = threading.Thread(target = self.check_connection_status, daemon = True)
        ccs.start()

    def back(self):
        pass

    def help(self):
        open_help()

class CheckingConnection_Screen(Screen): 
    def continue_installation(self):
        self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.text = f"Connection status: Unknown"
        self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.pos = 0, height_- 80
        self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_Continue.disabled = True
    
    def back(self):
        self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.text = f"Connection status: Unknown"
        self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.pos = 0, height_- 80
        self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_Continue.disabled = True
    def help(self):
        open_help()

class InstallationSettings_Screen(Screen): 
    def check_connection_status(self):        
        cs = Connection_status()
        cn_status = cs.status()
        if cn_status == True:
            cn = Connection_speed()
            cn_speed = round(cn.download() / 1048576, 2)

            self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.text = f"Connection status: Okay ({cn_speed} mb/sec)"
            self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.pos = 37, height_- 80
            self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_Continue.disabled = False
        else:
            self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.text = f"Connection status: No connection"
            self.manager.get_screen("checkingconnection_screen").ids.CheckingConnection_Screen_ConnectionStatus.pos = 20, height_- 80
  
    def back(self):
        dataset['timenow'] = time.time()
        ccs = threading.Thread(target = self.check_connection_status, daemon = True)
        ccs.start()
    def help(self):
        open_help()

class InstallationProcess_Screen(Screen): 
    def build(self):
        pass

class InstallationFinished_Screen(Screen): 
    def build(self):
        pass

sm = ScreenManager(transition=NoTransition())

sm.add_widget(Setup_Screen(name = 'setup_screen'))
sm.add_widget(Installation_Screen(name = 'installation_screen'))
sm.add_widget(CheckingConnection_Screen(name = 'checkingconnection_screen'))
sm.add_widget(InstallationSettings_Screen(name = 'installationsettings_screen'))
sm.add_widget(InstallationProcess_Screen(name = 'installationprocess_screen'))
sm.add_widget(InstallationFinished_Screen(name = 'installationfinished_screen'))


class InstallerApp(App):

    def build(self):
        global sm
        return sm


InstallerApp().run()
