from Crypto.Cipher import DES

def count_diff_bits(bytes1, bytes2):
    int1 = int.from_bytes(bytes1, 'big')
    int2 = int.from_bytes(bytes2, 'big')
    
    diff = int1 ^ int2
    
    return bin(diff).count('1')

def avalanche_test(student_id_key):
    key = student_id_key.encode('utf-8')[:8].ljust(8, b'0')
    p1 = b'STAYHOME'
    p2 = b'STAYHOMA'
    
    cipher = DES.new(key, DES.MODE_ECB)
    c1 = cipher.encrypt(p1)
    c2 = cipher.encrypt(p2)
    
    b1 = bin(int.from_bytes(c1, 'big'))[2:].zfill(64)
    b2 = bin(int.from_bytes(c2, 'big'))[2:].zfill(64)

    diff_bits = count_diff_bits(c1, c2)
    percentage = (diff_bits / 64) * 100
    
    print(f"Key đang dùng: {key.decode()}")
    print(f"C1 (bin): {b1}")
    print(f"C2 (bin): {b2}")
    print(f"Số bit khác nhau (Hamming Distance): {diff_bits}")
    print(f"Tỷ lệ thay đổi: {percentage:.2f}%\n")
    
    return percentage

mssv_list = ["24521974", "21529999"]
for mssv in mssv_list:
    avalanche_test(mssv)