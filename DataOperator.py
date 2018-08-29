# -*- coding: utf-8 -*-
import sqlite3
import json


class DataOperator:
  def __init__(self):
    # 定数の設定
    self.abc_path = 'data/abc'
    self.sql_path = 'data'
    self.dbname = 'lacerta.db'
    self.user_tbl_name = 'user_tbl'
    # カーソルの設定
    self.user_cur = self.get_user_cursor()
  
  # jsonファイルの読み込み
  def read_json(self, num):
    with open('{}/{}.json'.format(self.abc_path, '%03d' % num), 'r', encoding='utf-8') as f:
      json_dict = json.load(f)
    return json_dict
  
  # dbの作成、カーソルの取得
  def get_user_cursor(self):
    sql_createdb = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key,
        uname text,
        uname_screen text,
        twitter_id, text,
        coutry text,
        rating int,
        competitions int
      );
    """.format(self.user_tbl_name)
    return sqlite3.connect(self.user_tbl_name).cursor()


a = DataOperator()
# for d in a.read_json(100)['data']:
#   # print(d)
#   for j in d['tasks']:
#     print(j)
# print(a.read_json(1)['data'][0])

# conn = sqlite3.connect('data/example.db')
# c = conn.cursor()
# # Create table
# c.execute('''CREATE TABLE stocks
#              (date text, trans text, symbol text, qty real, price real)''')
#
# # Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
# # Save (commit) the changes
# conn.commit()
#
# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()
