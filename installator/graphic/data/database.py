import sqlite3
from os import path

_, default_file_path = "\ ", ""
for n in path.abspath(__file__).split(_[0])[0: len(default_file_path) - 1]:
    default_file_path += (n + _[0])

class Database:
    def __init__(self, database_name, file_path = default_file_path, k = ''):
        self.database_name = database_name
        if k == '':
            self.conn = (sqlite3.connect(f"{file_path}/" + self.database_name + ".db"))
        else:
            self.conn = (sqlite3.connect(file_path))
        self.cursor = self.conn.cursor()

        self.table_list = []
        self.table_rows = {}

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tb_l = self.cursor.fetchall()

        if tb_l != []:
            for l in tb_l[0]:
                self.table_list.append(l)

        for table_name in self.table_list:
            self.cursor.execute(f"select * from {table_name} limit 1")
            col_name = [i[0] for i in self.cursor.description]
            self.table_rows[table_name] = col_name

    def new_table(self, table_name, table_rows):
        if table_name not in self.table_list:
            self.table_list.append(table_name)
            tb = []
            for i in table_rows:
                tb.append(i[0])
            self.table_rows[table_name] = tb

            rows_count = len(table_rows)
            rows_sql = ""

            for id in range(rows_count):
                row_name, row_type, row_key = table_rows[id]
                rows_sql += f"{row_name} {row_type}"

                if row_key != "":
                    rows_sql += f" {row_key}"

                if id + 1 < rows_count:
                    rows_sql += ",\n"

            command = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
{rows_sql}
);
"""
            self.cursor.execute(command)
            self.conn.commit()
            return command
        else:
            return None

    def read_table(self, table_name):
        if table_name in self.table_list:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            data =  self.cursor.fetchall()
            return data
        else:
            return None

    def add_data(self, table, data):
        rows = ""
        for id in range(len(data)):
            rows += "\"" + data[id] + "\""
            if id + 1 < len(data):
                rows += ", "
        command = f"INSERT INTO {table} VALUES ({rows});"
        self.cursor.execute(command)
        self.conn.commit()
        return command

    def edit_data(self, table, data, key_name, key_value):
        table_rows = self.table_rows.get(table)
        comm = ""
        for id in range(len(data)):
            comm += table_rows[id]+ " = \"" + data[id] + "\""
            if id + 1 < len(data):
                comm += ", "
        command = f"UPDATE {table} SET {comm} WHERE {key_name} = \"{key_value}\""
        self.cursor.execute(command)
        self.conn.commit()
        return command

    def delete_data(self, table, key_name, key_value):
        command = f"DELETE FROM {table} WHERE {key_name} = \"{key_value}\""
        self.cursor.execute(command)
        self.conn.commit()
        return command
    
    def disconnect(self):
        self.conn.close()
