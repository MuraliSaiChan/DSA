def partition(cl, low, high):
    i = low - 1
    p = cl[high]

    for j in range(low,high):
        if cl[j] <= p:
            i = i+1
            cl[i], cl[j] = cl[j], cl[i]
    cl[i+1],cl[high] = cl[high],cl[i+1]
    return (i+1)

def quick(cl, low, high):
    if low < high:
        pi = partition(cl, low, high)
        quick(cl, low, pi - 1)
        quick(cl, pi + 1, high)


cl = [4, 2, 3, 1, 8, 6, 7, 0]
quick(cl, 0, 7)
print(cl)



