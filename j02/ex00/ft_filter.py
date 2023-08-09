def ft_filter(function_to_apply, iterable):
    # si true laisse dans iterable si false on vire
    for value in iterable:
        try:
            if function_to_apply(value):
                yield value
        except:
            ("ERROR: filter() arg2 must support iteration")
            exit()

if __name__ == '__main__':
    # creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
    # print(list(filter(lambda x: x[0].lower() in 'aeiou', creature_names)))
    x = [1, 2, 3, 4, 5]
    result = ft_filter(lambda dum: not (dum % 2), x)
    # result = filter(lambda dum: not (dum % 2), 35)
    print(list(result))