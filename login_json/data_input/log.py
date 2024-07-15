import os 
import json

class Open:
    LOCAL_FILE = os.path.dirname(__file__)
    ARQUIVO_JSON = os.path.join(LOCAL_FILE, 'login.json')

    def __init__(self, modo: str) -> None:
        self.modo = modo
        self.arquivo = None

    def __enter__(self):
        file = open(self.ARQUIVO_JSON, self.modo, encoding='utf-8')
        self.arquivo = file
        return file
    
    def __exit__(self, class_exception, exception_, traceback_):
        self.arquivo.close()
        if class_exception is not None:
            print(f'{class_exception.__name__}: {exception_}')
            return True
        
class Json:

    
    def read_json(self, lista_json_read):
        try:
            with Open('r') as file:
                lista_json_read = json.load(file)
            return lista_json_read
        except FileNotFoundError:
            return self.write_json(lista_json_read)
        
            
    
    def write_json(self, lista_json):
        with Open('w') as file:
            json.dump(lista_json, file, indent=4, ensure_ascii=False)
        return lista_json

