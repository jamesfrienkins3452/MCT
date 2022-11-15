def main(height_, width_, connection_status = "Unknown", repair_key = "successfully", install_key = "successfully"):
    main_screen = f"""
<Main_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'graphic/images/installation_background.jpg'
    Widget:
        Label:
            text: "Welcome to MCT!"
            size: "260", 0
            pos: "0", {height_- 30}
            font_size: 30

        # DropDown:
        #     id: camera_drop_list
        #     pos: {width_ - 160}, {height_ - 260}

        #     Button:
        #         id: btn1
        #         text: 'First Item'
        #         size_hint: None, None
        #         height: 35
        #         # on_release: camera_drop_list.select('First Item')
        #     Button:
        #         id: btn2
        #         text: 'Second Item'
        #         size_hint: None, None
        #         height: 35
        #         # on_release: camera_drop_list.select('Second Item')

        Button:
            text: "Camera list"
            size: "140", "40"
            pos: "10", {height_ - 110}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.camera()

        Button:
            text: "Logs"
            size: "140", "40"
            pos: "10", {height_ - 160}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.logs()

        Button:
            text: "Recordings"
            size: "140", "40"
            pos: "10", {height_ - 210}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.recordings()

        Button:
            text: "System files"
            size: "140", "40"
            pos: "10", {height_ - 260}
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.system_files()

        Button:
            text: "Help"
            size: "140", "32"
            pos: {width_ - 160}, "10"
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.help()

        Button:
            text: "Exit"
            size: "140", "32"
            pos: "10", "10"
            background_normal: ""
            background_color: 0.9, 0.9, 1, .8
            color: 0, 0, 0
            on_release:
                root.exit()"""

    result = main_screen

    return result

def camera(height_, camera_id = "", camera_link = "", camera_name = ""):
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