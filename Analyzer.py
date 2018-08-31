# -*- coding: utf-8 -*-
import json
import sys


class Analyzer:
  def __init__(self, num):
    # 現在参照中のファイル番号
    self.__now_num = num
    # 読み込んだファイル辞書
    self.tgt_dict = self.file_loader(num)
  
  # 解析ファイルパスの生成
  def __get_path(self, num):
    return 'data/abc/{}.json'.format('%03d' % num)
  
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
    self.__now_num = num
    fpath = self.__get_path(num)
    return self.__load_json(fpath)
  
  # レートを出す
  
  
  # @@
  def f(self):
    for d in self.tgt_dict['data']:
      print(d)
  
a = Analyzer(1)
print(a.f())