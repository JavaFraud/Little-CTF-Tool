import binascii
import json
import os

def get_file_sigs_from_json(path: str):
    with open(path) as file:
        file_sigs_file = json.load(file)
        all_file_sigs = file_sigs_file["filesigs"]
    return all_file_sigs

def get_file_sig_info(some_file_sig: dict):
    return """
    File description: {}
    Header (hex): {}
    File extension: {}
    FileClass: {}
    Header offset: {}
    Trailer (hex): {}
    """.format(
    some_file_sig["File description"],
    some_file_sig["Header (hex)"],
    some_file_sig["File extension"],
    some_file_sig["FileClass"],
    some_file_sig["Header offset"],
    some_file_sig["Trailer (hex)"])

def read_file_hex(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
        hex_data = binascii.hexlify(binary_data).decode('utf-8')
        return hex_data

#-----------------------------------------------------------

file_to_analyse_path = os.getcwd()+'\\'+'BurningKermit.jpg'
file_sigs_json_path = os.getcwd()+'\\'+'file_sigs.json'

file_to_alayse_hex_format = read_file_hex(file_to_analyse_path)

some_data = get_file_sigs_from_json(file_sigs_json_path)

for file_sig in some_data:
    if file_to_alayse_hex_format[0:len(file_sig["Header (hex)"].lower().replace(' ',''))] == file_sig["Header (hex)"].lower().replace(' ',''):
        print(get_file_sig_info(file_sig))

# Longest header
# 3C 3F 78 6D 6C 20 76 65 72 73 69 6F 6E 3D 22 31 2E 30 22 3F 3E 0D 0A 3C 4D 4D 43 5F 43 6F 6E 73 6F 6C 65 46 69 6C 65 20 43 6F 6E 73 6F 6C 65 56 65 72 73 69 6F 6E 3D 22