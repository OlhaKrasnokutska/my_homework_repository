def encrypt(message, key):
    encrypted = ""
    for char in message:
        if 'A' <= char <= 'Z':
            shift = (ord(char) - ord('A') + key) % 26
            encrypted += chr(ord('A') + shift)

        elif 'a' <= char <= 'z':
            shift = (ord(char) - ord('a') + key) % 26
            encrypted += chr(ord('a') + shift)

        # decided to add numbers also to encryption:
        elif char.isnumeric():
            encrypted += str(int(char) + abs(key))

        # for other symbols:
        else:
            encrypted += char
    return encrypted


key_input = int(input("Enter key: "))
message_input = input("Enter message: ")

encrypted_message = encrypt(message_input, key_input)
print(f"Result: {encrypted_message}")
