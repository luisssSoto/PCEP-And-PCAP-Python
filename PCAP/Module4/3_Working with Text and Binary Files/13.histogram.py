"""Histogram Creating a file"""

from os import strerror

data = '''London Bridge is falling down Falling down, falling down London Bridge is falling down My fair Lady 
Build it up with iron bars Iron bars, iron bars Build it up with iron bars My fair Lady
Iron bars will bend and break Bend and break, bend and break Iron bars will bend and break My fair Lady
Build it up with gold and silver Gold and silver, gold and silver Build it up with gold and silver My fair Lady
London Bridge is falling down Falling down, falling down London Bridge is falling down My fair Lady
Silver and gold will be stolen away, Stolen away, stolen away, Silver and gold will be stolen away, My fair Lady.
Set a man to watch all nigh, Watch all night, watch all night, Set a man to watch all night, My fair Lady.
Suppose the man should fall asleep, Fall asleep, fall asleep, Suppose the man should fall asleep? My fair Lady.
Give him a pipe to smoke all night, Smoke all night, smoke all night, Give him a pipe to smoke all night, My fair Lady.'''

try:
    stream = open(file="C:/programming languages/python/pcep-pcap-python/pcep-pcap/pcap/module4/3_working with text and binary files/london bridge.txt", mode='wt', encoding="utf-8")
    stream.write(data)
    stream.close()
except IOError as e:
    print('It was an error', strerror(e.errno))

