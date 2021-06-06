from time import time
from Crypto.PublicKey import RSA
from base64 import b64decode
import pickle

# This is a modified script
# Source: https://stackoverflow.com/a/20087129/14033284

def _decrypt_rsa():
    '''
    Decrypt RSA encrypted package with private key
    :param decrypt_key_file: Private key
    :param cipher_text: Base64 encoded string to decrypt
    :return: String decrypted
    '''

    key     = open("key.pub", "r").read()
    rsakey  = RSA.importKey(key)
        
    with open("flag.txt", "rb") as cipher_text_file:
        cipher_text = cipher_text_file.read().strip() 
        raw_cipher_data = b64decode(cipher_text)

    decrypted       = rsakey.decrypt(raw_cipher_data)

    return decrypted


if __name__ == "__main__":
    start = time()
    print(f"Decrypted flag: { _decrypt_rsa() }") 
    print(f"Time Taken: { time() - start }ms")

