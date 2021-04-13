import simplecrypt

with open('encrypted.bin', 'rb') as inp1, open('passwords.txt', 'r') as passwords:
    encrypted = inp1.read()
    for password in passwords:
        try:
            info = simplecrypt.decrypt(password.strip(), encrypted)
        except simplecrypt.DecryptionException:
            continue
        else:
            print(info)
            break
