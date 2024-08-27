n = int(input())
arr = [0 for _ in range(300)]
offset = 100

for i in range(n):
    x1, x2 = map(int, input().split())
    
    x1 += offset
    x2 += offset

    for j in range(x1, x2):
        arr[offset + j] += 1

max_value = max(arr)
print(max_value)