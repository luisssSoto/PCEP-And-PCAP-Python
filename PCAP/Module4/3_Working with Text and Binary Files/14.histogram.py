"""Histogram part 2 Reading a file"""

from os import strerror

src = input('Type the name of the file: ')
histogram = {}
sorted_histogram = {}

try:
    stream = open(file="C:/programming languages/python/pcep-pcap-python/pcep-pcap/pcap/module4/3_working with text and binary files/" + src, mode='rt', encoding="utf-8")
    reading = stream.read()
    for element in reading:
        if element.isalpha():
            element = element.lower()
            if element not in histogram:
                histogram[element] = 1
            elif element in histogram:
                histogram[element] = histogram[element] + 1
    print(histogram)
    for key, value in sorted(histogram.items()):
        sorted_histogram[key] = value
    print(sorted_histogram)
    stream.close()
except OSError as e:
    print('Something was wrong:', strerror(e.errno))


