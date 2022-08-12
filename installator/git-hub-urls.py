from os import path
from graphic.data.database import Database

raw_urls = [
'https://raw.githubusercontent.com/jamesfrienkins3452/MCT/main/program/main.py'
]
_, file_path = "\ ", ""
for n in path.abspath(__file__).split(_[0])[0: len(file_path) - 1]:
    file_path += (n + _[0])

db = Database('raw-urls', file_path)

db.new_table('urls', [('key', 'text', 'PRIMARY KEY'), ('url', 'text', '')])

for k in range(len(raw_urls)):
    db.add_data('urls', (str(k), raw_urls[0]))