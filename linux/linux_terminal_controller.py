import msvcrt
import sys
import os
from .key_dic import key_dic as kc
import termios
import tty

class Linux_TerminalController:
        
    def hide_cursor(self):
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
    
    def show_cursor(self):
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
        
    def getch(self):
        try:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
    def key(self):
        
        key = '' 
        key = key + str(self.getch())
            
        if "\x1b" in key or "b'\\x00'" in key or "b'\\xe0'" in key:
            
            for i in range(0,1):
                key = key + str(self.getch())
        
        try:
            key = kc[key]
        except:
            key = None

        return key

    def clear(self):
        os.system('cls')