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
    # 順位表テーブルの作成
    self.create_turn_table()
  
  # jsonファイルの読み込み
  def read_json(self, num):
    with open('{}/{}.json'.format(self.abc_path, '%03d' % num), 'r', encoding='utf-8') as f:
      json_dict = json.load(f)
    return json_dict
  
  # dbへの接続
  def connect_db(self):
    return sqlite3.connect('{}/{}'.format(self.db_path, self.dbname)).cursor()
  
  # userテーブルの作成
  def create_user_tbl(self):
    sql_create_user_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key,
        uname text,
        uname_screen text,
        twitter_id text,
        coutry text,
        rating int,
        competitions int
      );""".format(self.user_tbl_name)
    self.user_cur.execute(sql_create_user_tbl)
  
  # turn_tblの作成
  def create_turn_tbl(self):
    sql_create_turn_tbl = """
          CREATE TABLE IF NOT EXISTS {}(
            id int primary key,
            contest_id int,
            rank int,
            score int,
            time int,
            penalty int,
            failure int
          );""".format(self.user_tbl_name)
    self.user_cur.execute(sql_create_turn_tbl)

a = DataOperator()