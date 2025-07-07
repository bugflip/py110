def multiplicative_average(lst):
    length = len(lst)
    value = 1
    for num in lst:
        value = num * value
    return f"{value / length:.3f}"