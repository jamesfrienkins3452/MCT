import socket
import threading
from os import path, getenv, getlogin
from webbrowser import open as webbrowser_open
from graphic.data.database import Database
from internet.check_connection import Connection_status
from internet.check_speed import Connection_speed
from graphic.design import main
from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from graphic.screen import ScreenSettings
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from subprocess import Popen, PIPE
from functions.install import setup as setup_i
from functions.repair import setup as setup_r
from functions.uninstall import setup as setup_u

width_, height_ = ScreenSettings().width() // 5 * 2, ScreenSettings().height() // 5 * 2

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', str(width_))
Config.set('graphics', 'height', str(height_))
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

_, file_path = "\ ", ""
for n in path.abspath(__file__).split(_[0])[0: len(file_path) - 1]:
    file_path += (n + _[0])

Builder.load_string(main(height_, width_))

data = [['', '', ''], [getenv('APPDATA')[0:len(getenv('APPDATA')) - 8] + '\\Local', f'C:\\Users\\{getlogin()}\\Documents', f'C:\\Users\\{getlogin()}\\Documents']]

def serv_c():
    while True:
        sock_c = socket.socket()
        sock_c.bind(('', 5001))
        sock_c.listen(1)
        conn_c, _ = sock_c.accept()
        while True:
            try:
                info_c = conn_c.recv(1024).decode()
                if info_c == '':
                    break
                data[0] = info_c.split('|')
            except:
                pass

def serv_l():
    while True:
        sock_l = socket.socket()
        sock_l.bind(('', 5002))
        sock_l.listen(1)
        conn_l, _ = sock_l.accept()
        while True:
            try:
                info_l = conn_l.recv(1024).decode()
                if info_l == '':
                    break
                data[1] = info_l.split('|')
            except:
                pass

serv_c_t = threading.Thread(target = serv_c, daemon = True).start()
serv_c_l = threading.Thread(target = serv_l, daemon = True).start()

def open_help(key = None):
    if key == None:
        webbrowser_open('https://github.com/jamesfrienkins3452/MCT')

def run_script(file):
    Popen(['python', file], stdout = PIPE, stderr = PIPE)

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
    def check_connectioni_status(self):
        if Connection_status().status() == True:
            cn_speed = round(Connection_speed().download() / 1048576, 2)
            if self.manager.current == "checkingconnectioni_screen":
                self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.text = f"Connection status: Okay ({cn_speed} mb/sec)"
                self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.pos = 37, height_- 80
                self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_Continue.disabled = False
        else:
            if self.manager.current == "checkingconnectioni_screen":
                self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.text = f"Connection status: No connection"
                self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.pos = 20, height_- 80
    def install(self):
        threading.Thread(target = self.check_connectioni_status, daemon = True).start()
    def back(self):
        pass
    def help(self):
        open_help()

class CheckingConnectionI_Screen(Screen):
    def __init__(self, **kwargs):
        super(CheckingConnectionI_Screen, self).__init__(**kwargs)
    def continue_installation(self):
        self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.text = f"Connection status: Unknown"
        self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.pos = 0, height_- 80
        self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_Continue.disabled = True
    def back(self):
        self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.text = f"Connection status: Unknown"
        self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.pos = 0, height_- 80
        self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_Continue.disabled = True
    def help(self):
        open_help()

class InstallationSettings_Screen(Screen):
    def __init__(self, **kwargs):
        super(InstallationSettings_Screen, self).__init__(**kwargs)
        db = Database('', 'graphic\\data\\st-location.db' , k = True)
        dt = db.read_table('location')
        data[1][0] = dt[0][1]        
        data[1][1] = dt[1][1]
        data[1][2] = dt[2][1]

    def update_labels(self):
        if data[0][0] != '' and data[0][1] != '' and data[0][2] != '':
            self.manager.get_screen("installationsettings_screen").ids.camera_label.color = (1, 1, 1, 0)
            self.manager.get_screen("installationsettings_screen").ids.InstallationSettings_Screen_Continue.disabled = False
            self.manager.get_screen("installationsettings_screen").ids.InstallationSettings_Screen_Camera.disabled = True
            self.manager.get_screen("installationsettings_screen").ids.InstallationSettings_Screen_Location.disabled = True
        else:
            self.manager.get_screen("installationsettings_screen").ids.camera_label.color = (1, 1, 1, 1)
            self.manager.get_screen("installationsettings_screen").ids.InstallationSettings_Screen_Continue.disabled = True
            self.manager.get_screen("installationsettings_screen").ids.InstallationSettings_Screen_Camera.disabled = False
            self.manager.get_screen("installationsettings_screen").ids.InstallationSettings_Screen_Location.disabled = False

    def check_connection_status(self):        
        if Connection_status().status() == True:
            cn_speed = round(Connection_speed().download() / 1048576, 2)
            if self.manager.current == "checkingconnectioni_screen":
                self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.text = f"Connection status: Okay ({cn_speed} mb/sec)"
                self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.pos = 37, height_- 80
                self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_Continue.disabled = False
        else:
            if self.manager.current == "checkingconnectioni_screen":
                self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.text = f"Connection status: No connection"
                self.manager.get_screen("checkingconnectioni_screen").ids.CheckingConnectionI_Screen_ConnectionStatus.pos = 20, height_- 80
    def continue_installation(self):
        pass
    def camera(self):
        run_script('graphic/camera.py')
    def location(self):
        run_script('graphic/location.py')
    def back(self):
        self.manager.get_screen("installationsettings_screen").ids.InstallationSettings_Screen_Camera.disabled = False
        self.manager.get_screen("installationsettings_screen").ids.InstallationSettings_Screen_Location.disabled = False
        threading.Thread(target = self.check_connection_status, daemon = True).start()
    def help(self):
        open_help()

class InstallationProcess_Screen(Screen):
    def __init__(self, **kwargs):
        super(InstallationProcess_Screen, self).__init__(**kwargs)
    def install(self):
        install_key = setup_i(data[0], program_location = data[1][0], data_location = data[1][1], logs_location = data[1][2])
        self.manager.get_screen("installationprocess_screen").ids.InstallationProccess_Screen_Back.disabled = True
        self.manager.get_screen("installationprocess_screen").ids.InstallationProcess_Screen_Install.disabled = True
        self.manager.get_screen("installationprocess_screen").ids.InstallationProcess_Screen_Continue.disabled = False
        if install_key == "successfully":
            self.manager.get_screen("installationfinished_screen").ids.InstallationFinished_Screen_Label.size = (str(448), "0")
        else:
            self.manager.get_screen("installationfinished_screen").ids.InstallationFinished_Screen_Label.size = (str(482), "0")
        self.manager.get_screen("installationfinished_screen").ids.InstallationFinished_Screen_Label.text = f"Installation finished {install_key}"
    def continue_installation(self):
        pass
    def back(self):
        pass
    def help(self):
        open_help()

class InstallationFinished_Screen(Screen):
    def __init__(self, **kwargs):
        super(InstallationFinished_Screen, self).__init__(**kwargs)
    def finish(key):
        exit()
    def help(self):
        open_help()

class Repair_Screen(Screen):
    def __init__(self, **kwargs):
        super(Repair_Screen, self).__init__(**kwargs)
    def check_connectionr_status(self):
        if Connection_status().status() == True:
            cn_speed_ = round(Connection_speed().download() / 1048576, 2)
            if self.manager.current == "checkingconnectionr_screen":
                self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.text = f"Connection status: Okay ({cn_speed_} mb/sec)"
                self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.pos = 37, height_- 80
                self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_Continue.disabled = False
        else:
            if self.manager.current == "checkingconnectionr_screen":
                self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.text = f"Connection status: No connection"
                self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.pos = 20, height_- 80
    def repair(self):
        threading.Thread(target = self.check_connectionr_status, daemon = True).start()
    def back(self):
        pass
    def help(self):
        open_help()

class CheckingConnectionR_Screen(Screen):
    def __init__(self, **kwargs):
        super(CheckingConnectionR_Screen, self).__init__(**kwargs)
    def continue_repairing(self):
        self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.text = f"Connection status: Unknown"
        self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.pos = 0, height_- 80
        self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_Continue.disabled = True
    def back(self):
        self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.text = f"Connection status: Unknown"
        self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.pos = 0, height_- 80
        self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_Continue.disabled = True
    def help(self):
        open_help()

class RepairProccess_Screen(Screen):
    def __init__(self, **kwargs):
        super(RepairProccess_Screen, self).__init__(**kwargs)
    def check_connection_status(self):
        if Connection_status().status() == True:
            cn_speed = round(Connection_speed().download() / 1048576, 2)
            if self.manager.current == "checkingconnectionr_screen":
                self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.text = f"Connection status: Okay ({cn_speed} mb/sec)"
                self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.pos = 37, height_- 80
                self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_Continue.disabled = False
        else:
            if self.manager.current == "checkingconnectionr_screen":
                self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.text = f"Connection status: No connection"
                self.manager.get_screen("checkingconnectionr_screen").ids.CheckingConnectionR_Screen_ConnectionStatus.pos = 20, height_- 80
    def repair(self):
        repair_key = setup_r()
        self.manager.get_screen("repairproccess_screen").ids.RepairProccess_Screen_Back.disabled = True
        self.manager.get_screen("repairproccess_screen").ids.RepairProccess_Screen_Repair.disabled = True
        self.manager.get_screen("repairproccess_screen").ids.RepairProccess_Screen_Continue.disabled = False
        if repair_key == "successfully":
            self.manager.get_screen("repairproccessfinished_screen").ids.RepairProccessFinished_Screen_Label.size = (str(388), "0")
        else:
            self.manager.get_screen("repairproccessfinished_screen").ids.RepairProccessFinished_Screen_Label.size = (str(422), "0")
        self.manager.get_screen("repairproccessfinished_screen").ids.RepairProccessFinished_Screen_Label.text = f"Repair finished {repair_key}"
    def continue_reparing(self):
        pass
    def back(self):
        threading.Thread(target = self.check_connection_status, daemon = True).start()
    def help(self):
        open_help()

class RepairProccessFinished_Screen(Screen):
    def __init__(self, **kwargs):
        super(RepairProccessFinished_Screen, self).__init__(**kwargs)
    def finish(key):
        exit()
    def help(self):
            open_help()

class Uninstallation_Screen(Screen):
    def __init__(self, **kwargs):
        super(Uninstallation_Screen, self).__init__(**kwargs)
    def uninstall(self):
        pass
    def back(self):
        pass
    def help(self):
        open_help()

class UninstallationProccess_Screen(Screen):
    def __init__(self, **kwargs):
        super(UninstallationProccess_Screen, self).__init__(**kwargs)
    def uninstall(self):
        uninstall_key = setup_u()
        self.manager.get_screen("uninstallationproccess_screen").ids.UninstallationProccess_Screen_Back.disabled = True
        self.manager.get_screen("uninstallationproccess_screen").ids.UninstallationProcess_Screen_Uninstall.disabled = True
        self.manager.get_screen("uninstallationproccess_screen").ids.UninstallationProcess_Screen_Continue.disabled = False
        if uninstall_key == "successfully":
            self.manager.get_screen("uninstallationprocessfinished_Screen").ids.UninstallationFinished_Screen_Label.size = (str(425), "0")
        else:
            self.manager.get_screen("uninstallationprocessfinished_Screen").ids.UninstallationFinished_Screen_Label.size = (str(445), "0")
        self.manager.get_screen("uninstallationprocessfinished_Screen").ids.UninstallationFinished_Screen_Label.text = f"Uninstall finished {uninstall_key}"
    def continue_uninstalling(self):
        pass
    def back(self):
        pass
    def help(self):
        open_help()

class UninstallationProcessFinished_Screen(Screen):
    def __init__(self, **kwargs):
        super(UninstallationProcessFinished_Screen, self).__init__(**kwargs)
    def finish(key):
        exit()
    def help(self):
            open_help()

sm = ScreenManager(transition = NoTransition())

sm.add_widget(Setup_Screen(name = 'setup_screen'))
sm.add_widget(Repair_Screen(name = 'repair_screen'))
sm.add_widget(Installation_Screen(name = 'installation_screen'))
sm.add_widget(Uninstallation_Screen(name = 'uninstallation_screen'))
sm.add_widget(RepairProccess_Screen(name = 'repairproccess_screen'))
sm.add_widget(CheckingConnectionI_Screen(name = 'checkingconnectioni_screen'))
sm.add_widget(CheckingConnectionR_Screen(name = 'checkingconnectionr_screen'))
sm.add_widget(InstallationProcess_Screen(name = 'installationprocess_screen'))
sm.add_widget(InstallationSettings_Screen(name = 'installationsettings_screen'))
sm.add_widget(InstallationFinished_Screen(name = 'installationfinished_screen'))
sm.add_widget(RepairProccessFinished_Screen(name = 'repairproccessfinished_screen'))
sm.add_widget(UninstallationProccess_Screen(name = 'uninstallationproccess_screen'))
sm.add_widget(UninstallationProcessFinished_Screen(name = 'uninstallationprocessfinished_Screen'))

class InstallerApp(App):
    def build(self):
        global sm
        return sm

InstallerApp().run()