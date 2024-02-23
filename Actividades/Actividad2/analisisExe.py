import pefile as pe

# Cargamos el archivo
pe = pe.PE("./Actividades/Actividad2/suspicious.exe")

for section in pe.sections:
    print(section.Name.decode('utf-8') + " " + hex(section.VirtualAddress) + " " + hex(section.Misc_VirtualSize) + " " + hex(section.SizeOfRawData))

for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print("\nDLL:")
    print(entry.dll.decode('utf-8'))
    print("\nImports:")
    for imp in entry.imports:
        print(imp.name.decode('utf-8'))