
from Crypto.Cipher import AES
from Crypto.Util import Padding
import os

original_plaintext = os.urandom(1000) 
key = b'1234567890123456' # Khóa 16 bytes
iv = b'1234567890123456'  # Vector

def test_error_propagation(mode_name, mode_type):
    if mode_name == 'ECB':
        cipher_enc = AES.new(key, mode_type)
        cipher_dec = AES.new(key, mode_type)
    else:
        cipher_enc = AES.new(key, mode_type, iv=iv)
        cipher_dec = AES.new(key, mode_type, iv=iv)

    ciphertext = bytearray(cipher_enc.encrypt(Padding.pad(original_plaintext, 16)))

    # làm hỏng = cách đảo bit đầu của byte 26 bằng phép XOR với 0x01
    ciphertext[26] ^= 0x01 

    decrypted_data = Padding.unpad(cipher_dec.decrypt(ciphertext), 16)

    print(f"\n--- Chế độ: {mode_name} ---")
    for i in range(0, 100, 16): # Kiểm tra
        block_original = original_plaintext[i:i+16]
        block_decrypted = decrypted_data[i:i+16]
        if block_original != block_decrypted:
            print(f"Khối {i//16} (byte {i}-{i+15}): BỊ HỎNG")
        else:
            print(f"Khối {i//16} (byte {i}-{i+15}): OK")

# Test
test_error_propagation('ECB', AES.MODE_ECB)
test_error_propagation('CBC', AES.MODE_CBC)
test_error_propagation('CFB', AES.MODE_CFB)
test_error_propagation('OFB', AES.MODE_OFB)