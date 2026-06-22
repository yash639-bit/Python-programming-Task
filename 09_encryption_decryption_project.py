def encrypt(text,key):
    r=""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                r+=chr((ord(ch)-65+key)%26+65)
            else:
                r+=chr((ord(ch)-97+key)%26+97)
        else:
            r+=ch
    return r

def decrypt(text,key):
    r=""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                r+=chr((ord(ch)-65-key)%26+65)
            else:
                r+=chr((ord(ch)-97-key)%26+97)
        else:
            r+=ch
    return r

while True:
    print("\n1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")
    choice=input("Enter choice: ")
    if choice=="1":
        msg=input("Enter message: ")
        key=int(input("Enter key: "))
        print("Encrypted:",encrypt(msg,key))
    elif choice=="2":
        msg=input("Enter encrypted message: ")
        key=int(input("Enter key: "))
        print("Decrypted:",decrypt(msg,key))
    elif choice=="3":
        break
    else:
        print("Invalid choice")
