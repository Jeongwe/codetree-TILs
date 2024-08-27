n = int(input())
arr = [0 for _ in range(200)]
offset = 100

for i in range(n):
    x1, x2 = map(int, input().split())
    
    if x1 < 0:
        x1 += offset
    if x2 < 0:
        x2 += offset

    for j in range(x1, x2):
        arr[offset + j] += 1

max_value = max(arr)
print(max_value)