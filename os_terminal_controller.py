import sys
import os
import time
import platform

class Os_Controller:
        
    def __init__(self):
        self.sysOp = self.Get_os()
        self.terminal = None
        self.Set_terminal()
    
    def Get_os(self):
        return platform.system()
    
    def Set_terminal(self):
        if self.sysOp == "Windows":
            print("É windows")
            from windows import windows_terminal_controller
            self.terminal = windows_terminal_controller.Windows_TerminalController()
    
    def ReadKey(self):
        return self.terminal.key()
    
controller = Os_Controller()
print(controller.ReadKey())