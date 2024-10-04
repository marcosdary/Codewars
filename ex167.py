from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path
from os import walk, path as path_f
ARQUIVO = Path().home() / 'Desktop' / 'Autoconsciência'
ARQUIVO_COMPACTADO = Path().home() / 'Desktop' / 'Autoconsciência.zip' 

def zipdir(path, zipf=None):
    for root, dirs, files in walk(path):
        for file in files:
            file_path = path_f.join(root, file)
            zipf.write(file_path, path_f.relpath(file_path, path_f.dirname(path)))

with ZipFile(ARQUIVO_COMPACTADO, 'w', ZIP_DEFLATED) as zipf:
    zipdir(ARQUIVO, zipf)