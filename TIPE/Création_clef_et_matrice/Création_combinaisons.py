def combinaisons(n):
    L = []
    for a in range(1,n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                for d in range(1, n+1):
                    L.append([a, b, c, d])
    return L
