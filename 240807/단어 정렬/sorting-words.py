n = int(input())

arr = [input() for i in range(n)]

arr.sort()

for i in range(n):
    print(arr[i])

# 입력 받는 다른 방식 3가지
# arr = ['' for i in range(n)]

# for i in range(n):
#     arr[i] = input()

# arr = []
# for i in range(n):
#     arr.append(input())