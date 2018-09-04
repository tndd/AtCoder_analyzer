# -*- coding: utf-8 -*-
import json
import sys


class Analyzer:
  def __init__(self, num):
    # 定数ファイル定義
    self.__set_const()
    # 変数ファイルの設定
    self.__set_val(num)
    # 辞書に情報登録
    self.reg_info2dict()

  # 定数の設定
  def __set_const(self):
    self.JSON_PATH = 'data/abc'
  
  # 変数の設定
  def __set_val(self, num):
    # ファイル辞書の読み込み
    self.tgt_dict = self.file_loader(num)
    # 参加者数の合計辞書の読み込み
    self.participants_dict = self.gen_participants_dict()
    # 問題の項目ごとの合計辞書リスト
    self.problem_dic = [self.gen_problem_dict() for _ in range(4)]
  
  # 解析ファイルパスの生成
  def __get_path(self, num):
    return '{}/{}.json'.format(self.JSON_PATH, '%03d' % num)
  
  # ファイル読み込み
  def __load_json(self, fpath):
    try:
      with open(fpath, 'r', encoding='utf-8') as f:
        json_dict = json.load(f)
    except:
      sys.stderr.write('[不正なファイル番号]: ファイル読み込みに失敗')
      exit(1)
    return json_dict
  
  # jsonファイルを読み込むラッパーメソッド
  def file_loader(self, num):
    fpath = self.__get_path(num)
    return self.__load_json(fpath)
  
  # レート毎参加者数の辞書
  def gen_participants_dict(self):
    dic = {
      # 参加者数合計
      'gray': 0,
      'brown': 0,
      'green': 0,
      'cyan': 0,
      'blue': 0,
      'yellow': 0,
      'orange': 0,
      'red': 0,
    }
    return dic
  
  # 問題毎のAC数、回答合計時間、失敗数
  def gen_problem_dict(self):
    problem_dict = {
      # AC数合計
      'gray_ac': 0,
      'brown_ac': 0,
      'green_ac': 0,
      'cyan_ac': 0,
      'blue_ac': 0,
      'yellow_ac': 0,
      'orange_ac': 0,
      'red_ac': 0,
      # 回答時間合計
      'gray_avg': 0,
      'brown_avg': 0,
      'green_avg': 0,
      'cyan_avg': 0,
      'blue_avg': 0,
      'yellow_avg': 0,
      'orange_avg': 0,
      'red_avg': 0,
      # 失敗数合計
      'gray_fail': 0,
      'brown_fail': 0,
      'green_fail': 0,
      'cyan_fail': 0,
      'blue_fail': 0,
      'yellow_fail': 0,
      'orange_fail': 0,
      'red_fail': 0
    }
    return problem_dict
  
  # レートを色に変換
  def rate2color(self, dic):
    rate = dic['rating']
    if rate < 400:
      return 'gray'
    elif rate < 800:
      return 'brown'
    elif rate < 1200:
      return 'green'
    elif rate < 1600:
      return 'cyan'
    elif rate < 2000:
      return 'blue'
    elif rate < 2400:
      return 'yellow'
    elif rate < 2800:
      return 'orange'
    else:
      return 'red'
  
  
  # 統計情報を辞書データ(参加者、問題)に登録
  def reg_info2dict(self):
    # 人数毎にループ
    for d in self.tgt_dict['data']:
      # レート色を算出
      rate = self.rate2color(d)
      # 参加者集計
      self.participants_dict[rate] += 1
      # 問題毎の情報集計
      i = 0
      for t, pd in zip(d['tasks'], self.problem_dic):
        if 'elapsed_time' in t:
          pd['{}_ac'.format(rate)] += 1
          pd['{}_avg'.format(rate)] += t['elapsed_time']
          pd['{}_fail'.format(rate)] += t['failure']

a = Analyzer(106)
print(a.problem_dic)
