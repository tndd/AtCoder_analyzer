# -*- coding: utf-8 -*-
import sqlite3
import json


class DataOperator:
  def __init__(self):
    # 定数の設定
    self.abc_path = 'data/abc'
    self.db_path = 'data'
    self.dbname = 'lacerta.db'
    # テーブル名定義
    self.contest_tbl_name = 'contest'
    self.problem_tbl_name = 'problem'
    self.ac_tbl_name = 'ac'
    self.avg_tbl_name = 'avg'
    self.fail_tbl_name = 'fail'
    # カーソル作成
    self.cursor = self.connect_db()
    # テーブルの作成
    self.create_contest_tbl()
    self.create_problem_tbl()
    self.create_ac_tbl()
    self.create_avg_tbl()
    self.create_fail_tbl()
  
  # jsonファイルの読み込み
  def read_json(self, num):
    with open('{}/{}.json'.format(self.abc_path, '%03d' % num), 'r', encoding='utf-8') as f:
      json_dict = json.load(f)
    return json_dict
  
  # dbへの接続
  def connect_db(self):
    return sqlite3.connect('{}/{}'.format(self.db_path, self.dbname)).cursor()
  
  # 大会テーブルの作成
  def create_contest_tbl(self):
    sql_create_user_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key,
        name text,
        a_id int,
        b_id int,
        c_id int,
        d_id int
      );""".format(self.contest_tbl_name)
    self.cursor.execute(sql_create_user_tbl)

  # 問題テーブルの作成
  def create_problem_tbl(self):
    sql_create_problem_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key,
        name text,
        ac_id int,
        avg_id int,
        fail_id int
      );""".format(self.problem_tbl_name)
    self.cursor.execute(sql_create_problem_tbl)
  
  # ac率テーブルの作成
  def create_ac_tbl(self):
    sql_create_ac_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key,
        rate real,
        rate_gray real,
        rate_brown real,
        rate_green real,
        rate_cyan real,
        rate_blue real,
        rate_yellow real,
        rate_orange real,
        rate_red real
      );""".format(self.ac_tbl_name)
    self.cursor.execute(sql_create_ac_tbl)

  # 平均回答時間テーブルの作成
  def create_avg_tbl(self):
    sql_create_avg_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key,
        time int,
        time_gray int,
        time_brown int,
        time_green int,
        time_cyan int,
        time_blue int,
        time_yellow int,
        time_orange int,
        time_red int
      );""".format(self.avg_tbl_name)
    self.cursor.execute(sql_create_avg_tbl)

  # 平均失敗数テーブルの作成
  def create_fail_tbl(self):
    sql_create_fail_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key,
        fail int,
        fail_gray int,
        fail_brown int,
        fail_green int,
        fail_cyan int,
        fail_blue int,
        fail_yellow int,
        fail_orange int,
        fail_red int
      );""".format(self.fail_tbl_name)
    self.cursor.execute(sql_create_fail_tbl)


a = DataOperator()
