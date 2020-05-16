import math

Q = int(input())

II = 0

while (II < Q):
    n = int(input())
    ans = 0
    for i in range(1, math.floor(n / 2) + 1):
        ans += i * 8 * i
    
    print(ans)

    II += 1