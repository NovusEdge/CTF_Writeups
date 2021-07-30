# import functools
#
# from time import time
#
#
# def sum_digits(number):
#     if len(str(number)) < 2:
#         return number
#
#     return sum(map( lambda x: int(x), str(number) ))
#
# def fancy(x, y):
#     return sum_digits(x*y) if x*y >= 10 else x*y
#
# def check_number(number):
#     num = str(number)
#
#     if len(num) < 6:
#         num = "0"*(6-len(num)) + num
#
#     fstr = f"543210{num}1234"
#
#     num_map = zip("212121", num)
#     temp_sum = sum(map(lambda x: fancy(int(x[0]), int(x[1])), num_map))
#
#     if 29 + temp_sum % 10 == 0 and int(str) % 123457 == 0:
#         return fstr
#
# def main():
#     for i in range(0, 999999):
#         num = check_number(i)
#         if num is not None:
#             return num
#
# if __name__ == '__main__':
#     start = time()
#     ans = main()
#     end = time() - start
#
#     print(f"Flag: {ans}")
#     print(f"Time Taken: {end}")

from luhn import *

cero = '0'
numero = 0
pre = '543210'
post = '1234'
parche = '000000'
str_numero = str(numero)

cc = pre + parche + post

while True:
    if numero == 1000000:
        break

    str_numero = str(numero)
    parche = (cero * (6 - len(str_numero)) + str_numero)
    cc = pre + parche + post

    if int(cc) % 123457 == 0:
        if verify(cc) == True:
            print(f'La tarjeta usada fue: {cc}')
            break

    numero = numero + 1
