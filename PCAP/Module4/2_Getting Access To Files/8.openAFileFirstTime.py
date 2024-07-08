"""Openning a file at first time"""
try:
    stream = open(file='C:\\Users\\AlexSoto\\Desktop\\fileTest.txt', mode='rt', encoding='utf-8')
    stream.close()
except Exception as exc:
    print("The file can't be opened", exc)