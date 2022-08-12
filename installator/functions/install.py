import os
from requests import get as get_file
from graphic.data.database import Database
settings_location = os.getenv('APPDATA')[0:len(os.getenv('APPDATA')) - 8] + '\\Local'

def read_default_urls():
    download_file('https://github.com/jamesfrienkins3452/MCT/raw/main/raw-urls.db', settings_location + '\\MCT', l = True)
    db = Database('raw-urls.db', settings_location + '\\MCT\\raw-urls.db', k = True)
    dt = db.read_table('urls')
    f = []
    for i in dt:
        f.append(i[1])
    return f

def create_folder(root, folder):
    if not os.path.isdir(root + '\\' + folder):
        os.mkdir(root + '\\' + folder)

def create_folders(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)

prog_l = os.getenv('APPDATA')[0:len(os.getenv('APPDATA')) - 8] + '\\Local'
data_l = f'C:\\Users\\{os.getlogin()}\\Documents'
logs_l = f'C:\\Users\\{os.getlogin()}\\Documents'

def download_file(raw_url, folder, l = False):
    data = raw_url.split('/')
    file_name = data[len(data) - 1].split('?')[0]
    sub_folder = ''
    k = False
    data = raw_url.split('?')[0].split('/')
    for d in data:
        if not k:
            if d == 'installator':
                k = True
        else:
            if d != file_name:
                sub_folder += d + '\\'
    raw = get_file(raw_url, allow_redirects = True)
    if l == False:
        create_folders(folder + '\\MCT\\system files\\program\\' + sub_folder)
        open(folder + '\\MCT\\system files\\program\\' + sub_folder + '\\' + file_name, 'wb').write(raw.content)
    else:
        create_folders(folder)
        open(folder + '\\' + file_name, 'wb').write(raw.content)


def download_program(prg_loc, dt_loc):
    raw_link_list = read_default_urls()
    for link in raw_link_list:
        download_file(link, prg_loc)

def setup(camera_settings, program_location = prog_l, data_location = data_l, logs_location = logs_l):
    try:
        key = "successfully"
        create_folder(settings_location, 'MCT')
        create_folder(program_location, 'MCT')
        create_folder(program_location, 'MCT\\system files')
        create_folder(program_location, 'MCT\\system files\\data')
        create_folder(program_location, 'MCT\\system files\\cache')
        create_folder(program_location, 'MCT\\system files\\program')
        create_folder(program_location, 'MCT\\system files')
        create_folder(data_location, 'MCT')
        create_folder(data_location, 'MCT\\recordings')
        create_folder(logs_location, 'MCT')
        create_folder(logs_location, 'MCT\\logs')

        camera_id, camera_link, camera_name = camera_settings

        db = Database('installation settings',  file_path = settings_location + '\\MCT')
        db.new_table('location', [('key', 'text', 'PRIMARY KEY'), ('value', 'text', '')])
        db.add_data('location', ('program location', program_location))
        db.add_data('location', ('data location', data_location))
        db.add_data('location', ('logs location', logs_location))

        db_cam = Database('camera settings', file_path = program_location + '\\MCT\\system files\\data')
        db_cam.new_table('camera_list', [('key', 'text', 'PRIMARY KEY'), ('name', 'text', '')])
        db_cam.add_data('camera_list', ('cam_1', 'camera_1'))
        db_cam.new_table('camera_1', [('key', 'text', 'PRIMARY KEY'), ('value', 'text', '')])
        db_cam.add_data('camera_1', ('camera id', camera_id))
        db_cam.add_data('camera_1', ('camera link', camera_link))
        db_cam.add_data('camera_1', ('camera name', camera_name))

        download_program(program_location, data_location)
    except:
        key = "unsuccessfully"
    return key

