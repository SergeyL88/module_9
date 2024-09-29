def apply_all_func(int_list, *functions):
    results = dict()
    for function in functions:
        try:
            results[function.__name__] = function(int_list)
        except TypeError as exc:
            if 'unsupported operand' in exc.args[0]:
                print(f'Функция {function.__name__} не поддерживает {int_list}')

    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func(['string_5', 'string_2'], len, sum, sorted))
