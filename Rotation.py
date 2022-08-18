def rotation(a, k):
    len_a = len(a)
    new = [None] * len_a
    rev = list(range(-len_a, 0))

    for i in rev:
        new[i + k] = a[i]

    return new


print(rotation([1, 2, 3, 4], 3))
