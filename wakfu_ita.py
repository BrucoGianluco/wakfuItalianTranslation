import os
import requests
from tkinter import filedialog, Tk

# Funzione per scaricare il file da GitHub
def download_file(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

# Funzione per verificare se esiste la cartella di Wakfu
def check_wakfu_folder(folder_path):
    return os.path.exists(os.path.join(folder_path, 'zaap.yml'))

# Creazione della finestra di dialogo per la selezione della cartella di Wakfu
root = Tk()
root.withdraw()
wakfu_folder = filedialog.askdirectory(title="Seleziona la cartella di installazione di Wakfu")

# Verifica se la cartella di Wakfu è stata selezionata
if not wakfu_folder:
    print("Nessuna cartella di installazione di Wakfu selezionata.")
else:
    # Verifica se la cartella di Wakfu contiene il file zaap.yml
    if not check_wakfu_folder(wakfu_folder):
        print("Cartella di installazione di Wakfu non trovata.")
    else:
        # Scarica il file zaap.yml
        zaap_url = "https://raw.githubusercontent.com/BrucoGianluco/wakfuItalianTranslation/main/zaap.yml"
        zaap_file_path = os.path.join(wakfu_folder, 'zaap.yml')
        download_file(zaap_url, zaap_file_path)
        print("File zaap.yml scaricato correttamente.")

        # Copia il file i18n_it.jar nella cartella corretta
        i18n_url = "https://raw.githubusercontent.com/BrucoGianluco/wakfuItalianTranslation/main/i18n_en.jar"
        i18n_file_path = os.path.join(wakfu_folder, 'contents', 'i18n', 'i18n_en.jar')
        download_file(i18n_url, i18n_file_path)
        print("File i18n_it.jar scaricato correttamente e posizionato nella cartella di Wakfu.")
