'''def f(m):
    s = m * (m + 1) // 2

    if s > k:
        return -1
    if s == k:
        return m * (m + 1)
    if k - s <= m + 1:
        return -1
    return (k - s) * (m + 1)


t = int(input())
for i in range(t):
    k = int(input())
    l = -1
    r = k + 100

    while r - l > 2:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3

        if f(m1) >= f(m2):
            r = m2
        else:
            l = m1
    print(f((r + l) // 2))








s1 = input()
s2 = input()
if len(s1) == len(s2):
    if len(s1) < 5:
        print((5 - len(s1))*2)
    if len(s1) >= 5:
        print(2)

else: #разные длины
    if len(s1) >= 5:
        print(1)
    if len(s1) < 5:
        print((5 - len(s1)) + (5-len(s2)))

'''
cnt = 0
n = int(input())
s = input()
a = s.split()

a = [int(x) for x in a]
for i in range(0, n):
    last1 = a[i] % 10
    for j in range(i+1, n):
        last2 = a[j]%10
        s1 = str(a[j])
        s2 = str(a[i])
        if last1 == int(s1[0]):
            cnt += 1;
            #print(a[i], a[j])
        if last2 == int(s2[0]):
            cnt += 1;
            #print(a[i], a[j])
print(cnt)

