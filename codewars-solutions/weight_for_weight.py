# https://www.codewars.com/kata/55c6126177c9441a570000cc

def order_weight(strng):
    li = strng.split()
    sums = []
    for n in li:
        sum_ = 0
        for c in n:
            sum_ += int(c)
        sums.append(sum_)

    sums_set = set(sums)
    same_sums = []
    for sum_ in sums_set:
        same_sum = [tup for tup in zip(li, sums) if tup[1] == sum_]
        same_sums.append([n for n in sorted(same_sum, key=lambda pair: pair[0])])
    
    sorted_same_sums = [n for n in sorted(same_sums, key=lambda k: k[0][1])]
    
    res = []
    for same_sum in sorted_same_sums:
        for tup in same_sum:
            res.append(tup[0])

    return ' '.join(res)