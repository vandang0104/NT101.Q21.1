from Crypto.Cipher import AES

my_key = b'1234567890123456'
raw_data = b"UIT_LAB_UIT_LAB_UIT_LAB_UIT_LAB_" 
ma_hoa_ecb = AES.new(my_key, AES.MODE_ECB)
ban_ma_ecb = ma_hoa_ecb.encrypt(raw_data)

my_iv = b'0000000000000000'
ma_hoa_cbc = AES.new(my_key, AES.MODE_CBC, iv=my_iv)
ban_ma_cbc = ma_hoa_cbc.encrypt(raw_data)

print(f"Ket qua ECB: {ban_ma_ecb.hex()}")
print(f"Ket qua CBC: {ban_ma_cbc.hex()}")

block1_ecb = ban_ma_ecb.hex()[:32]
block2_ecb = ban_ma_ecb.hex()[32:]
print(f"ECB Block 1: {block1_ecb}")
print(f"ECB Block 2: {block2_ecb}")


block1_cbc = ban_ma_cbc.hex()[:32]
block2_ecb = ban_ma_cbc.hex()[32:]
print(f"CBC Block 1: {block1_ecb}")
print(f"CBC Block 2: {block2_ecb}")