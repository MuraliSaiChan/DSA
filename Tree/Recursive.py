
def recursive(n):
    if n == 1:
        return n
    else:
        return n*recursive(n-1)

print(recursive(10))