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



#recursion method, not as efficient as the above 
def fibo_recursive2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive2(n - 1) + fibo_recursive2(n - 2)

# Generating the sequence up to the nth index
def generate_fibo_sequence(n):
    return [fibo_recursive2(i) for i in range(n + 1)]

# Example usage
print(generate_fibo_sequence(7))  # Output: [0, 1, 1, 2, 3, 5, 8, 13]
