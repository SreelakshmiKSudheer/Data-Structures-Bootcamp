def hash_division(key, table_size):
    return key % table_size

def hash_mid_square(key, table_size):
    square = key * key
    square_str = str(square)
    
    mid = len(square_str) // 2
    mid_digits = square_str[mid - 1:mid + 1] if len(square_str) >= 2 else square_str
    
    return int(mid_digits) % table_size

def hash_folding(key, table_size):
    key_str = str(key)
    sum_parts = 0
    for i in range(0, len(key_str), 2):
        part = key_str[i:i+2]
        sum_parts += int(part)
    return sum_parts % table_size

# --- User Input ---
key = int(input("Enter a numeric key: "))
table_size = int(input("Enter the hash table size: "))

print("\nHash Values:")
print("1. Division Method:", hash_division(key, table_size))
print("2. Mid-Square Method:", hash_mid_square(key, table_size))
print("3. Folding Method:", hash_folding(key, table_size))
