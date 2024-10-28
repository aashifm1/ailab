import random
import string
def gen_psw(length):
    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    digits=string.digits
    special=string.punctuation
    all_char=upper+lower+digits
    x=input("Need special character? (yes/no): ")
    if x=="yes":
        all_char+=special
    psw=''.join(random.choice(all_char) for _ in range(length))
    return psw
length=int(input("\nEnter the length of password: "))
print("Generate password:",gen_psw(length))