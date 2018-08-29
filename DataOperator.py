# -*- coding: utf-8 -*-
import sqlite3
import json


class DataOperator:
  def __init__(self):
    # 定数の設定
    self.abc_path = 'data/abc'
    self.db_path = 'data'
    self.dbname = 'lacerta.db'
    self.user_tbl_name = 'user_tbl'
    # カーソルの設定
    self.user_cur = self.connect_db()
    # userテーブルの作成
    self.create_user_tbl()
  
  # jsonファイルの読み込み
  def read_json(self, num):
    with open('{}/{}.json'.format(self.abc_path, '%03d' % num), 'r', encoding='utf-8') as f:
      json_dict = json.load(f)
    return json_dict
  
  # dbへの接続
  def connect_db(self):
    return sqlite3.connect('{}/{}'.format(self.db_path, self.dbname)).cursor()
  
  # テーブルの作成
  def create_user_tbl(self):
    sql_createdb = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key,
        uname text,
        uname_screen text,
        twitter_id text,
        coutry text,
        rating int,
        competitions int
      );""".format(self.user_tbl_name)
    self.user_cur.execute(sql_createdb)


a = DataOperator()