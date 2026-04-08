import base64

def calculate_rsa_keys(p, q, e):
    # 1. Tính n
    n = p * q
    
    # 2. Tính phi(n)
    phi = (p - 1) * (q - 1)
    
    # 3. Tính d (nghịch đảo modulo của e theo phi)
    try:
        d = pow(e, -1, phi)
    except ValueError:
        return "Lỗi: e và phi(n) không nguyên tố cùng nhau."
    
    return n, d

p1 = 11
q1 = 17
e1 = 7

n1, d1 = calculate_rsa_keys(p1, q1, e1)
print("--- Trường hợp 1 ---")
print(f"PU = ({e1}, {n1})")
print(f"PR = ({d1}, {n1})\n")

p2 = 20079993872842322116151219
q2 = 676717145751736242170789
e2 = 17

n2, d2 = calculate_rsa_keys(p2, q2, e2)
print("--- Trường hợp 2 ---")
print(f"PU = ({e2}, {n2})")
print(f"PR = ({d2}, {n2})\n")

# Chuyển đổi chuỗi Hex sang số nguyên hệ 10 để tính toán
p3 = int("F7E75FDC469067FFDC4E847C51F452DF", 16)
q3 = int("E85CED54AF57E53E092113E62F436F4F", 16)
e3 = int("0D88C3", 16)

n3, d3 = calculate_rsa_keys(p3, q3, e3)

# Chuyển kết quả ngược lại sang dạng Hex 
n3_hex = hex(n3)[2:].upper()
d3_hex = hex(d3)[2:].upper()
e3_hex = hex(e3)[2:].upper()

print("--- Trường hợp 3 (Hiển thị dưới dạng Hex) ---")
print(f"PU = ({e3_hex}, {n3_hex})")
print(f"PR = ({d3_hex}, {n3_hex})")



# --- CÂU 2: MÃ HÓA M = 5 VỚI KHÓA 1 ---
print("\n=== KẾT QUẢ CÂU 2 ===")
M = 5

# Tính bảo mật : Mã hóa bằng PU (e), giải bằng PR (d)
c_bao_mat = pow(M, e1, n1)
m_giai_ma = pow(c_bao_mat, d1, n1)
print(f"1. Bảo mật:  Bản mã C = {c_bao_mat} ---> Giải mã ra = {m_giai_ma}")

# Tính xác thực : Mã hóa bằng PR (d), giải bằng PU (e)
c_xac_thuc = pow(M, d1, n1)
m_xac_minh = pow(c_xac_thuc, e1, n1)
print(f"2. Xác thực: Chữ ký C = {c_xac_thuc} ---> Xác minh ra = {m_xac_minh}")


# ===============================================
# --- CÂU 3: MÃ HÓA CHUỖI  ---
# ===============================================
print("\n=== KẾT QUẢ CÂU 3 ===")
chuoi_can_ma_hoa = "The University of Information Technology"

k3 = (n3.bit_length() + 7) // 8
chunk_size = k3 - 1 

chuoi_bytes = chuoi_can_ma_hoa.encode('utf-8')
ban_ma_bytes_tong = b''

# Băm chuỗi ra thành từng khúc nhỏ để mã hóa
for i in range(0, len(chuoi_bytes), chunk_size):
    chunk = chuoi_bytes[i:i+chunk_size]
    chunk_so_nguyen = int.from_bytes(chunk, byteorder='big')
    
    # Mã hóa khúc này: C = M^e mod n
    c_so = pow(chunk_so_nguyen, e3, n3)
    
    # Ép cục số bản mã về lại đúng k3 byte rồi nối vào chuỗi tổng
    ban_ma_bytes_tong += c_so.to_bytes(k3, byteorder='big')

# Encode Base64 in ra màn hình
ban_ma_b64 = base64.b64encode(ban_ma_bytes_tong).decode('utf-8')
print(f"Chuỗi gốc dài {len(chuoi_bytes)} bytes. Cắt thành các block {chunk_size} bytes để mã hóa.")
print("Bản mã Base64 là:", ban_ma_b64)


# ===============================================
# --- CÂU 4: GIẢI MÃ TÌM BẢN RÕ  ---
# ===============================================

print("\n=== KẾT QUẢ CÂU 4 ===")

danh_sach_khoa = [
    ("Khóa 1", d1, n1),
    ("Khóa 2", d2, n2),
    ("Khóa 3", d3, n3)
]

c1_b64 = "raUcesUlOkx/8ZhgodMoo0Uu18sC20yXlQFevSu7W/FDxIy0YRHMyXcHdD9PBvIT2aUft5fCQEGomiVVPv4I"
c2_hex = "C87F570FC4F699CEC24020C6F54221ABAB2CE0C3"
c3_b64 = "Z2BUSkJcg0w4XEpgm0JcMExEQmBlVH6dYEpNTHpMHptMQ7NgTHlgQrNMQ2BKTQ=="
c4_bin = "001010000001010011111111101101110010111011001010111011000110011110111111001111110110100011001111001100001001010001010100111101010100110011101110111011110101101100000100"

c1_bytes = base64.b64decode(c1_b64)
c2_bytes = bytes.fromhex(c2_hex)
c3_bytes = base64.b64decode(c3_b64)
c4_so = int(c4_bin, 2)
c4_bytes = c4_so.to_bytes((len(c4_bin) + 7) // 8, byteorder='big')

danh_sach_ban_ma = [
    ("Bản mã 1 (Base64)", c1_bytes),
    ("Bản mã 2 (Hex)", c2_bytes),
    ("Bản mã 3 (Base64)", c3_bytes),
    ("Bản mã 4 (Binary)", c4_bytes)
]

for ten_ban_ma, ban_ma_bytes in danh_sach_ban_ma:
    print(f"\nĐang thử mở {ten_ban_ma}...")
    mo_thanh_cong = False

    for ten_khoa, d, n in danh_sach_khoa:
        k = (n.bit_length() + 7) // 8  
        
        so_du = len(ban_ma_bytes) % k
        if so_du != 0:
            ban_ma_bytes_padded = (b'\x00' * (k - so_du)) + ban_ma_bytes
        else:
            ban_ma_bytes_padded = ban_ma_bytes

        giai_ma_bytes = b''
        for i in range(0, len(ban_ma_bytes_padded), k):
            block = ban_ma_bytes_padded[i:i+k]
            
            c = int.from_bytes(block, 'big')
            m = pow(c, d, n)

            m_bytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')
            giai_ma_bytes += m_bytes

        try:
            text = giai_ma_bytes.decode('utf-8')
            
            if text.strip() != "" and text.isprintable():
                print(f" -> THÀNH CÔNG! Dùng {ten_khoa}: '{text}'")
                mo_thanh_cong = True
                break
        except Exception:
            pass

    if not mo_thanh_cong:
        print(" -> Thất bại!")