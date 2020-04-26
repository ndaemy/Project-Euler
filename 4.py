def isPalindrome(n):
    temp, r, digit = n, 0, 0
    while temp > 0:
        temp = int(temp / 10)
        digit += 1

    temp = n
    digit -= 1
    while temp > 0:
        r += (10 ** digit) * (temp % 10)
        digit -= 1
        temp = int(temp / 10)

    return r == n


results = []
for i in range(1, 1000):
    for j in range(1, 1000):
        if isPalindrome(i*j):
            results.append(i*j)

results.sort()
print(results[-1])
