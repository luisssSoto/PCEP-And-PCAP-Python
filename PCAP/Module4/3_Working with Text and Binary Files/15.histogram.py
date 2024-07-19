"""Histogram part 3 Writting a file"""

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
    unordered_list = list(map(lambda x: x[1], histogram.items()))
    print(unordered_list)
    is_sorted = False
    while is_sorted == False:
        is_sorted = True
        for i in range(len(unordered_list) - 1):
            if unordered_list[i] < unordered_list[i + 1]:
                unordered_list[i], unordered_list[i + 1] = unordered_list[i + 1], unordered_list[i]
                is_sorted = False
    print(unordered_list)
    sorted_dict = {}
    for puntuation in unordered_list:
        for items in histogram.items():
            if puntuation in items:
                sorted_dict[items[0]] = items[1]
    print(sorted_dict)
    stream = open(file="C:/programming languages/python/pcep-pcap-python/pcep-pcap/pcap/module4/3_working with text and binary files/" + src + '.hist', mode='wt', encoding="utf-8")
    data = ''
    for key, value in sorted_dict.items():
        data += key + '->' + str(value) + '\n'
    writting = stream.write(data)
    stream.close()
except OSError as e:
    print('Something was wrong:', strerror(e.errno))

unordered_dict = {'l': 87, 'o': 44, 'n': 60, 'd': 51, 'b': 24, 'r': 35, 'i': 67, 'g': 28, 'e': 46, 's': 36, 'f': 21, 'a': 82, 'w': 24, 'm': 19, 'y': 22, 'u': 12, 't': 31, 'p': 16, 'h': 22, 'k': 8, 'v': 8, 'c': 4}     
sorted_dict = {'a': 82, 'b': 24, 'c': 4, 'd': 51, 'e': 46, 'f': 21, 'g': 28, 'h': 22, 'i': 67, 'k': 8, 'l': 87, 'm': 19, 'n': 60, 'o': 44, 'p': 16, 'r': 35, 's': 36, 't': 31, 'u': 12, 'v': 8, 'w': 24, 'y': 22}