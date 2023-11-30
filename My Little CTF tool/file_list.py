import os

def get_file_list(path):
    repertoire = path
    dirs = [f for f in os.listdir(repertoire) if os.path.isdir(os.path.join(repertoire, f))]
    files = [f for f in os.listdir(repertoire) if os.path.isfile(os.path.join(repertoire, f))]
    elements = {"files":files,"dirs":dirs}
    return elements