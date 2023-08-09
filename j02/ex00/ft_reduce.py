def ft_reduce(function_to_apply, iterable):
    try:
        it = iter(iterable)
    except:
        print("ERROR: reduce() arg2 must support iteration")
        exit()
    res = next(it)
    for value in it:
        try:
            res = function_to_apply(res, value)
        except StopIteration:
            break
    return res
    

if __name__ == '__main__':
    import functools
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print(ft_reduce(lambda u, v: u + v, lst))


