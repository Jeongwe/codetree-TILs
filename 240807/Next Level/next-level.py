class Student:
    def __init__(self, idd='codetree', level=10):
        self.idd = idd
        self.level = level

arr = list(map(str, input().split()))
student1 = Student(arr[0], arr[1])
student2 = Student()
print(f'user {student2.idd} lv {student2.level}')
print(f'user {student1.idd} lv {student1.level}')