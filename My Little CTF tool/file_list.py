import os

def get_file_list(path):
    repertoire = path
    dirs = os.listdir(os.getcwd())
    dirs_iterate = dirs.copy()
    for element in dirs_iterate:
        if not os.path.isdir(os.getcwd()+"\\"+ element):
            dirs.remove(element)
    files = [f for f in os.listdir(repertoire) if os.path.isfile(os.path.join(repertoire, f))]
    elements = {"files":files,"dirs":dirs}
    return elements