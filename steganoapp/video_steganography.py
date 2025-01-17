def encode_video(video_path, secret_message, output_path):
    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    binary_msg = ''.join([format(ord(char), '08b') for char in secret_message])
    binary_msg += '1111111111111110'  # End of message delimiter

    data_index = 0
    msg_len = len(binary_msg)
    encoded = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if not encoded:
            for row in frame:
                for pixel in row:
                    for color_index in range(3):  # RGB channels
                        if data_index < msg_len:
                            pixel[color_index] = int(format(pixel[color_index], '08b')[:-1] + binary_msg[data_index], 2)
                            data_index += 1
                        if data_index >= msg_len:
                            encoded = True
                            break

        out.write(frame)

    cap.release()
    out.release()
    return True
