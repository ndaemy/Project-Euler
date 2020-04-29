def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i is 0:
            return False
    return True


def prime_number_list(length: int):
    result = []
    i = 2
    while len(result) != length:
        if is_prime(i):
            result.append(i)
        i += 1
    return result


length = int(input('Length? '))
print(prime_number_list(length)[-1])
