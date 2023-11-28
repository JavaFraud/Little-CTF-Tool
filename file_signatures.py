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

def get_file_header_info(file_hex, file_sigs: dict):
    for file_sig in file_sigs:
        if file_hex[0:len(file_sig["Header (hex)"].lower().replace(' ',''))] == file_sig["Header (hex)"].lower().replace(' ',''):
            result = get_file_sig_info(file_sig)
    return result
#-----------------------------------------------------------

#file_to_analyse_path = os.getcwd()+'\\'+'testFile.png'
#file_sigs_json_path = os.getcwd()+'\\'+'file_sigs.json'

#file_to_analyse_hex = read_file_hex(file_to_analyse_path)
#file_sigs = get_file_sigs_from_json(file_sigs_json_path)

#result = get_file_header_info(file_to_analyse_hex, file_sigs)
#print(result)