from multiprocessing import Process as process
from multiprocessing import Pipe
from traceback import format_exc
from subprocess import check_output, CREATE_NO_WINDOW, Popen
from threading import Thread

class Process(process):
    def __init__(self, *args, **kwargs):
        process.__init__(self, *args, **kwargs)
        self._pconn, self._cconn = Pipe()
        self._exception = None

    def run(self):
        try:
            process.run(self)
            self._cconn.send(None)
        except Exception as e:
            tb = format_exc()
            self._cconn.send((e, tb))
            
    @property
    def exception(self):
        if self._pconn.poll():
            self._exception = self._pconn.recv()
        return self._exception

def process_list():
    return check_output(["tasklist"],shell=False,creationflags=CREATE_NO_WINDOW).decode("utf-8").split("\r\n")[3:]

def run(path,executable):
    return Popen([f"{path}\\{executable}"],shell=False,creationflags=CREATE_NO_WINDOW,cwd=path)

def kill(process):
    return Popen(["taskkill","-f","-im",process,"-t"],shell=False,creationflags=CREATE_NO_WINDOW)
