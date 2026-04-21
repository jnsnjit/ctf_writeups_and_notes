# zero_width_decoder_full.py

ZERO_WIDTH_BLOB = "\u200C\u200B\u200B\u200B\u200B\u200B\u200C\u200C\u200C\u200C\u2060\u200C\u200C\u200B\u200C\u200C\u200C\u200C\u2060\u200C\u200B\u200B\u200B\u200B\u200B\u2060\u200C\u200C\u200C\u200B\u200C\u200B\u200B\u2060\u200C\u200C\u200B\u200C\u200C\u200C\u200C\u2060\u200C\u200B\u200B\u200B\u200B\u200B\u2060\u200C\u200B\u200C\u200C\u200C\u200C\u2060\u200C\u200C\u200B\u200C\u200C\u200B\u200C\u2060\u200C\u200C\u200C\u200C\u200B\u200B\u200C\u2060\u200C\u200B\u200C\u200C\u200B\u200C\u2060\u200C\u200C\u200B\u200C\u200B\u200B\u200B\u2060\u200C\u200C\u200B\u200C\u200B\u200B\u200C\u2060\u200C\u200C\u200B\u200B\u200C\u200B\u200B\u2060\u200C\u200C\u200B\u200B\u200C\u200B\u200B\u2060\u200C\u200C\u200B\u200B\u200C\u200B\u200C\u2060\u200C\u200C\u200B\u200C\u200C\u200C\u200B\u2060\u200C\u200B\u200C\u200C\u200B\u200C\u2060\u200C\u200C\u200B\u200B\u200B\u200C\u200B\u2060\u200C\u200C\u200B\u200C\u200C\u200B\u200B\u2060\u200C\u200C\u200B\u200C\u200C\u200C\u200C\u2060\u200C\u200C\u200B\u200B\u200C\u200C\u200C\u200C"
binary_value = {' ': '\u2060', '0': '\u200B', '1': '\u200C'}
reverse_binary_val = {v: k for k, v in binary_value.items()}

def encode(secret_text, normal_text):
    bin_text = ""
    encoded_text = normal_text
    bin_text = ' '.join(format(ord(x), 'b') for x in secret_text)
    for b in bin_text:
        encoded_text +=  binary_value[b]
    return encoded_text

def decode(given_text):
    bin_text = ""
    for w in given_text:
        if w in reverse_binary_val:
            bin_text += reverse_binary_val[w]
    bin_val = bin_text.split()
    secret_text = ""
    for b in bin_val:
        secret_text += chr(int(b, 2))
    return secret_text

to_decode = input("Input the encoded message: ")
print(decode(to_decode))