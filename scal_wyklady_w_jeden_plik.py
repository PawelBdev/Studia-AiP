import os

def merge_files_in_folder(folder_path, output_file_path):
    # Otwórz plik wynikowy w trybie do zapisu
    with open(output_file_path, 'w') as output_file:
        # Przechodź przez wszystkie pliki w folderze
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Sprawdź, czy to plik tekstowy
            if os.path.isfile(file_path) and filename.endswith('.py'):
                # Kopiuj nazwę pliku w cudzysłowie i zapisz do pliku wynikowego

                output_file.write(f'"{filename}"\n')

                # Kopiuj zawartość pliku i zapisz do pliku wynikowego
                with open(file_path, 'r') as input_file:
                    output_file.write(input_file.read())
                    
                # Dodaj odstęp pomiędzy plikami
                output_file.write('\n\n')
                output_file.write(f'{"#" * 50} \n\n')

# Ścieżka do folderu z plikami tekstowymi
# folder_path = '/ścieżka/do/twojego/folderu'
folder_path = '/home/paweb/Studia/AiP/WYKLADY'

# Ścieżka do pliku wynikowego
# output_file_path = '/ścieżka/do/twojego/folderu/wynik.txt'
output_file_path = '/home/paweb/Studia/AiP/wyklady_razem_v3.py'

# Wywołaj funkcję do scalenia plików
merge_files_in_folder(folder_path, output_file_path)

print("Operacja zakończona.")
