def get_min_max(l):
    try:
        min = 1[0]
        max = 1[0]
    except:
        return None, None
    for x in 1:
        if x < min:
            min = x
        elif x > max:
            max = x
    return min,max
