# -*- coding: utf-8 -*-
import sqlite3
import json

class DataOperator:
  def __init__(self):
    self.abc_path = './data/abc'
    
  def read_dict(self, num):
    with open('{}/{}.json'.format(self.abc_path, '%03d' % num), 'r', encoding='utf-8') as f:
      json_dict = json.load(f)
    return json_dict
 
a = DataOperator()
for d in a.read_dict(100)['data']:
  print(d)
  for j in d['tasks']:
    print(j)
# print(a.read_dict(1)['data'][-1]['tasks'][''])