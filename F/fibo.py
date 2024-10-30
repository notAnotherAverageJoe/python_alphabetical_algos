def fibo(n):
    if n == 0:
        return [0]

    if n == 1:
        return [0,1]

    fibo_counter = [0,1]

    a = 0
    b = 1

    for _ in range(2, n + 1):
        temp = a + b
        a = b
        b = temp

        fibo_counter.append(b)

    return fibo_counter


print(fibo(7))
