n = int(input())
arr = list(map(int, input().split()))

arr1 = sorted(arr)
arr2 = sorted(arr)[::-1]

# print(arr1)
# print(arr2)

for i in range(n):
    print(arr1[i], end=' ')
print()

for i in range(n):
    print(arr2[i], end=' ')
print()