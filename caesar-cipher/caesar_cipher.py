alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']


def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == "encode":
        encrypt(plain_text=start_text, shift_amount=shift_amount)
    elif cipher_direction == "decode":
        decrypt(cipher_text=start_text, shift_amount=shift_amount)


def encrypt(plain_text, shift_amount):
    res = []
    for letter in plain_text:
        i = alphabet.index(letter)
        res.append(alphabet[(i + shift_amount) % len(alphabet)])
    print(f"Encoded message is {''.join(res)}")


def decrypt(cipher_text, shift_amount):
    res = []
    for letter in cipher_text:
        i = alphabet.index(letter)
        res.append(alphabet[(i + (len(alphabet) - shift_amount)) % len(alphabet)])
    print(f"Decoded message is {''.join(res)}")
