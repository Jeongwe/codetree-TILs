binary = input()
num = 0
arr = [int(digit) for digit in str(binary)]

for i in range(len(arr)):
    num = num * 2 + arr[i]

print(num)