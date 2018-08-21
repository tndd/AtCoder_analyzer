from bs4 import BeautifulSoup
import requests
import re
import json

def url_generator(time):
  return 'https://abc{}.contest.atcoder.jp/standings#page_1'.format(time)

def get_content(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'lxml')
  return soup.find('script', type="text/JavaScript").string.replace(' ', '').replace('\n', '')

def get_content_dict(content):
  regex = '.*(data:.*}]}]).*'
  extr = re.search(regex, content).group(1)
  json_str = '{{{}}}'.format(extr).replace('data:[{','\"data\":[{')
  return json.loads(json_str,encoding='utf-8')

url = url_generator(106)
content = get_content(url)
jsn_dict = get_content_dict(content)

