from datetime import date

d, m = map(int, input().split())
d1, m1, y1 = map(int, input().split())

y = y1
if m1 > m or (m1 == m and d1 >= d):
    y += 1

dd = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ans = 0
if y > y1:
    for i in range(m1 - 1, 12):
        currd = dd[i]
        if i == 1 and (y1 % 400 == 0 or (y1 % 4 == 0 and y1 % 100 != 0)):
            currd += 1
        if i == m1 - 1:
            ans += currd - d1 
        else:
            ans += currd 
    for i in range(0, m):
        currd = dd[i]
        if i == 1 and (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
            currd += 1
        if i == m - 1:
            ans += d
        else:
            ans += currd 
else:
    for i in range(m1 - 1, m):
        currd = dd[i]
        if i == 1 and (y1 % 400 == 0 or (y1 % 4 == 0 and y1 % 100 != 0)):
            currd += 1
        if i == m1 - 1:
            ans += currd - d1 
        elif i == m - 1:
            ans += d
        else:
            ans += currd 

print(ans)