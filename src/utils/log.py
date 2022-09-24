from os import path, mkdir
from time import strftime
from utils.env_paths import LOG_PATH
from utils.process import run


class Log:
    def __init__(self,filename,flush=True):
        if not path.exists(LOG_PATH):
            mkdir(LOG_PATH)
            
        self.filename = f"{filename} - {strftime('%d.%m.%Y %H.%M.%S')}.log"
        self.file_io = open(f"{LOG_PATH}\\{self.filename}","w")

    def write(self, text):
        self.file_io.write(f"[{strftime('%d.%m.%Y %H:%M:%S')}] {text}\n")
        self.file_io.flush()

    def open(self):
        run("{LOG_PATH}\\{self.filename}")

    def close(self):
        self.file_io.close()
