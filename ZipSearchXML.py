# 郵便番号検索APIにアクセスして、xmlファイルを取得する

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET


zip_str = input('検索したい郵便番号を入力してください（ハイフン無し）： ')
zip = int(zip_str)

# ファイルの保存先
path_w = f"/home/vagrant/workspace/Python3/xmlAnalysis/zip_{zip}.xml"

params = {"zn":zip}

p = urllib.parse.urlencode(params)
url = 'http://zip.cgis.biz/xml/zip.php?' + p

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    xml_string = response.read()

root = ET.fromstring(xml_string)
tree = ET.ElementTree(element=root)

tree.write(path_w) 
