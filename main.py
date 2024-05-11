def encrypt(plaintext, key):
    # convert plaintext to list of numbers, as `ord` gives the numerical value of the char relative to 'A' (0 for 'A', 1 for 'B', etc.).
    plaintext_nums = [ord(c) - ord('A') for c in plaintext.upper()]

    # apply enc formula: f(p) = (p + k) mod m
    m = 26  # size of the alphapet
    ciphertext_nums = [(num + key) % m for num in plaintext_nums]

    # convert numbers back to chars
    ciphertext = ''.join(chr(num + ord('A')) for num in ciphertext_nums)
    return ciphertext


def decrypt(ciphertext, key):
    # convert ciphertext to list of numbers
    ciphertext_nums = [ord(c) - ord('A') for c in ciphertext.upper()]

    # apply dec formula: f^-1(p) = (p - k) mod m, this time i set it to - to undo the shift operation in ecryption
    m = 26  # Size of the alphabet
    plaintext_nums = [(num - key) % m for num in ciphertext_nums]

    # convert numbers back to chars
    plaintext = ''.join(chr(num + ord('A')) for num in plaintext_nums)
    return plaintext


plaintext = "STOP GLOBAL WARMING"
# we set this key is a numerical value determines how the plaintext is shifted during the enc and dec processes
key = 11
ciphertext = encrypt(plaintext, key)
print("plaintext:", plaintext)
print("ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("decrypted text:", decrypted_text)
