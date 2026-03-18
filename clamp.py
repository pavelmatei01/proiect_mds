def clamp(x, lo, hi):
    if x < lo:      # pragma: no mutate
        return lo
    if x > hi:      # pragma: no mutate
        return hi
    return x
