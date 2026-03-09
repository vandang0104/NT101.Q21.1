import string
from collections import Counter

ENGLISH_FREQS = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074
]

def clean_text(text):
    """Lọc bỏ khoảng trắng, dấu câu và viết hoa toàn bộ"""
    return ''.join(c.upper() for c in text if c.isalpha())

def calculate_ioc(text):
    """Tính Chỉ số trùng hợp (Index of Coincidence)"""
    n = len(text)
    if n <= 1:
        return 0.0
    
    counts = Counter(text)
    ioc = sum(f * (f - 1) for f in counts.values())
    return ioc / (n * (n - 1))

def guess_key_length(cipher, max_len=20):
    """Đoán độ dài khóa dựa trên IoC gần với 0.065 nhất"""
    best_len = 1
    best_diff = float('inf')
    target_ioc = 0.065

    for length in range(1, max_len + 1):
        columns = [cipher[i::length] for i in range(length)]
        avg_ioc = sum(calculate_ioc(col) for col in columns) / length

        if abs(avg_ioc - target_ioc) < best_diff:
            best_diff = abs(avg_ioc - target_ioc)
            best_len = length

    return best_len

def guess_key(cipher, key_length):
    """Đoán từng ký tự khóa bằng kiểm định Chi-square"""
    key = ""
    for i in range(key_length):
        column = cipher[i::key_length]
        col_len = len(column)
        min_chisq = float('inf')
        best_shift = 0

        for shift in range(26):
            chi_sq = 0.0
            decrypted_col = [chr(((ord(c) - 65 - shift) % 26) + 65) for c in column]
            counts = Counter(decrypted_col)

            for k in range(26):
                char = chr(k + 65)
                observed = counts.get(char, 0)
                expected = ENGLISH_FREQS[k] * col_len
                
                if expected > 0:
                    chi_sq += ((observed - expected) ** 2) / expected

            if chi_sq < min_chisq:
                min_chisq = chi_sq
                best_shift = shift

        key += chr(best_shift + 65)
    
    return key

def decrypt_vigenere(cipher, key):
    """Giải mã Vigenere khi đã biết khóa"""
    plain = []
    key_len = len(key)
    for i, c in enumerate(cipher):
        c_val = ord(c) - 65
        k_val = ord(key[i % key_len]) - 65
        plain.append(chr(((c_val - k_val) % 26) + 65))
    return ''.join(plain)

def main():
    print("=== CHUONG TRINH PHA MA VIGENERE (PYTHON) ===")
    user_input = input("Nhap Ciphertext (co the chua khoang trang/dau cau):\n> ")
    cipher = clean_text(user_input)

    if not cipher:
        print("Vui long nhap chuoi hop le.")
        return

    if len(cipher) < 30:
        print("\n[Canh bao]: Ciphertext qua ngan (duoi 30 ky tu). Thong ke co the bi sai lech!")

    key_length = guess_key_length(cipher)
    predicted_key = guess_key(cipher, key_length)
    plaintext = decrypt_vigenere(cipher, predicted_key)

    print("\n--- KET QUA PHAN TICH ---")
    print(f"- Do dai khoa du doan : {key_length}")
    print(f"- Khoa tim duoc       : {predicted_key}")
    print(f"- Ban ro (Plaintext)  :\n{plaintext}")
    print("-------------------------")

if __name__ == "__main__":
    main()