from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('-headless')
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://music.163.com/playlist?id=2020864493&userid=303132041')
browser.switch_to.frame("contentFrame")
html_source = browser.page_source
id_list = re.findall('<div class="opt hshow">(.*?)</div>',html_source,re.S)
for id in id_list:
    number = re.findall('''<span data-res-id="(.*?)" data-res-type="18" data-res-action="fav"''',id)
    print(number)
import json
import requests
# url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_1481164987'
# json_response = requests.get(url=url)
# html = json_response.text
# json_data = json.loads(html)
#
# results = json_data["hotComments"]
# for result in results:
#     content = result['content']
#     print(content)



