import time

class Student:
    def take_nap(self, seconds):
        print(f"I'm going to take a nap for a {seconds} seconds")
        time.sleep(seconds)
        print('I am ready now!')

student1 = Student()
student1.take_nap(5)