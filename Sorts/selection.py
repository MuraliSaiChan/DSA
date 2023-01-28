def _min(l):
    t = l[0]
    k = 0
    for i,j in enumerate(l):
        if j < t:
            t = j
            k = i
    return k,t

def selection(l,k = []):
    if len(l) == 1: #1
        k.append(l[0]) #1
        return k #1
    else: #1
        k.append(_min(l)[1]) #N
        del(l[_min(l)[0]]) #N
        k = selection(l,k)#N
        return k


print(selection([2,5,10,0,3,1,8,4,6]))