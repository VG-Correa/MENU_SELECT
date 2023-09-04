import time
import msvcrt
import platform
import ctypes
from .key_dic import key_dic as kc

class Windows_TerminalController:
        
    def hide_cursor(self):
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
    
    def show_cursor(self):
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
        
    def getch(self):
        tecla = msvcrt.getch()
        return tecla
    
    def key(self):
        while True:
            key = '' 
            key = key + str(self.getch())
                
            if "\x1b" in key or "b'\\x00'" in key or "b'\\xe0'" in key:
                
                for i in range(0,1):
                    key = key + str(self.getch())

            print(key)
            
            try:
                key = kc[key]
            except:
                key = None

            return key
