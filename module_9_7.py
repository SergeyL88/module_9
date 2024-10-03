def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        counter = 0
        for i in range(1, result+1):
            if result % i == 0:
                counter += 1
        if counter > 2:
            print('Составное')
        else:
            print('Простое')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(1, 3, 7)
print(result)
