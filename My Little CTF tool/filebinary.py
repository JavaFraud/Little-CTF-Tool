import binascii

def read_file_hex(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
        hex_data = binascii.hexlify(binary_data).decode('utf-8')
        return hex_data