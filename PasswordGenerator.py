import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "()[]{},;:._-/\/*-+?#"

upper, lower, nums, syms = True, True, True, True #Here you can choose that what you want in your password

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 10 #Here you can write the length of your password
amount = 1 #Here you can choose that how many passwords you want

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)