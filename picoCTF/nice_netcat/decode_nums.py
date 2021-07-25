import sys

from time import time


def decode_flag():
    file_path = sys.argv[1]
    decoded_flag = ""

    with open(file_path, "r") as f:
        data = f.read().split()

        decoded_flag += ''.join(map(lambda x: chr(int(x)), data))

    return decoded_flag


if __name__ == '__main__':
    start = time()
    flag = decode_flag()

    print(f"\nThe flag is: { flag }")
    print(f"Time Taken: { time() - start }\n")
