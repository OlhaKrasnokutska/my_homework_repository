def decrypt(message, key):
    decrypted = ""
    for char in message:
        if 'A' <= char <= 'Z':
            shift = (ord(char) - ord('A') - key) % 26
            decrypted += chr(ord('A') + shift)

        elif 'a' <= char <= 'z':
            shift = (ord(char) - ord('a') - key) % 26
            decrypted += chr(ord('a') + shift)

        elif char.isnumeric():
            decrypted += str(int(char) - abs(key))

        else:
            decrypted += char
    return decrypted


key_input = int(input("Enter key: "))
message_input = input("Enter message: ")

decrypted_message = decrypt(message_input, key_input)
print(f"Result: {decrypted_message}")