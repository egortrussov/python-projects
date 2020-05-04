a = list(map(int, input().split()))

k = int(input())

b = a[(len(a) - k):] + a[0:(len(a) - k)]
print(b)