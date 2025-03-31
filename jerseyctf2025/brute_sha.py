import hashlib
import binascii
import itertools
import string

def try_message_pbkdf2(message, salt, original_hash, iterations, key_length, algorithm):
    """Hashes a message using PBKDF2-HMAC and compares it to the given hash."""
    derived_key = hashlib.pbkdf2_hmac(algorithm, message.encode(), salt.encode(), iterations, dklen=key_length)
    return binascii.hexlify(derived_key).decode() == original_hash

def brute_force_pbkdf2(salt, original_hash, iterations, key_length, max_length=6, algorithm='sha256'):
    """Brute-force all possible combinations of characters up to max_length"""
    characters = string.ascii_letters + string.digits  # Letters + digits (expand as needed)
    
    # Generate all possible combinations up to max_length
    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            message = ''.join(combination)  # Combine tuple into a string
            if try_message_pbkdf2(message, salt, original_hash, iterations, key_length, algorithm):
                print(f"✅ Original message found: {message}")
                return message
    print("❌ No match found.")
    return None

# 🔹 Replace with your actual values
salt = "337732746345653074784a63663675364552517942773d3d"
original_hash = "gAAAAABnuPB37lcJBTXH4v6DImWCOjQZMpgk1-5S8A2gSgVCrZJGsPgyQ6QH9iC3-8W9_WanbHr-KKYdzAfajwYMZGlXGs9IRnlTPdbM2_RA8ZkONRXxoOk="
iterations = 100  # Example value, adjust accordingly
key_length = 32  # Length of the derived key in bytes (e.g., 32 for SHA-256)
hash_algorithm = "sha256"  # Ensure this matches the original hashing function

# Run brute-force for combinations up to length 4 (or adjust max_length for higher lengths)
max_length = 4  # Adjust based on the expected length of the message
brute_force_pbkdf2(salt, original_hash, iterations, key_length, max_length, hash_algorithm)
