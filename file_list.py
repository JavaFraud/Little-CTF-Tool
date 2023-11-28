# Spécifiez le chemin du répertoire
repertoire = os.getcwd()

# Obtenez la liste des fichiers dans le répertoire
fichiers = [f for f in os.listdir(repertoire) if os.path.isfile(os.path.join(repertoire, f))]

# Affichez la liste des fichiers
print(fichiers)