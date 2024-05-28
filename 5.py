def get_matrix(n=1, m=0, value=0):
    if n == 1 and not m:
        m == 1
    elif n != 1 and not m:
        m = n
    return [[value for _ in range(m)] for _ in range(n)]


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)