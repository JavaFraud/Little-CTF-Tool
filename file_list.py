import os

def get_file_list(path):
    repertoire = path
    fichiers = [f for f in os.listdir(repertoire) if os.path.isfile(os.path.join(repertoire, f))]
    return fichiers