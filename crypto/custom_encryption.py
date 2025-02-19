from random import randint
import sys


def first_var_raised_to_the_p_power_module_by_p(g, x, p):
    # function returns g raised to the x power, then divided by module p #
    return pow(g, x) % p


def STEP_TWO_encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def STEP_ONE_dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text


def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    # takes the two primes, and returns a number within ten of the prime given #
    a = randint(p-10, p)
    b = randint(g-10, g)
    print(f"a = {a}")
    print(f"b = {b}")

    #u is g^a%p
    u = first_var_raised_to_the_p_power_module_by_p(g, a, p)
    #v is g^b%p
    v = first_var_raised_to_the_p_power_module_by_p(g, b, p)
    #key is v^a%p
    key = first_var_raised_to_the_p_power_module_by_p(v, a, p)
    #bkey is u^b%p
    b_key = first_var_raised_to_the_p_power_module_by_p(u, b, p)

    shared_key = None
    #so if v^a%p = u^b%p, then share the key
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    # if all checks worked, then run dynamic xor
    semi_cipher = STEP_ONE_dynamic_xor_encrypt(plain_text, text_key)
    # cipher works by taking semi and applied key calculated bf!
    cipher = STEP_TWO_encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')


if __name__ == "__main__":
    message = sys.argv[1]
    test(message, "trudeau")
