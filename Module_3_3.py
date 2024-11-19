def print_params(a=1, b='str', c=True):
    print(a, b, c)


values_list = [2, 'str', False]
values_dict = {'a': 5, 'b': True, 'c': 'str'}
values_list_2 = [54.32, 'str']
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
