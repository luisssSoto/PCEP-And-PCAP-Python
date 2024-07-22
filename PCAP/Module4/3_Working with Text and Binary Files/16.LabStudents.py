"""Lab Evaluating Students' degrees"""

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # Escribe tu código aquí.
    def __init__(self, line, error_message, character):
        self.__line = line
        self.__error_message = error_message
        self.__character = character


class FileEmpty(StudentsDataException):
    # Escribe tu código aquí.
    def __init__(self, file, size_file, error_message):
        self.__file = file
        self.__error_message = error_message
        self.__size_file = size_file
 

from os import strerror

data = '''John     Smith    5
          Anna     Boleyn   4.5
          John     Smith    2
          Anna     Boleyn   11
          Andrew   Cox      1.5
'''
try:
    stream = open(file="C:\\PCEP-And-PCAP-Python\\PCAP\\Module4\\3_Working with Text and Binary Files\\jeky_file.txt", mode="wt", encoding="utf-8")
    text = stream.write(data)
    stream.close()
except IOError as ioE:
    print("Creation file failed", strerror(ioE.errno))

try:
    source = input("Type the Jeky's source: ")
    stream = open(file="C:\\PCEP-And-PCAP-Python\\PCAP\\Module4\\3_Working with Text and Binary Files\\" + source, mode="rt", encoding="utf-8")
    lines = stream.readlines()
    students_degrees = {}
    if len(lines) == 0:
        raise FileEmpty(source, 'this file is empty:', len(lines))
    while len(lines) != 0:
        for line in lines:
            full_name = ''
            grade = ''
            for character in line:
                if character.isalpha() == False and character.isdigit() == False and character.isspace() == False and character != '.':
                    raise BadLine(line, 'has invalid data:', character)
                elif (character.isalpha() or character.isspace()) and character != '.':
                    full_name += character
                elif character.isdigit() or character == '.':
                    grade += character
            full_name = full_name.replace('\n', '')
            full_name = full_name.lstrip(' ')
            if full_name not in students_degrees:
                students_degrees[full_name] = float(grade)
            else:
                students_degrees[full_name] += float(grade)
        lines = stream.readlines()
    print(students_degrees)
    stream.close()
    for student, degree in students_degrees.items():
        print(student, degree)
except IOError as ioE:
    print("Something was wrong", strerror(ioE.errno))