import hashlib

with open('c0_body.bin', 'rb') as f:
    body_data = f.read()
my_hash = hashlib.sha256(body_data).hexdigest()

with open('modulus_n.txt', 'r') as f:
    n_hex = f.read().strip()
with open('signature.txt', 'r') as f:
    sig_hex = f.read().strip()

n = int(n_hex, 16)
e = 65537
sig = int(sig_hex, 16)
#Giai ma RSA
decrypted_msg = pow(sig, e, n)
decrypted_hex = hex(decrypted_msg)

print(f"KẾT QUẢ ")
print(f"Mã băm SHA-256 tự tính (Hash): {my_hash}")
print(f"Dữ liệu giải mã RSA: {decrypted_hex}")

if my_hash in decrypted_hex:
    print("\n=> KẾT LUẬN: CHỨNG CHỈ HỢP LỆ! (Mã băm khớp)")
else:
    print("\n=> KẾT LUẬN: CHỨNG CHỈ KHÔNG HỢP LỆ!")
