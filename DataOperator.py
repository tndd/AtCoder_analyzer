# -*- coding: utf-8 -*-
import sqlite3
import numpy as np
from logging import getLogger
from Const import Const as CST


class DataOperator:
  # 番号のファイルで初期化される
  def __init__(self):
    # loggerの設定
    self.logger = getLogger(__name__)
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
    self.__AC_TBL_NAME = 'ac'
    self.__TIME_TBL_NAME = 'time'
    self.__FAIL_TBL_NAME = 'fail'
    return CST.SUCCESS
  
  # テーブルの作成
  def __create_tbls(self):
    # 大会テーブル
    self.__create_contest_tbl()
    # ac率テーブル
    self.__create_ac_tbl()
    # 平均回答時間テーブル
    self.__create_time_tbl()
    # 失敗数テーブル
    self.__create_fail_tbl()
    return CST.SUCCESS
  
  # dbへの接続
  def __connect_db(self):
    # コネクション確立
    self.__conn_racerta = sqlite3.connect('{}/{}'.format(self.__DB_PATH, self.__DB_NAME))
    # カーソル取得
    self.__cursor_racerta = self.__conn_racerta.cursor()
    return CST.SUCCESS
  
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
    return CST.SUCCESS
  
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
        rate_red real,
        deviation real
      );""".format(self.__AC_TBL_NAME)
    self.__cursor_racerta.execute(sql_create_ac_tbl)
    return CST.SUCCESS
  
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
    return CST.SUCCESS
  
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
    return CST.SUCCESS
  
  # ACテーブルにデータ挿入(戻り値は格納したID)
  def __insert_ac_tbl(self, problem_dict):
    sql_insert_ac_tbl = """
      REPLACE INTO {tbl_name} VALUES(
        {id},
        {all},
        {gray},
        {brown},
        {green},
        {cyan},
        {blue},
        {yellow},
        {orange},
        {red},
        {deviation}
      );
    """.format(
      id=problem_dict['id'],
      tbl_name=self.__AC_TBL_NAME,
      all=problem_dict['ac'],
      gray=problem_dict['gray_ac'],
      brown=problem_dict['brown_ac'],
      green=problem_dict['green_ac'],
      cyan=problem_dict['cyan_ac'],
      blue=problem_dict['blue_ac'],
      yellow=problem_dict['yellow_ac'],
      orange=problem_dict['orange_ac'],
      red=problem_dict['red_ac'],
      deviation=0
    )
    self.__cursor_racerta.execute(sql_insert_ac_tbl)
    
    return self.__cursor_racerta.lastrowid
  
  # 回答時間テーブルにデータ挿入
  def __insert_time_tbl(self, problem_dict):
    sql_insert_time_tbl = """
      REPLACE INTO {tbl_name} VALUES(
        {id},
        {all},
        {gray},
        {brown},
        {green},
        {cyan},
        {blue},
        {yellow},
        {orange},
        {red}
      );
    """.format(
      id=problem_dict['id'],
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
  def __insert_fail_tbl(self, problem_dict):
    sql_insert_fail_tbl = """
      REPLACE INTO {tbl} VALUES(
        {id},
        {all},
        {gray},
        {brown},
        {green},
        {cyan},
        {blue},
        {yellow},
        {orange},
        {red}
      );
    """.format(
      id=problem_dict['id'],
      tbl=self.__FAIL_TBL_NAME,
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
  
  # 辞書データをDBに登録(一部)
  def __reg_db_part(self, problem_dict_part):
    # ACテーブル
    self.__insert_ac_tbl(problem_dict_part)
    # 回答時間テーブル
    self.__insert_time_tbl(problem_dict_part)
    # 失敗数テーブル
    self.__insert_fail_tbl(problem_dict_part)
    return problem_dict_part['id']
  
  
  # 辞書データ登録
  def reg_db(self, problem_dict, num):
    # 大会名
    name = 'abc{}'.format('%03d' % num)
    # 辞書データを登録しつつ問題IDのリスト取得
    prob_ids = [self.__reg_db_part(d) for d in problem_dict]
    # DB登録SQL
    sql_insert_contest = """
      INSERT INTO {tbl} VALUES(
        null,
        '{name}',
        {a_id},
        {b_id},
        {c_id},
        {d_id}
      );
    """.format(
      tbl=self.__CONTEST_TBL_NAME,
      name=name,
      a_id=prob_ids[0],
      b_id=prob_ids[1],
      c_id=prob_ids[2],
      d_id=prob_ids[3]
    )
    # insert実行
    self.__cursor_racerta.execute(sql_insert_contest)
    # コミット
    self.__conn_racerta.commit()
    self.logger.info('{} is commited'.format('%03d' % num))
    return CST.SUCCESS

  # 偏差値更新用sql文の生成
  def __gen_upd_ac_dev_sql(self, rate, deviation):
    sql_upd_ac_dev = """
      UPDATE {tbl}
      SET
        deviation = {deviation}
      WHERE
        rate = {rate}
      ;
      """.format(
      tbl=self.__AC_TBL_NAME,
      deviation=deviation,
      rate=rate
    )
    return sql_upd_ac_dev
  
  # 問題の難易度偏差値の計算
  def calc_deviation(self):
    # ac率リストの取得
    sql_calc_deviation = 'SELECT rate from {tbl}'.format(tbl=self.__AC_TBL_NAME)
    self.__cursor_racerta.execute(sql_calc_deviation)
    # レート一覧リスト
    rates = [x[0] for x in self.__cursor_racerta]
    scores = [(1 - x) * 100 for x in rates]
    # 平均値、標準偏差の計算
    avg_ = np.mean(scores)
    std_ = np.std(scores)
    # ACテーブルの偏差値の更新
    for (rate, score) in zip(rates, scores):
      # 偏差値計算
      deviation = round(10 * ((score - avg_) / std_) + 50, 2)
      # 偏差値の更新
      upd_ac_dev_sql = self.__gen_upd_ac_dev_sql(rate, deviation)
      self.__cursor_racerta.execute(upd_ac_dev_sql)
    # コミット
    self.__conn_racerta.commit()
    return CST.SUCCESS
  
    
if __name__ == '__main__':
  a = DataOperator()
  a.calc_deviation()
