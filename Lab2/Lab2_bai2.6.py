import random

# kiểm tra số nguyên tố 
def is_prime_miller_rabin(n, k=5): # k là số lần thử
    if n <= 1: return False
    if n <= 3: return True
    # Phân tích n-1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n) # Tính a^d mod n
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

# lũy thừa modulo: 7^40 mod 19
result_pow = pow(7, 40, 19) 

# Tìm GCD bằng thuật toán Euclid
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a