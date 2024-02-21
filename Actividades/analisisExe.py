import pefile as pe

# Cargamos el archivo
pe = pe.PE("C:/Users/Usuario/Desktop/Actividades/actividad2/putty.exe")

for section in pe.sections:
    print(section.Name.decode('utf-8') + " " + hex(section.VirtualAddress) + " " + hex(section.Misc_VirtualSize) + " " + hex(section.SizeOfRawData))

for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print("DLL:")
    print(entry.dll.decode('utf-8'))
    print("\nImports:")
    for imp in entry.imports:
        print(imp.name.decode('utf-8'))