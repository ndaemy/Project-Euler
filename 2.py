# Problem:
# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

n = int(input('Max number: '))

result = 0
fibonacci = [1, 2]

x = fibonacci[-1] + fibonacci[-2]
while x <= n:
    fibonacci.append(x)
    x = fibonacci[-1] + fibonacci[-2]

for i in fibonacci:
    if not i % 2:
        result += i

print(result)
