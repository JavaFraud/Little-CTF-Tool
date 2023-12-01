import json
import os

def get_timestamps_from_json(path: str):
    with open(path) as file:
        data = json.load(file)
        all_patterns = data["time stamps patterns"]
    return all_patterns

def get_file_metadata(file_path):
    if os.path.exists(file_path):
        file_stat = os.stat(file_path)
        file_metadata = {
            "size_bytes" : file_stat.st_size,
            "A" : file_stat.st_atime,
            "M" : file_stat.st_mtime,
            "C" : file_stat.st_ctime
        }
        return file_metadata
    else:
        return "No MetaData were found"

def timestamp_pattern_equation(pattern,A,C,M):
    result = False
    parts = pattern.split(" ")
    for i, part in enumerate(parts):
        if part == "=":
            parts[i] = "=="
    condition = f"{parts[0]} {parts[1]} {parts[2]}"+" and "+f"{parts[2]} {parts[3]} {parts[4]}"
    condition.replace('=','==')
    result = eval(condition)
    return result

def get_associated_patterns(all_patterns: dict, file_metadatas: dict):
    patterns_informations = {}
    for i, pattern in enumerate(all_patterns):
        is_pattern = timestamp_pattern_equation(pattern["pattern"],file_metadatas['A'],file_metadatas['C'],file_metadatas['M'])
        if is_pattern:
            patterns_informations["pattern"] = pattern["pattern"]
            patterns_informations["description"] = pattern["description"]
    return patterns_informations

def get_timestamps_patterns_info(file_path,timestamps_path):
    all_patterns = get_timestamps_from_json(timestamps_path)
    file_metadatas = get_file_metadata(file_path)
    infos = get_associated_patterns(all_patterns,file_metadatas)
    result ="""Modification: {}
Access: {}
Creation: {}
Pattern: {}
Information: {}""".format(
        str(file_metadatas["M"]),
        str(file_metadatas["A"]),
        str(file_metadatas["C"]),
        infos["pattern"],
        infos["description"])
    return result