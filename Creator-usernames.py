import argparse

parser = argparse.ArgumentParser(description='Genera nombres de usuario de AD basados en Nombre y Apellido')
parser.add_argument('filename', metavar="File", type=str, help='Archivo TXT que contiene la lista de usuarios')
args = parser.parse_args()

def opentxt(filename):
    name_list = []
    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 2:
                    name_list.append([parts[0], parts[1]])
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no se pudo encontrar.")
        exit()
    except Exception as e:
        print(f"Error: {e}")
        exit()
    return name_list

def main():
    name_list = opentxt(args.filename)
    for row in name_list:
        name = row[0].strip().lower()
        surname = row[1].strip().lower()

        print(f"Generando nombres para: {name.capitalize()} {surname.capitalize()}")
        print(name)                        # Nombre
        print(name + surname)              # NombreApellido
        print(name + "-" + surname)        # Nombre-Apellido
        print(name + "." + surname)        # Nombre.Apellido
        print(name[:3] + surname[:3])      # NomApe
        print(name[:3] + "-" + surname[:3])  # Nom-Ape
        print(name[:3] + "." + surname[:3])  # Nom.Ape
        print(name[0] + surname)           # N Apellido
        print(name[0] + "-" + surname)     # N-Apellido
        print(name[0] + "." + surname)     # N.Apellido
        print(surname + name)              # ApellidoNombre
        print(surname + "-" + name)        # Apellido-Nombre
        print(surname + "." + name)        # Apellido.Nombre
        print(surname[:3] + name[:3])      # ApeNom
        print(surname[:3] + "-" + name[:3])  # Ape-Nom
        print(surname[:3] + "." + name[:3])  # Ape.Nom
        print(surname[0] + name)           # ANombre
        print(surname[0] + "-" + name)     # A-Nombre
        print(surname[0] + "." + name)     # A.Nombre
        print(surname + name[0])           # ApellidoN
        print(surname + "-" + name[0])     # Apellido-N
        print(surname + "." + name[0])     # Apellido.N


if __name__ == "__main__":
    main()