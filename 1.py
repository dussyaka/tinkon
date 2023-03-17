page = list(map(int, input().split()))

if page == sorted(page) or page == sorted(page, reverse=True):
    print('YES')
else:
    print('NO')