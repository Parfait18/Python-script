def increment_file_name(file_name):
    # Extraire le numéro du fichier s'il existe
    match = re.match(r"(.*?)(\d+)(\.\w+)$", file_name)
    if match:
        base_name = match.group(1)
        number = int(match.group(2))
        extension = match.group(3)
        # Incrémenter le numéro du fichier
        new_file_name = f"{base_name}{number + 1}{extension}"
    else:
        # Si aucun numéro n'est trouvé, ajouter 2
        base_name, extension = os.path.splitext(file_name)
        new_file_name = f"{base_name}2{extension}"
    return new_file_name


directory = "/chemin/vers/le/repertoire"
file_name = "book2.csv"  # Nom du fichier que vous voulez incrémenter
full_path = os.path.join(directory, file_name)
