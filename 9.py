result = []


def set_result(result: list) -> list:
    for a in range(1, 1001):
        for b in range(a, 1001):
            for c in range(b, 1001):
                if a**2 + b**2 == c**2:
                    result.append([a, b, c])
                    if a + b + c == 1000:
                        return [a, b, c]


print(set_result(result))
