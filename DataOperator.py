# -*- coding: utf-8 -*-
import sqlite3


class DataOperator:
  # 番号のファイルで初期化される
  def __init__(self):
    # 定数の設定
    self.__set_const()
    # racelta.dbに接続
    self.__connect_db()
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
    self.__TIME_TBL_NAME = 'time'
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
    self.__create_time_tbl()
    # 失敗数テーブル
    self.__create_fail_tbl()
    return self.__SUCCESS
  
  # dbへの接続
  def __connect_db(self):
    # コネクション確立
    self.__conn = sqlite3.connect('{}/{}'.format(self.__DB_PATH, self.__DB_NAME))
    # カーソル取得
    self.__cursor_racerta = self.__conn.cursor()
    return self.__SUCCESS
  
  # 大会テーブルの作成
  def __create_contest_tbl(self):
    sql_create_user_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id integer primary key autoincrement,
        name text,
        a_id integer,
        b_id integer,
        c_id integer,
        d_id integer
      );""".format(self.__CONTEST_TBL_NAME)
    self.__cursor_racerta.execute(sql_create_user_tbl)
    return self.__SUCCESS
  
  # 問題テーブルの作成
  def __create_problem_tbl(self):
    sql_create_problem_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id integer primary key autoincrement,
        ac_id integer,
        avg_id integer,
        fail_id integer
      );""".format(self.__PROBLEM_TBL_NAME)
    self.__cursor_racerta.execute(sql_create_problem_tbl)
    return self.__SUCCESS
  
  # ac率テーブルの作成
  def __create_ac_tbl(self):
    sql_create_ac_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id integer primary key autoincrement,
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
  def __create_time_tbl(self):
    sql_create_time_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id integer primary key autoincrement,
        time integer,
        time_gray integer,
        time_brown integer,
        time_green integer,
        time_cyan integer,
        time_blue integer,
        time_yellow integer,
        time_orange integer,
        time_red integer
      );""".format(self.__TIME_TBL_NAME)
    self.__cursor_racerta.execute(sql_create_time_tbl)
    return self.__SUCCESS
  
  # 平均失敗数テーブルの作成
  def __create_fail_tbl(self):
    sql_create_fail_tbl = """
      CREATE TABLE IF NOT EXISTS {}(
        id integer primary key autoincrement,
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
  
  # ACテーブルにデータ挿入(戻り値は格納したID)
  def insert_ac_tbl(self, problem_dict):
    sql_insert_ac_tbl = """
      INSERT INTO {tbl_name} VALUES(
        null,
        {all},
        {gray},
        {brown},
        {green},
        {cyan},
        {blue},
        {yellow},
        {orange},
        {red}
      )""".format(
      tbl_name=self.__AC_TBL_NAME,
      all=problem_dict['ac'],
      gray=problem_dict['gray_ac'],
      brown=problem_dict['brown_ac'],
      green=problem_dict['green_ac'],
      cyan=problem_dict['cyan_ac'],
      blue=problem_dict['blue_ac'],
      yellow=problem_dict['yellow_ac'],
      orange=problem_dict['orange_ac'],
      red=problem_dict['red_ac']
    )
    self.__cursor_racerta.execute(sql_insert_ac_tbl)
    
    return self.__cursor_racerta.lastrowid
  
  # 回答時間テーブルにデータ挿入
  def insert_time_tbl(self, problem_dict):
    sql_insert_time_tbl = """
      INSERT INTO {tbl_name} VALUES(
        null,
        {all},
        {gray},
        {brown},
        {green},
        {cyan},
        {blue},
        {yellow},
        {orange},
        {red}
      );""".format(
        tbl_name=self.__TIME_TBL_NAME,
        all=problem_dict['time'],
        gray=problem_dict['gray_time'],
        brown=problem_dict['brown_time'],
        green=problem_dict['green_time'],
        cyan=problem_dict['cyan_time'],
        blue=problem_dict['blue_time'],
        yellow=problem_dict['yellow_time'],
        orange=problem_dict['orange_time'],
        red=problem_dict['red_time']
    )
    self.__cursor_racerta.execute(sql_insert_time_tbl)
    return self.__cursor_racerta.lastrowid
  
  # 回答時間テーブルにデータ挿入
  def insert_fail_tbl(self, problem_dict):
    sql_insert_fail_tbl = """
      INSERT INTO {tbl_name} VALUES(
        null,
        {all},
        {gray},
        {brown},
        {green},
        {cyan},
        {blue},
        {yellow},
        {orange},
        {red}
      );""".format(
      tbl_name=self.__FAIL_TBL_NAME,
      all=problem_dict['fail'],
      gray=problem_dict['gray_fail'],
      brown=problem_dict['brown_fail'],
      green=problem_dict['green_fail'],
      cyan=problem_dict['cyan_fail'],
      blue=problem_dict['blue_fail'],
      yellow=problem_dict['yellow_fail'],
      orange=problem_dict['orange_fail'],
      red=problem_dict['red_fail']
    )
    self.__cursor_racerta.execute(sql_insert_fail_tbl)
    return self.__cursor_racerta.lastrowid
  
  # 辞書データをDBに登録
  def reg_db(self, problem_dict):
    # ACテーブル
    ac_id = self.insert_ac_tbl(problem_dict[0])
    # 回答時間テーブル
    time_id = self.insert_time_tbl(problem_dict[0])
    # 失敗数テーブル
    fail_id = self.insert_fail_tbl(problem_dict[0])
    # 問題テーブル
    self.__conn.commit()


if __name__ == '__main__':
  a = DataOperator()
