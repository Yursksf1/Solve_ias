def getValor(a,i,j):
    try:
        return a[i][j]
    except:
        return ""

def alternate(a):
    w = ''
    for i in range(0,4):
        for j in range(0,4):
            w += getValor(a,j,i)
    return w