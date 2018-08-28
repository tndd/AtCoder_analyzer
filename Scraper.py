# coding: utf-8
from bs4 import BeautifulSoup
import requests
import re
import json
import os


class Scraper:
  def __init__(self):
    # 保存先
    self.abc_path = 'data/abc'
    os.makedirs(self.abc_path, exist_ok=True)
  
  # url生成
  def __url_generator(self, time):
    return 'https://abc{}.contest.atcoder.jp/standings#page_1'.format(time)
  
  # htmlから情報抜き出し
  def __get_content(self, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup.find('script', type="text/JavaScript").string.replace(' ', '').replace('\n', '')
  
  # 抜き出した情報からdictの作成
  def __get_content_dict(self, content):
    regex = '.*(data:.*}]}]).*'
    extr = re.search(regex, content).group(1)
    json_str = '{{{}}}'.format(extr).replace('data:[{', '\"data\":[{')
    return json.loads(json_str, encoding='utf-8')
  
  # 情報保存メソッド
  def scalpe_abc(self, num):
    # url生成
    url = self.__url_generator(num)
    content = self.__get_content(url)
    jsn_dict = self.__get_content_dict(content)
    # ファイル書き込み
    with open('{}/{}.json'.format(self.abc_path, num), 'w', encoding='utf-8') as f:
      json.dump(jsn_dict, f, indent=2, ensure_ascii=False)
    # 完了
    print('abc{}\tdone'.format('%03d' % num))
  
  # ループして情報を取得
  def scalpe_abc_loop(self, end, start = 1):
    for i in range(start, end):
      i_str = '%03d' % i
      self.scalpe_abc(i_str)
