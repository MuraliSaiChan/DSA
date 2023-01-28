def merge(cl, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = cl[l + i]

    for i in range(n2):
        R[i] = cl[i + m + 1]
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            cl[k] = L[i]
            i += 1
        else:
            cl[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        cl[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        cl[k] = R[j]
        j += 1
        k += 1


def mergeSort(cl, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSort(cl, l, m)
        mergeSort(cl, m + 1, r)
        merge(cl, l, m, r)


cl = [4, 2, 3, 1, 8, 6, 7, 0]
mergeSort(cl, 0, 7)
print(cl)

