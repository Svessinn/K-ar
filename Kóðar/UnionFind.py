par = [0]
sz = [1]

def uf_find(a):
    if par[a] == a: return a
    else:
        par[a] = uf_find(par[a])
        return par[a]

def uf_union(a, b):
    pa = uf_find(a)
    pb = uf_find(b)
    if pa != pb:
        par[pb] = uf_find(a)
        sz[pa] += sz[pb]
        return True
    else:
        return False

def uf_size(a):
    return sz[uf_find(a)]
