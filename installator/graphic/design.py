def main(height_, width_, connection_status = "Unknown", repair_key = "successfully", install_key = "successfully"):
    setup_screen = f"""
<Setup_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Welcome to MCT installator!"
            size: "397", 0
            pos: "0", {height_- 30}
            font_size: 30
        Button:
            text: "Install"
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'installation_screen'
                root.install()
        Button:
            text: "Repair"
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'repair_screen'
                root.repair()
        Button:
            text: "Uninstall"
            size: "140", "40"
            pos: "10", {height_ - 200}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'uninstallation_screen'
                root.uninstall()
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    installation_screen = f"""
<Installation_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Installation"
            size: "170", 0
            pos: "0", {height_- 30}
            font_size: 30
        Button:
            text: "Install"
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'checkingconnectioni_screen'
                root.install()
        Button:
            text: "Back"
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'setup_screen'
                root.back()
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    checkingConnectionI_screen = f"""
<CheckingConnectionI_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Preparation for installing"
            size: "347", 0
            pos: "0", {height_- 30}
            font_size: 30
        Label:
            text: "Connection status: {connection_status}"
            id: CheckingConnectionI_Screen_ConnectionStatus
            size: "220", 0
            pos: "0", {height_- 80}
            font_size: 15
        Button:
            text: "Continue"
            id: CheckingConnectionI_Screen_Continue
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'installationsettings_screen'
                root.continue_installation()
            disabled: True
        Button:
            text: "Back"
            id: CheckingConnectionI_Screen_Back
            size: "140", "40"
            pos: "10", {height_ - 200}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'installation_screen'
                root.back()
            disabled: False
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    installationSettings_screen = f"""
<InstallationSettings_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Setting up"
            size: "157", 0
            pos: "0", {height_- 30}
            font_size: 30
        Label:
            text: "Settings:"
            size: "150", 0
            pos: "175", {height_- 30}
            font_size: 30
        Button:
            text: "Camera"
            id: InstallationSettings_Screen_Camera
            size: "140", "40"
            pos: "190", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.camera()
        Label:
            id: camera_label
            text: "Camera isn't configured"
            size: "155", "30"
            pos: "345", {height_ - 105}
            color: 1, 1, 1, 1
        Button:
            text: "Location"
            id: InstallationSettings_Screen_Location
            size: "140", "40"
            pos: "190", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.location()
        Button:
            id: InstallationSettings_Screen_Continue
            text: "Continue"
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'installationprocess_screen'
                root.continue_installation()
            disabled: True
        Button:
            text: "Update"
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.update_labels()
        Button:
            text: "Back"
            size: "140", "40"
            pos: "10", {height_ - 200}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'checkingconnectioni_screen'
                root.back()
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    installationProccess_screen = f"""
<InstallationProcess_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Ready for installing"
            size: "270", 0
            pos: "0", {height_- 30}
            font_size: 30
        Button:
            text: "Install"
            id: InstallationProcess_Screen_Install
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.install()
        Button:
            text: "Continue"
            id: InstallationProcess_Screen_Continue
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'installationfinished_screen'
                root.continue_installation()
            disabled: True
        Button:
            text: "Back"
            id: InstallationProccess_Screen_Back
            size: "140", "40"
            pos: "10", {height_ - 200}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'installationsettings_screen'
                root.back()
            disabled: False
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    installationFinished_screen = f"""
<InstallationFinished_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Installation finished {install_key}"
            id: InstallationFinished_Screen_Label
            size: "0", 0
            pos: "0", {height_- 30}
            font_size: 30
        Button:
            text: "Finish"
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.finish()
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    repair_screen = f"""
<Repair_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Repair"
            size: "102", 0
            pos: "0", {height_- 30}
            font_size: 30
        Button:
            text: "Repair"
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'checkingconnectionr_screen'
                root.repair()
        Button:
            text: "Back"
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'setup_screen'
                root.back()
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    checkingConnectionR_screen = f"""
<CheckingConnectionR_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Preparation for repairing"
            size: "340", 0
            pos: "0", {height_- 30}
            font_size: 30
        Label:
            text: "Connection status: {connection_status}"
            id: CheckingConnectionR_Screen_ConnectionStatus
            size: "220", 0
            pos: "0", {height_- 80}
            font_size: 15
        Button:
            text: "Continue"
            id: CheckingConnectionR_Screen_Continue
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'repairproccess_screen'
                root.continue_repairing()
            disabled: True
        Button:
            text: "Back"
            id: CheckingConnectionR_Screen_Back
            size: "140", "40"
            pos: "10", {height_ - 200}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'repair_screen'
                root.back()
            disabled: False
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    repairProccess_screen = f"""
<RepairProccess_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Ready for reparing"
            size: "260", 0
            pos: "0", {height_- 30}
            font_size: 30
        Button:
            text: "Repair"
            id: RepairProccess_Screen_Repair
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.repair()
        Button:
            text: "Continue"
            id: RepairProccess_Screen_Continue
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'repairproccessfinished_screen'
                root.continue_reparing()
            disabled: True
        Button:
            text: "Back"
            id: RepairProccess_Screen_Back
            size: "140", "40"
            pos: "10", {height_ - 200}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'checkingconnectionr_screen'
                root.back()
            disabled: False
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""
    
    repairProccessFinished_screen = f"""
<RepairProccessFinished_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Repair finished {repair_key}"
            id: RepairProccessFinished_Screen_Label
            size: "0", 0
            pos: "0", {height_- 30}
            font_size: 30
        Button:
            text: "Finish"
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.finish()
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    uninstalllation_screen = f"""
<Uninstallation_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Uninstallation"
            size: "205", 0
            pos: "0", {height_- 30}
            font_size: 30
        Button:
            text: "Uninstall"
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'uninstallationproccess_screen'
                root.uninstall()
        Button:
            text: "Back"
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'setup_screen'
                root.back()
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""
    
    uninstallationProccess_screen = f"""
<UninstallationProccess_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Ready for Uninstalling"
            size: "310", 0
            pos: "0", {height_- 30}
            font_size: 30
        Button:
            text: "Uninstall"
            id: UninstallationProcess_Screen_Uninstall
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.uninstall()
        Button:
            text: "Continue"
            id: UninstallationProcess_Screen_Continue
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'uninstallationprocessfinished_Screen'
                root.continue_uninstalling()
            disabled: True
        Button:
            text: "Back"
            id: UninstallationProccess_Screen_Back
            size: "140", "40"
            pos: "10", {height_ - 200}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'uninstallation_screen'
                root.back()
            disabled: False
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    uninstallationProccessFinished_screen = f"""
<UninstallationProcessFinished_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Uninstallation finished {install_key}"
            id: UninstallationFinished_Screen_Label
            size: "0", 0
            pos: "0", {height_- 30}
            font_size: 30
        Button:
            text: "Finish"
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.finish()
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""

    result = setup_screen + installation_screen + checkingConnectionI_screen + installationSettings_screen + repair_screen + checkingConnectionR_screen + repairProccess_screen + repairProccessFinished_screen + installationProccess_screen + installationFinished_screen + uninstalllation_screen + uninstallationProccess_screen + uninstallationProccessFinished_screen

    return result

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
            text: "Camera settings:"
            size: "160", 0
            pos: "40", {height_- 30}
            font_size: 30
        Label:
            text: "Camera id:"
            size: "110", "30"
            pos: "0", {height_ - 100}
        Label:
            text: "Camera link:"
            size: "121", "30"
            pos: "0", {height_ - 150}
        Label:
            text: "Camera name:"
            size: "135", "30"
            pos: "0", {height_ - 200}
        TextInput:
            id: camera_id
            hint_text: "camera_id"
            text: "{camera_id}"
            size: "155", "30"
            pos: "150", {height_ - 100}
            on_text: root.update_data()
        TextInput:
            id: camera_link
            text: "{camera_link}"
            hint_text: "camera_link"
            size: "155", "30"
            pos: "150", {height_ - 150}
            on_text: root.update_data()
        TextInput:
            id: camera_name
            text: "{camera_name}"
            hint_text: "camera_name"
            size: "155", "30"
            pos: "150", {height_ - 200}
            on_text: root.update_data()
        Button:
            text: "Exit"
            size: "140", "40"
            pos: "10", "10"
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.exit_screen()
        Button:
            text: "Help"
            size: "140", "40"
            pos: "160", "10"
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""
    
    result = main_screen

    return result

def locations_(height_, program_location = "", files_location = "", logs_location = ""):
    main_screen = f"""
<LocationsSettings_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label: 
            text: "Files settings:"
            size: "122", 0
            pos: "40", {height_- 30}
            font_size: 30
        Label:
            text: "MCT location:"
            size: "121", "30"
            pos: "0", {height_ - 100}
        Label:
            text: "Video/pictures location:"
            size: "189", "30"
            pos: "0", {height_ - 150}
        Label:
            text: "Logs location:"
            size: "124", "30"
            pos: "0", {height_ - 200}
        TextInput:
            id: program_location
            hint_text: "program_location"
            text: "{program_location}"
            size: "255", "30"
            pos: "210", {height_ - 100}
            on_text: root.update_data()
        TextInput:
            id: files_location
            text: "{files_location}"
            hint_text: "files_location"
            size: "255", "30"
            pos: "210", {height_ - 150}
            on_text: root.update_data()
        TextInput:
            id: logs_location
            text: "{logs_location}"
            hint_text: "logs_location"
            size: "255", "30"
            pos: "210", {height_ - 200}
            on_text: root.update_data()
        Label:
            id: program_location_label
            text: "No such directory or field is empty"
            size: "155", "30"
            pos: "510", {height_ - 100}
            color: 1, 1, 1, 1
        Label:
            id: files_location_label
            text: "No such directory or field is empty"
            size: "155", "30"
            pos: "510", {height_ - 150}
            color: 1, 1, 1, 1
        Label:
            id: logs_location_label
            text: "No such directory or field is empty"
            size: "155", "30"
            pos: "510", {height_ - 200}
            color: 1, 1, 1, 1
        Button:
            text: "Exit"
            size: "140", "40"
            pos: "10", "10"
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.exit_screen()
        Button:
            text: "Help"
            size: "140", "40"
            pos: "160", "10"
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()"""
    
    result = main_screen

    return result

def objects_():
    pass