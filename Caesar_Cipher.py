
# Caesar Cipher

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
text = input("Type your message:").lower()
shift = int(input("Type the shift number:"))


def caesar(directions, txt, shift):
    new_code = ''
    if directions == 'decode':
        shift *= -1

    for letter in txt:
        ascii_val = ord(letter)
        new_code += chr(ascii_val + shift)

    print(f"Cipher word is {new_code}")


caesar(directions, text, shift)

