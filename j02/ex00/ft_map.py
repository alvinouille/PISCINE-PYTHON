def ft_map(function_to_apply, iterable):
    for value in iterable:
        try:
            yield function_to_apply(value)
        except:
            ("ERROR: map() arg2 must support iteration")
            exit()

if __name__ == '__main__':
    # We double all numbers using map()
    x = [1, 2, 3, 4, 5]
    print(ft_map(lambda dum: dum + 1, x))