def encode_image(image_path, secret_message, output_path):
    img = cv2.imread(image_path)
    binary_msg = ''.join([format(ord(char), '08b') for char in secret_message])
    binary_msg += '1111111111111110'  # End of message delimiter
    
    data_index = 0
    msg_len = len(binary_msg)
    for row in img:
        for pixel in row:
            for color_index in range(3):  # RGB channels
                if data_index < msg_len:
                    pixel[color_index] = int(format(pixel[color_index], '08b')[:-1] + binary_msg[data_index], 2)
                    data_index += 1
    
    cv2.imwrite(output_path, img)
    return True


def decode_image(image_path):
    img = cv2.imread(image_path)
    binary_msg = ''
    for row in img:
        for pixel in row:
            for color_index in range(3):  # RGB channels
                binary_msg += format(pixel[color_index], '08b')[-1]

    # Split the binary string into 8-bit chunks
    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    decoded_message = ''.join([chr(int(char, 2)) for char in chars])
    return decoded_message.split('1111111111111110')[0]
