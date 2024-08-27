n = int(input())
# 겹침을 처리할 배열 0으로 초기화
arr = [0] * 300 # [0 for _ in range(300)]
# 음수 값 처리를 위해 오프셋
offset = 100

for i in range(n):
    x1, x2 = map(int, input().split())
    
    # 오프셋을 적용하여 음수 --> 양수 
    x1 += offset
    x2 += offset

    for j in range(x1, x2):
        arr[j] += 1

max_value = max(arr)
print(max_value)