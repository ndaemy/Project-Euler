n = int(input('1 to n? '))


def search(n):
    number = n
    while True:
        for i in range(1, n + 1):
            if i == n and number % i == 0:
                return number
            if number % i != 0:
                break
        number += n


result = search(n)
print(result)
