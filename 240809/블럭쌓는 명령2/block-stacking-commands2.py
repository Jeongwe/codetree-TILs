n, k = map(int, input().split())
cnt = [0 for i in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    
    for i in range(a, b+1):
        cnt[i] += 1

max_val = 0
for i in range(1, n+1):
    if max_val < cnt[i]:
        max_val = cnt[i]

print(max_val)