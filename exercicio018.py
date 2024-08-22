# Objetivo: Copiar um arquivo de um diretório para outro.
# Tarefa:
# Crie um objeto Path para o arquivo de origem e para o diretório de destino.
# Verifique se o arquivo de origem existe e se o diretório de destino também existe.
# Se ambos existirem, copie o arquivo para o diretório de destino com o mesmo nome.

from pathlib import Path
from os import walk
from shutil import copy

DESKTOP = Path().home() / 'Desktop'
LOUCURA = DESKTOP / 'Loucura'
CONTRA_LOUCURA = DESKTOP / 'Contra Loucura'
CONTRA_LOUCURA.mkdir(exist_ok=True)

class ClonarPasta:
    def __init__(self, origem:Path, destino:Path) -> None:
        self.origem = origem
        self.destino = destino
        self.status = self.__camninho_existir()

    def __camninho_existir(self):
        return True if self.origem.exists() and self.destino.exists() else False
    
    def clonar(self):
        if not self.status:
            raise FileNotFoundError('Pasta não encontrada')

        def inner_clonar(origem:Path, destino:Path):
            for root, dirs, files in origem.walk():
                diretorio = Path(str(root).replace(str(self.origem), str(self.destino)))
                diretorio.mkdir(exist_ok=True)
            
                for file in files:
                    arquivo_origem = Path(root) / file
                    arquivo_destino = Path(str(arquivo_origem).replace(str(root), str(diretorio)))   
                    copy(arquivo_origem, arquivo_destino)    

            return True        

        return inner_clonar(self.origem, self.destino)

clonar_pasta = ClonarPasta(LOUCURA, CONTRA_LOUCURA)
print(clonar_pasta.clonar())

