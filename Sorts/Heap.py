def heapify(cl, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and cl[l] > cl[largest]:
        largest = l
    if r < N and cl[r] > cl[largest]:
        largest = r
    if largest != i:
        cl[largest], cl[i] = cl[i], cl[largest]
        heapify(cl, N, largest)


def heapsort(cl):
    N = len(cl)

    for i in range(N // 2 - 1, -1, -1):  # from last non leaf node to root node
        heapify(cl, N, i)

    for i in range(N - 1, 0, -1):
        cl[i], cl[0] = cl[0], cl[i]  # swap top bottom
        heapify(cl, i, 0)  # heapify the new changed heap tree


cl = [8, 3, 5, 0, 1, 10, 9, 4, 7, 2, 6]
heapsort(cl)
print(cl)