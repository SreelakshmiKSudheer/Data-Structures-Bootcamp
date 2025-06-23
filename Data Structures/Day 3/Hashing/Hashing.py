# Division Method:
# This method uses the modulus operator to get the remainder when key is divided by table_size.
# It's simple and commonly used.
def hash_division(key, table_size):
    return key % table_size  # Returns a value between 0 and table_size - 1

# Mid-Square Method:
# This method first squares the key, then extracts the middle digits of the square,
# and then applies the modulus operation to get the hash.
def hash_mid_square(key, table_size):
    square = key * key  # Step 1: Square the key
    square_str = str(square)  # Convert the square to a string so we can get middle digits

    # Step 2: Get the middle 2 digits from the square
    mid = len(square_str) // 2  # Find the middle index
    # Take 2 middle digits (one before and one after the center)
    mid_digits = square_str[mid - 1:mid + 1] if len(square_str) >= 2 else square_str

    # Step 3: Convert the middle digits back to number and apply modulo
    return int(mid_digits) % table_size

# Folding Method:
# In this method, the key is broken into parts (usually of 2 digits),
# then all parts are added together and the sum is used to find the hash value.
def hash_folding(key, table_size):
    key_str = str(key)  # Convert key to string so we can slice it
    sum_parts = 0  # Initialize sum

    # Break the key into parts of 2 digits and sum them
    for i in range(0, len(key_str), 2):
        part = key_str[i:i+2]  # Get 2 digits at a time
        sum_parts += int(part)  # Convert to number and add to sum

    # Apply modulo to get final hash value
    return sum_parts % table_size

# --- User Input Section ---

# Ask the user to enter a numeric key (e.g., 1234)
key = int(input("Enter a numeric key: "))

# Ask the user to enter the hash table size (e.g., 10)
table_size = int(input("Enter the hash table size: "))

# Display the results of the three hashing methods
print("\nHash Values:")
print("1. Division Method:", hash_division(key, table_size))
print("2. Mid-Square Method:", hash_mid_square(key, table_size))
print("3. Folding Method:", hash_folding(key, table_size))
