def F(right, subkey):
    return (right ^ subkey) & 0x0F

def feistel_round(L_in, R_in, subkey):
    L_out = R_in
    R_out = L_in ^ F(R_in, subkey)
    return L_out, R_out

def track_avalanche(msg, key):
    L = (msg >> 4) & 0x0F
    R = msg & 0x0F
    
    subkeys = [
        key & 0x0F,         
        (key >> 4) & 0x0F,  
        (key + 1) & 0x0F,    
        (key + 2) & 0x0F    
    ]
    
    print(f"Khởi tạo: L={format(L, '04b')}, R={format(R, '04b')} (Hex: {hex(msg)})")
    
    for i in range(4):
        L, R = feistel_round(L, R, subkeys[i])
        print(f"Vòng {i+1}: L={format(L, '04b')}, R={format(R, '04b')}")
    
    return (L << 4) | R

key_input = 0x12

print("--- Mã hóa M1 ---")
res1 = track_avalanche(0xAB, key_input)

print("\n--- Mã hóa M2 ---")
res2 = track_avalanche(0xAC, key_input)