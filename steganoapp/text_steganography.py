def encode_text(message, shift):
    return ''.join(chr((ord(char) - 32 + shift) % 95 + 32) for char in message)


def decode_text(encoded_message, shift):
    return ''.join(chr((ord(char) - 32 - shift) % 95 + 32) for char in encoded_message)
