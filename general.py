def coins(n, d):
    d = list(reversed(d))
    len_d = len(d)
    k = [0] * len_d
    r = n
    for i in range(len_d):
        if r < d[i]:
            k[i] = 0
            continue
        else:  
            k[i] = r // d[i]
            r -= k[i] * d[i]
    return k

print(coins(140, [50, 25, 10, 5, 1]))
