Automatically copies files from a USB on insertion. 

Executable made using Pyinstaller using --windowed argument to make it run in the background.

Should work on all Windows versions, 32 bit and 64 bit. Tested on Windows 7 32 bit and Windows 10 64 bit.

**Instructions for use**

Copy the entire folder containing the executable onto the target PC and run the executable "detectusb2.exe". 

The process will run, copying all .ppt and .pptx files from inserted USBs till the PC is shutdown or the process is terminated.

**P.S.** The process will terminate throwing an error if the USB is removed while files are being copied. 

Need to add a try except condition for this.



