def persistence(n, num=0):
    if len(str(n)) == 1:
        return num
    else:
        new_n = reduce(lambda x, y: x*y, [int(i) for i in str(n)])
        return persistence(new_n, num=num+1)