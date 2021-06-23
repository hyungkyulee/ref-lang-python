import xml.etree.ElementTree as ET
import urllib
from urllib.request import urlopen

url = 'http://py4e-data.dr-chuck.net/comments_1126576.xml'
document = urlopen(url).read()
print('document lenth: ', len(document))

# data = '''<comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>'''

tree = ET.fromstring(document)
count_list = tree.findall('.//count')
total_count = 0
lenth_count = 0
# print('Count:', len(count_list))
for item in count_list:
    # print(int(item.text))
    if int(item.text) >= 0:
        lenth_count += 1
        total_count += int(item.text)

print('found: %d, num of count: %d, total: %d' % (len(count_list), lenth_count, total_count))



