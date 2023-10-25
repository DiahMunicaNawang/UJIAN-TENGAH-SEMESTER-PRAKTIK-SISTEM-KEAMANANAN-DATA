#!/usr/bin/env python
# coding: utf-8

# In[7]:


#!/usr/bin/env python
# coding: utf-8

# In[10]:


def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            encrypted_char = chr(((char_code + shift) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            decrypted_char = chr(((char_code - shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    key_index = 0 
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            key_char = key[key_index % key_length].lower()
            key_code = ord(key_char) - ord('a')
            encrypted_char = chr(((char_code + key_code) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
            key_index += 1  
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            key_char = key[key_index % key_length].lower()
            key_code = ord(key_char) - ord('a')
            decrypted_char = chr(((char_code - key_code) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

plaintext = "SUCCESS IS NOT FINAL, FAILURE IS NOT FATAL, IT IS COURAGE TO CONTINUE THAT COUNTS"
caesar_shift = 5
vigenere_key = "MONA"

# Enkripsi
caesar_encrypted = caesar_encrypt(plaintext, caesar_shift)
vigenere_encrypted = vigenere_encrypt(caesar_encrypted, vigenere_key)

print("Hasil Kombinasi (Enkripsi):", vigenere_encrypted)

# Dekripsi
vigenere_decrypted = vigenere_decrypt(vigenere_encrypted, vigenere_key)
caesar_decrypted = caesar_decrypt(vigenere_decrypted, caesar_shift)

print("Dekripsi :", caesar_decrypted)


# In[ ]:




