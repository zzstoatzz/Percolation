import os, sys, copy, random
# 'union' subroutine to connect vertices
def connect(v1, v2, A, B, i):
    v1[i] = A
    v2[i] = B        
    return i + 1
# recursive path compression 'find' algorithm
def findroot(i, ptr):
    if ptr[i] < 0: 
        return i
    ptr[i] = findroot(ptr[i], ptr)
    return ptr[i]
# init vertex lists, return iterator (3/2*N) as 'index'
def init_lists(v1, v2, WIDTH, HEIGHT, W):
    index = 0
    for x in range(0, WIDTH):
        for y in range(0, WIDTH):
            for z in range(0, HEIGHT):
                s1 = x + WIDTH*y + WIDTH*WIDTH*z
                s2 = ((x+1)&W) + WIDTH*y + WIDTH*WIDTH*z
                index = connect(v1, v2, s1, s2, index)
                s2 = x + WIDTH*((y+1)&W)+ WIDTH*WIDTH*z
                index = connect(v1, v2, s1, s2, index)
                if (z < HEIGHT-1):
                    s2 = x + WIDTH*y + WIDTH*WIDTH*((z+1)&W)
                    index = connect(v1, v2, s1, s2, index)
                else:
                    s2 = x + WIDTH*y + WIDTH*WIDTH*(0)
                    index = connect(v1, v2, s1, s2, index)
    return index
# randomize list of bonds
def shuffle_bonds(index, v1, v2):
    for i in range(0, index):
        rn = random.random()
        j = i + int((index-i)*rn)
        temp = copy.copy(v1[i])
        v1[i] = v1[j]
        v1[j] = temp
        temp = copy.copy(v2[i])
        v2[i] = v2[j]
        v2[j] = temp
# union-find routine: bonds connect sites
def cluster(i, lists, big, M2):
    v1, v2, ptr, M2minus = lists    
    tup = [v1[i], v2[i]]
    r1, r2 = findroot(v1[i], ptr), findroot(v2[i], ptr)

    if (r2 != r1):
        M2 += ptr[r1]*2.0*ptr[r2]
        if ptr[r1] > ptr[r2]:
            ptr[r2] += ptr[r1]
            ptr[r1] = r2
            r1 = r2
        else:
            ptr[r1] += ptr[r2]
            ptr[r2] = r1
        if (-ptr[r1]>big):
            big = -ptr[r1]
    M2minus[i] += (M2 - big*1.0*big)
    return tup
