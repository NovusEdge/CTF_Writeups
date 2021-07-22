import codecs  

from time import time


def decode(s: str):
    rot13 = lambda s : codecs.getencoder("rot-13")(s)[0]

    return rot13(s)


if __name__ == "__main__":
    enc_flag = input("Enter flag: ")
    start = time()
    dec_flag = decode(enc_flag); end = time() - start

    print(f"\nDecoded flag: { dec_flag }")
    print(f"Time Taken: { end }\n")

