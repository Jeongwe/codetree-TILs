a, b = map(int, input().split())
n = input()

narr = [int(digit) for digit in str(n)]
demical = 0
for i in range(len(narr)):
    demical = demical * a + narr[i]

binary = []
while True:
    if demical < b:
        binary.append(demical)
        break
    
    binary.append(demical % b)
    demical //= b

for digit in binary[::-1]:
    print(digit, end="")