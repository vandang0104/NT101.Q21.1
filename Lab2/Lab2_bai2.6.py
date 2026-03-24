import random
# Thuật toán Miller-Rabin
def is_prime(n, k=5):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True
# Thuật toán Euclid tìm GCD 
def gcd(a, b):
    while b: a, b = b, a % b
    return a
#Tạo số nguyên tố
def gen_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if p % 2 != 0 and is_prime(p): return p
print(f"1. Số nguyên tố ngẫu nhiên: 8-bit: {gen_prime(8)}, 16-bit: {gen_prime(16)}, 64-bit: {gen_prime(64)}")
#Tìm 10 số nguyên tố < M10 (2^89 - 1)
m10 = 2**89 - 1
primes, cur = [], m10 - 1
while len(primes) < 10:
    if is_prime(cur): primes.append(cur)
    cur -= 1
print(f"2. 10 số nguyên tố < M10: {primes}")
print(f"3. GCD số lớn: {gcd(123456789101112, 987654321098765)}")
print(f"4. Kết quả 7^40 mod 19: {pow(7, 40, 19)}")
print("\n5. Kiểm tra số nguyên tố tùy ý:")
try:
    user_num = int(input("Nhập số cần kiểm tra (nhỏ hơn 2^89 - 1): "))
    if user_num < 2**89 - 1:
        if is_prime(user_num):
            print(f"   => {user_num} LÀ số nguyên tố.")
        else:
            print(f"   => {user_num} KHÔNG PHẢI là số nguyên tố.")
    else:
        print("   (!) Số bạn nhập lớn hơn hoặc bằng 2^89 - 1.")
except ValueError:
    print("   (!) Vui lòng nhập một số nguyên hợp lệ.")