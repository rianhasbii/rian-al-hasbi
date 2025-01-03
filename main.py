import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

panjang_password = int(input("Berapa panjang passwordnya?"))
password = ""
for i in range(panjang_password):
    password += random.choice(elements)

print(password)