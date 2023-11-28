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

some_data = get_file_sigs_from_json(os.getcwd()+'\\'+'file_sigs.json')
some_info = get_file_sig_info(some_data[0])
print(some_info)