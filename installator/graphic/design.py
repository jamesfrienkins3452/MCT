def design(height_, connection_status = "Unknown"):
    dsgn = f"""
<Setup_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Welcome to MCT installator!"
            size: "400", 0
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
                root.repair()
        Button:
            text: "Uninstall"
            size: "140", "40"
            pos: "10", {height_ - 200}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.uninstall()
        Button:
            text: "Help"
            size: "140", "32"
            pos: "10", {10}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()


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
                root.manager.current = 'checkingconnection_screen'
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
                root.help()


<CheckingConnection_Screen>:
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
            id: CheckingConnection_Screen_ConnectionStatus
            size: "220", 0
            pos: "0", {height_- 80}
            font_size: 15
        Button:
            text: "Continue"
            id: CheckingConnection_Screen_Continue
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
            id: CheckingConnection_Screen_Back
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
                root.help()


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
        Button:
            text: "Continue"
            size: "140", "40"
            pos: "10", {height_ - 100}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            disabled: True
        Button:
            text: "Back"
            size: "140", "40"
            pos: "10", {height_ - 150}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.manager.current = 'checkingconnection_screen'
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
                root.help()
    """
    return dsgn