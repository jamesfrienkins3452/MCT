import os
import shutil
from graphic.data.database import Database

settings_location = os.getenv('APPDATA')[0:len(os.getenv('APPDATA')) - 8] + '\\Local'

def remove_folder(folder):
    if os.path.isdir(folder):
        shutil.rmtree(folder)

def setup():
    try:
        db = Database('installation settings',  file_path = settings_location + '\\MCT')
        data = db.read_table('location')
        db.disconnect()
        
        try:
            for loc in data:
                    remove_folder(loc[1] + '\\MCT')

            remove_folder(settings_location + '\\MCT')
        except:
            pass
        key = "successfully"
    except:
        key = "unsuccessfully"
    return key