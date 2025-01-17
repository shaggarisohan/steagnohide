def encode_audio(audio_path, secret_message, output_path):
    audio = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    binary_msg = ''.join([format(ord(char), '08b') for char in secret_message])
    binary_msg += '1111111111111110'  # End of message delimiter

    data_index = 0
    for i in range(len(frame_bytes)):
        if data_index < len(binary_msg):
            frame_bytes[i] = (frame_bytes[i] & 254) | int(binary_msg[data_index])
            data_index += 1

    output_audio = wave.open(output_path, mode='wb')
    output_audio.setparams(audio.getparams())
    output_audio.writeframes(frame_bytes)
    output_audio.close()
    return True


def decode_audio(audio_path):
    audio = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    binary_msg = ''.join([str(frame_bytes[i] & 1) for i in range(len(frame_bytes))])
    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    decoded_message = ''.join([chr(int(char, 2)) for char in chars])
    return decoded_message.split('1111111111111110')[0]
