import os
import json
BASE_FILE = os.path.dirname(__file__)
SAVE_DIR = os.path.join(BASE_FILE, 'log.json')
class File:
    def save_file(self, log):
        with open(SAVE_DIR, 'w', encoding='utf-8') as file:
            json.dump(log, file, indent=4, ensure_ascii=False)
            
    def read_file(self, log):
        try:
            with open(SAVE_DIR, 'r', encoding='utf-8') as file:
                log_read = json.load(file)        
            return log_read 
        except FileNotFoundError:
            self.save_file(log)
        return log
            
loggins = File().read_file([])

class Log:
    
    def _log(self, msg):
        raise NotImplementedError('Implemente no módulo')
    
    def log_success(self, msg):
        return self._log(('Success', msg))
    
    def log_error(self, msg):
        return self._log(('Error', msg))
    
    
class LogFileMixin(Log):
    
    def _log(self, msg):
        msg_formatada = {'status': msg[0], 'mensagem': msg[1]}
        loggins.append(msg_formatada)
        File().save_file(loggins)
        

class LogPrintMixin(Log):

    def _log(self, msg):
        print(f'{msg[1]} ({self.__class__.__name__})')
        

    