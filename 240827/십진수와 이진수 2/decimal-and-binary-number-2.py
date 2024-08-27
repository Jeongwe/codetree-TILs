binary = input()
arr = [int(digit) for digit in str(binary)]
demical = 0

for i in range(len(arr)):
    demical = demical * 2 + arr[i]
demical *= 17

digits = []
while True:
    if demical < 2:
        digits.append(demical)
        break
    
    digits.append(demical % 2)
    demical //= 2

for n in digits[::-1]:
    print(n, end="")