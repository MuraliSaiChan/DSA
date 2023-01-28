def bubble(l):
    t = l[0]
    count = 0
    for n in l: #O(N^2)
        j = 0
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                t = l[i]
                l[i] = l[i+1]
                l[i+1] = t
                j = 1
        #print(l)
        count += 1
        if j == 0:
            print(count)
            return l
    print(count)
    return l


print(bubble([2,5,3,1,8,4,6]))
#print(bubble([1,3,2,4,5]))
