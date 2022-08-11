import os

def setup(settings_location = os.getenv('APPDATA')[0:len(os.getenv('APPDATA')) - 8] + '\\Local', data_location = f'C:\\Users\\{os.getlogin()}\\Documents', logs_location = f'C:\\Users\\{os.getlogin()}\\Documents'):
    key = "successfully"
    # try:
    if not os.path.isdir(settings_location + '\\MCT'):
        os.mkdir(settings_location + '\\MCT')
    if not os.path.isdir(data_location + '\\MCT'):
        os.mkdir(data_location + '\\MCT\\Recordings')
    if not os.path.isdir(logs_location + '\\MCT'):
        os.mkdir(logs_location + '\\MCT\\Logs')
    # except:
    #     key = "unsuccessfully"
    return key