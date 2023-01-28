def binary_search(cl, value):
    start = 0
    end = len(cl) - 1
    mid = (start + end)//2

    while not(cl[mid] == value) and start <= end:
        if value < cl[mid]:
            end = mid-1
        else:
            start = mid + 1
        mid = (start + end)//2

    if cl[mid] == value:
        return mid
    else:
        return -1

cl = list(range(10,20))
value = 15
index = binary_search(cl, value)
print("{} found at {}".format(value,index))