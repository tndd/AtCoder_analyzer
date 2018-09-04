# -*- coding: utf-8 -*-
import sqlite3


class DataOperator:
  # 番号のファイルで初期化される
  def __init__(self):
    # 定数の設定
    self.__set_const()
    # racelta.dbに接続
    self.__cursor_racerta = self.__connect_db()
    # テーブルの作成
    self.__create_tbls()
  
  # 定数の設定
  def __set_const(self):
    # 大会データソースのパス
    self.__ABC_PATH = 'data/abc'
    # dbの保存先パス
    self.__DB_PATH = 'data'
    # dbの名前
    self.__DB_NAME = 'lacerta.db'
    # テーブル名定義
    self.__CONTEST_TBL_NAME = 'contest'
    self.__PROBLEM_TBL_NAME = 'problem'
    self.__AC_TBL_NAME = 'ac'
    self.__AVG_TBL_NAME = 'avg'
    self.__FAIL_TBL_NAME = 'fail'
    ## ステータスコード
    # 正常終了の時に返す値
    self.__SUCCESS = 0
    # 異常終了の時に返すコード
    self.__FAILED = 1
    return self.__SUCCESS
  
  # テーブルの作成
  def __create_tbls(self):
    # 大会テーブル
    self.__create_contest_tbl()
    # 問題テーブル
    self.__create_problem_tbl()
    # ac率テーブル
    self.__create_ac_tbl()
    # 平均回答時間テーブル
    self.__create_avg_tbl()
    # 失敗数テーブル
    self.__create_fail_tbl()
    return self.__SUCCESS
  
  # dbへの接続
  def __connect_db(self):
    return sqlite3.connect('{}/{}'.format(self.__DB_PATH, self.__DB_NAME)).cursor()
  
  # 大会テーブルの作成
  def __create_contest_tbl(self):
    sql_create_user_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key autoincrement,
        name text,
        a_id int,
        b_id int,
        c_id int,
        d_id int
      );""".format(self.__CONTEST_TBL_NAME)
    self.__cursor_racerta.execute(sql_create_user_tbl)
    return self.__SUCCESS
  
  # 問題テーブルの作成
  def __create_problem_tbl(self):
    sql_create_problem_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key autoincrement,
        ac_id int,
        avg_id int,
        fail_id int
      );""".format(self.__PROBLEM_TBL_NAME)
    self.__cursor_racerta.execute(sql_create_problem_tbl)
    return self.__SUCCESS
  
  # ac率テーブルの作成
  def __create_ac_tbl(self):
    sql_create_ac_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key autoincrement,
        rate real,
        rate_gray real,
        rate_brown real,
        rate_green real,
        rate_cyan real,
        rate_blue real,
        rate_yellow real,
        rate_orange real,
        rate_red real
      );""".format(self.__AC_TBL_NAME)
    self.__cursor_racerta.execute(sql_create_ac_tbl)
    return self.__SUCCESS
  
  # 平均回答時間テーブルの作成
  def __create_avg_tbl(self):
    sql_create_avg_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key autoincrement,
        time int,
        time_gray int,
        time_brown int,
        time_green int,
        time_cyan int,
        time_blue int,
        time_yellow int,
        time_orange int,
        time_red int
      );""".format(self.__AVG_TBL_NAME)
    self.__cursor_racerta.execute(sql_create_avg_tbl)
    return self.__SUCCESS
  
  # 平均失敗数テーブルの作成
  def __create_fail_tbl(self):
    sql_create_fail_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id int primary key autoincrement,
        fail real,
        fail_gray real,
        fail_brown real,
        fail_green real,
        fail_cyan real,
        fail_blue real,
        fail_yellow real,
        fail_orange real,
        fail_red real
      );""".format(self.__FAIL_TBL_NAME)
    self.__cursor_racerta.execute(sql_create_fail_tbl)
    return self.__SUCCESS
  
  # ACテーブルに追加
  def insert_ac_tbl(self, problem_dict):
    sql_insert_ac_tbl = """
      INSERT INTO {tbl_name} VALUES(
        {v1},{v2},{v3},{v4},{v5},{v6},{v7},{v8},{v9}
    );""".format(
      tbl_name = self.__AC_TBL_NAME,
      v1 = problem_dict['acRate'],
      v2 = problem_dict['a']
    )
  # 辞書データをDBに登録
  def reg_db(self, problem_dict):
    # ACテーブル
    # 回答時間テーブル
    # 失敗数テーブル
    # 問題テーブル
    
    pass

if __name__ == '__main__':
  a = DataOperator()
