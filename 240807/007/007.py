class Student:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time
    

arr = input().split()
student1 = Student(arr[0], arr[1], arr[2])
print("secret code :", student1.code)
print("meeting point :", student1.point)
print("time :", student1.time)