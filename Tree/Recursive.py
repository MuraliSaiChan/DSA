
def recursive(n):
    if n == 0:
        return
    else:
        print(n)
        return recursive(n-1)

recursive(10)