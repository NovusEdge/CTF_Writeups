import string

from time import time


LETTERS      = string.ascii_letters.upper()*2
encoded_data = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }".split(' ')
decoded_nums = ""


for num in encoded_data:
    if num not in "{}":
        decoded_nums += LETTERS[int(num)-1]
    else:
        decoded_nums += num


print(f"The flag: {decoded_nums}")
