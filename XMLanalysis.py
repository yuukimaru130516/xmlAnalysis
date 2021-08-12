# XMLファイルを読み込んで文字列を返す
import xml.etree.ElementTree as ET

zip = 'zip_2450016.xml'

tree = ET.ElementTree(file=zip)
root = tree.getroot()

for value in root.iter('value'):
  print(value.attrib)