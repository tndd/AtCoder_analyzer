# coding: utf-8
from bs4 import BeautifulSoup
import requests
import re
import json
import os

# url生成
def url_generator(time):
  return 'https://abc{}.contest.atcoder.jp/standings#page_1'.format(time)

# htmlから情報抜き出し
def get_content(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'lxml')
  return soup.find('script', type="text/JavaScript").string.replace(' ', '').replace('\n', '')

# 抜き出した情報からdictの作成
def get_content_dict(content):
  regex = '.*(data:.*}]}]).*'
  extr = re.search(regex, content).group(1)
  json_str = '{{{}}}'.format(extr).replace('data:[{','\"data\":[{')
  return json.loads(json_str,encoding='utf-8')

# 情報保存メソッド
def scalpe_abc(num):
  # 保存先
  abc_path = 'data/abc'
  os.makedirs(abc_path, exist_ok=True)
  # url生成
  url = url_generator(num)
  content = get_content(url)
  jsn_dict = get_content_dict(content)
  # ファイル書き込み
  with open('{}/{}.json'.format(abc_path, num), 'w', encoding='utf-8') as f:
    json.dump(jsn_dict, f, indent=2, ensure_ascii=False)

# 情報保存
for i in range(1,108):
  i_str = '%03d' % i
  scalpe_abc(i_str)
  print('done:\t{}'.format(i_str))