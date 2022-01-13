import caesar_cipher
import art

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar_cipher.caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
