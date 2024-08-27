n, k = map(int, input().split())
arr = [0 for i in range(n)] # N개의 칸 생성 

for i in range(k):  # 명령 개수 K만큼 반복 
    a, b = map(int, input().split())
    for j in range(a, b + 1):   # A번째 칸부터 B번째 칸까지 
        arr[j - 1] += 1 # 위치 = 인덱스 + 1

max_value = max(arr)
print(max_value)